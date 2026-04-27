from flask import Flask, request, render_template, send_file
import pandas as pd
import paramiko
import re #regex for user validation 



app = Flask(__name__) # flask initialize 

SSH_USER = "ec2-user"
SSH_KEY = "/mnt/c/Users/ewgpasu/Downloads/web_key.pem"


# Run command on server
def run_command(client, command): # client - SSH connection Object 
    stdin, stdout, stderr = client.exec_command(command)
    return stdout.read().decode().strip(), stderr.read().decode().strip()
    
    # run_command = “ function  to run command on remote server and show result”

    #stdout.read() → output bytes me aata hai
#.decode() → string me convert
# .strip() → extra spaces/newline hata deta hai


# Main logic
def process_server(ip, target_user):
    client = None
    try:
        # Username validation
        if not re.match("^[a-zA-Z0-9_-]+$", str(target_user)):
            return f"{ip} → Invalid username"

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # SSH connect
        client.connect(
            hostname=ip,
            username=SSH_USER,
            key_filename=SSH_KEY,
            timeout=5,
            banner_timeout=5,
            auth_timeout=5
        )

        # Check user exists -> function call 
        output, error = run_command(client, f"id {target_user}")
        if error:
            return f"{ip} → User does not exist"

        # Shell check
        output, _ = run_command(client, f"grep {target_user} /etc/passwd")
        if "/sbin/nologin" not in output:
            return f"{ip} → Shell not nologin"

        # Process check
        output, _ = run_command(client, f"ps -u {target_user}")
        if len(output.split("\n")) > 1:
            return f"{ip} → User running processes"

        # Delete user
        run_command(client, f"sudo userdel {target_user}")

        # Verify deletion
        _, error = run_command(client, f"id {target_user}")
        if error:
            return f"{ip} → Deleted successfully"
        else:
            return f"{ip} → Deletion failed"

    except Exception:
        return f"{ip} → Not reachable / SSH failed"

    finally:
        if client:
            try:
                client.close()
            except:
                pass


# Home page
@app.route('/') # decorator 
def home():
    return render_template('upload.html')


# Upload route
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    # Read Excel
    df = pd.read_excel(file)

    if df.empty:
        return "Excel file is empty"

    # Normalize column names
    df.columns = df.columns.str.strip().str.lower()

    if 'ip' not in df.columns or 'username' not in df.columns:
        return "Invalid Excel format (required: ip, username)"

    results = []         # UI ke liye (with IP)
    excel_results = []   # Excel ke liye (without IP)

    for _, row in df.iterrows():
        ip = row['ip']
        user = row['username']

        print(f"Processing {ip} - {user}")

        result = process_server(ip, user)

        # UI ke liye full result
        results.append(result)

        # Excel ke liye IP hata do
        clean_result = result.split("→")[-1].strip()
        excel_results.append(clean_result)

    # Add remark column in Excel
    df['remark'] = excel_results

    # Save file
    df.to_excel("output.xlsx", index=False)

    # Show result on UI
    return render_template("result.html", results=results)


# Download route
@app.route('/download')
def download():
    return send_file("output.xlsx", as_attachment=True)


# Run app
if __name__ == '__main__':
    app.run(debug=True)