import pexpect
import re

SERVER_IP = "13.203.202.74"
USERNAME = "ec2-user"      
PASSWORD = "MY_PASSWORD"   
OUTPUT_FILE = "pexpect_server_output.txt"
PROMPT = r'\$\s*$|#\s*$|\]\s*[\$#]\s*'

# .*          → line ka jo bhi text hai sab 
# [\$#>]      → last me $, #, ya >
#  ?          → optional space
# $           → line ka end h validate krta h 


# ssh -o option_name=value
# StrictHostKeyChecking=no ->: yes/no prompt no 
# encoding='utf-8' -> to get direct string not any bytes data 
# constructor 
# class spawn:
#     def __init__(self, command, encoding=None, timeout=30):

def clean_output(text):
    ansi_escape = re.compile(r'\x1b\[[0-9;]*[a-zA-Z]|\x1b\][^\x07]*\x07|\[\?2004[lh]') # pattern define 
    text = ansi_escape.sub('', text) # replace with empty string
    lines = [
        line for line in text.splitlines()
        if line.strip() and not re.search(r'\[.*@.*\]', line)
    ]
    return '\n'.join(lines) 
try: 
    print ("connecting...") 
    child = pexpect.spawn(f'ssh -i  ~/.ssh/web_key.pem -o  StrictHostKeyChecking=no -o  "SetEnv TERM=dumb" {USERNAME}@{SERVER_IP}',
            encoding= "utf-8",
            timeout= 20
    )

    i = child.expect([
        "password:", # index 0 
        "yes/no",   # index 1 
         PROMPT ,  # index 2
        pexpect.TIMEOUT , # index 3
        pexpect.EOF  # index 4
    ])

    # case 1 
    if i == 0:
        child.sendline(PASSWORD)
        child.expect(PROMPT)


    # Case 2: first-time yes/no

    elif i == 1:
        child.sendline("yes")
        j = child.expect(["password:" , PROMPT , pexpect.TIMEOUT ])
        if j == 0:
            child.sendline(PASSWORD)
            child.expect(PROMPT)
        elif j == 1: 
            print("Passwordless login")
        elif j == 2:
            print("SSH timeout")
            child.close()
            exit()
    elif i == 2:
        print("Passwordless log in ")
    elif i == 3:
        print("SSH timeout")
        child.close()
        exit()
    elif i == 4:
        print("SSH connection failed / EOF received")
        print(child.before)  # shows the actual error message
        exit()

    


       
    commands = ["hostname" , "uptime" , "whoami" , "df -h"]

    output_text = ""

    for cmd in commands:
        print(f"Running : {cmd}")
        child.sendline(cmd)
        child.expect(PROMPT)
        lines = child.before.strip().split('\n')
        output = '\n'.join(lines[1:]).strip()
        output = clean_output(output)

# child.before → jo text match milne se pehle aaya
# child.after → jo text match hua (jis pattern par expect() ruk gaya)

        output_text += f"\n------- {cmd} --------\n"
        output_text += output + "\n"

    with open(OUTPUT_FILE , "w" , encoding = "utf-8") as f:
        f.write(output_text)
    
    print(f"saved in {OUTPUT_FILE}")

    child.sendline("exit")
    child.close()
except Exception as e:
    print("Error :" , e)


    




