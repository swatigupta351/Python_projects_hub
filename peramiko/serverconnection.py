# code for connecting the remote server 

import paramiko

client = paramiko.SSHClient() # client object , sshclient class in paramiko library
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # 

try: # we use try when we want to handle error like block can be produce error as well so to avoide code crash we use try and excepty. 
    # risky kaam
    client.connect(
        hostname="13.203.155.186",
        username="ec2-user",
        key_filename="/home/swati/swati_projects/my server.pem"
    )

    print("Connected")

    stdin, stdout, stderr = client.exec_command("uptime") # exe_command 3 object return krta h stdin , stdout, stderr 
    # “stdin ka use tab hota hai jab hume server par chal rahi command ko input dena ho.”
    print(stdout.read().decode())

except Exception as e: # e is a variable error object m jo error ayega vo is variable m store hoga 
    # agar error aaya
    print("Error aaya:", e)

finally:
    # hamesha chalega
    client.close()
    print("Connection closed")

# # try-except
# ➡️ code ke around lagta hai
# ➡️ error handle karta hai