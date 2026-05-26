# WAP to connect a server and run a command and collect the output. 
# IMPORTANT** 
# Ctrl+C  →  Kill        →  infinite loop, hang
# Ctrl+D  →  EOF/Logout  →  terminal band, python exit
# Ctrl+Z  →  Pause       →  background mein dalo
# Ctrl+L  →  Clear       →  screen saaf karo
# Ctrl+R  →  Search      →  history mein dhundho
# Ctrl+U  →  Line hata   →  galat command mita do
# Ctrl+A  →  Line start  →  cursor shuruaat pe
# Ctrl+E  →  Line end    →  cursor end pe

# sendline(cmd)      →  cmd + Enter        →  normal commands
# send(cmd)          →  cmd only           →  manual control
# sendcontrol('c')   →  Ctrl+C             →  kill process
# sendcontrol('d')   →  Ctrl+D             →  EOF/logout  
# sendeof()          →  Ctrl+D shortcut    →  EOF/logout
# sendintr()         →  Ctrl+C shortcut    →  kill process

import pexpect

child = pexpect.spawn("ssh -i web_key.pem ec2-user@43.204.229.13")
index = child.expect(['\\$' , '\]#' , pexpect.EOF , pexpect.TIMEOUT])
if index == 0:
    print("connected local user")
    child.sendline('uname -a')
    child.expect('\\$')
    print(child.before)
    print(child.before.splitlines())
    print(child.before.splitlines()[0])
    print(child.before.splitlines()[1])
    print(child.before.splitlines()[2])
    print(child.before.splitlines()[3])
    lines = child.before.splitlines()
    for line in lines:
        print(line)
    uname_output = child.before.decode('utf-8')
    with open("uname_output.txt" , "w") as f:
        f.write(uname_output)
    child.sendline('df -h')
    child.expect('\\$')
    print(child.before)
    df_output = child.before.decode('utf-8')
    with open("df_output.txt" , "w") as f:
        f.write(df_output)
    child.sendline('free -m')
    child.expect('\\$')
    print(child.before)
    free_output = child.before.decode('utf-8')
    with open("free_output.txt" , "w") as f:
        f.write(free_output)
    with open("all_output.txt", "a") as f:
        f.write(uname_output)
        f.write(df_output)
        f.write(free_output)
        
elif index == 1:
    print("connected root user")
elif index == 2:
    print("Connection closed")
elif index == 3:
    print("timeout")
