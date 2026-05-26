import paramiko
import os 

SERVER_IP = "13.126.79.255"
USERNAME = "ec2-user"
KEY_PATH = os.path.expanduser("/home/swati/swati_projects/python_projects/pexpect/test_project/web_key.pem")
OUTPUT_FILE = "peramiko_server_output.txt"

commands = ["hostname", "uptime", "whoami", "df -h"]

try:
    print("Connecting...")
    
    # Load the key 
    key = paramiko.RSAKey.from_private_key_file(KEY_PATH)
    
    # create client object and connect ssh
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # StrictHostKeyChecking=no jaisa
    client.connect(hostname=SERVER_IP, username=USERNAME, pkey=key)
    
    print("Connected!")
    
    output_text = ""
    
    for cmd in commands:
        print(f"Running: {cmd}")
        
        stdin, stdout, stderr = client.exec_command(cmd)  # ✅ command run karo
        output = stdout.read().decode('utf-8').strip()     # ✅ output lo - already clean!
        
        output_text += f"\n------- {cmd} --------\n"
        output_text += output + "\n"
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(output_text)
    
    print(f"Saved in {OUTPUT_FILE}")
    client.close()

except Exception as e:
    print("Error:", e)