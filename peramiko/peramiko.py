import paramiko

host = "3.109.123.10"
username = "ec2-user"
key_path = "/home/swati/swati_projects/my server.pem"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

key = paramiko.RSAKey.from_private_key_file(key_path)

client.connect(hostname=host, username=username, pkey=key)

stdin, stdout, stderr = client.exec_command("uptime")

print(stdout.read().decode())

client.close()
