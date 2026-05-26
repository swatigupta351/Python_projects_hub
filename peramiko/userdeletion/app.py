from flask import Flask, request, render_template, send_file
import pandas as pd
import paramiko
import re
import logging

app = Flask(__name__)

# logging setup
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

SSH_USER = "ec2-user"
SSH_KEY = "/mnt/c/Users/ewgpasu/Downloads/web_key.pem"


# Run command on server
def run_command(client, command):
    logging.info(f"Executing: {command}")

    stdin, stdout, stderr = client.exec_command(command)

    out = stdout.read().decode().strip()
    err = stderr.read().decode().strip()

    # save everything to file
    with open("server_output.txt", "a") as f:
        f.write("\n============================\n")
        f.write(f"COMMAND: {command}\n")
        f.write(f"OUTPUT:\n{out}\n")
        if err:
            f.write(f"ERROR:\n{err}\n")

    # log warning after capture
    if err:
        logging.warning(f"Command error: {err}")

    return out, err

# Main logic
def process_server(ip, target_user):
    client = None

    try:
        logging.info(f"Processing started: {ip} - {target_user}")

        # Username validation
        if not re.match("^[a-zA-Z0-9_-]+$", str(target_user)):
            logging.warning(f"{ip} → Invalid username")
            return f"{ip} → Invalid username"

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        logging.info(f"{ip} → Connecting SSH")

        client.connect(
            hostname=ip,
            username=SSH_USER,
            key_filename=SSH_KEY,
            timeout=10,
            banner_timeout=10,
            auth_timeout=10
        )

        logging.info(f"{ip} → SSH connected")

        # Check user exists
        output, error = run_command(client, f"id {target_user}")
        if "no such user" in error.lower() or output == "":
            return f"{ip} → User does not exist"

        # Shell check (safe grep)
        output, _ = run_command(client, f"grep '^{target_user}:' /etc/passwd")
        if "nologin" not in output:
            logging.warning(f"{ip} → Shell not nologin")
            return f"{ip} → Shell not nologin"

        # Process check
        output, _ = run_command(client, f"ps -u {target_user}")
        if len(output.split("\n")) > 1:
            logging.warning(f"{ip} → User running processes")
            return f"{ip} → User running processes"

        # Delete user
        run_command(client, f"sudo userdel {target_user}")
        logging.info(f"{ip} → User deleted")

        # Verify deletion
        output, error = run_command(client, f"id {target_user}")
        if error:
            logging.info(f"{ip} → Deletion verified")
            return f"{ip} → Deleted successfully"
        else:
            logging.error(f"{ip} → Deletion failed")
            return f"{ip} → Deletion failed"

    except Exception as e:
        logging.error(f"{ip} → SSH failed: {str(e)}")
        return f"{ip} → Not reachable / SSH failed"

    finally:
        if client:
            client.close()
            logging.info(f"{ip} → Connection closed")


# Home page
@app.route('/')
def home():
    logging.info("Home page accessed")
    return render_template('upload.html')


# Upload route
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    df = pd.read_excel(file)

    if df.empty:
        return "Excel file is empty"

    df.columns = df.columns.str.strip().str.lower()

    if 'ip' not in df.columns or 'username' not in df.columns:
        return "Invalid Excel format (required: ip, username)"

    results = []
    excel_results = []

    for _, row in df.iterrows():
        ip = row['ip']
        user = row['username']

        logging.info(f"Processing {ip} - {user}")

        result = process_server(ip, user)

        results.append(result)

        clean_result = result.split("→")[-1].strip()
        excel_results.append(clean_result)

    df['remark'] = excel_results

    df.to_excel("output.xlsx", index=False)

    return render_template("result.html", results=results)


# Download route
@app.route('/download')
def download():
    logging.info("File downloaded")
    return send_file("output.xlsx", as_attachment=True)


# Run app
if __name__ == '__main__':
    app.run(debug=True)