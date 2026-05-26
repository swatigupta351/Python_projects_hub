import pexpect 
import pandas as pd
child = pexpect.spawn("ssh -i web_key.pem ec2-user@65.0.75.80")
index = child.expect(['\\$' , '\]#', pexpect.EOF, pexpect.TIMEOUT] )
if index == 0:
    print("Local user connected")
    child.sendline("df -h")
    child.expect("\\$")
    output = child.before.decode("utf-8")
    with open("output.txt" , "w") as f:
        f.write(output)
    lines = child.before.decode('utf-8').splitlines()
    # print("lines_output" , lines)
    data = []
    header = []
    for line in lines:
        # print("line_output", line)
        parts = line.split()
        # print("parts_output" , parts)
        if len(parts) >=5:
            use_memory = parts[4]
            if use_memory == "Use%": 
                print(line)
                header = parts[0:5] + ["Mounted_on"]
                continue

            if '%' in use_memory :
                use_memory_number = int(use_memory.replace('%', ''))
                if use_memory_number >= 5 and use_memory_number < 20:
                    print(line)
                    data.append(parts)
                    df = pd.DataFrame(data , columns=header )
                    df.to_excel("output.xlsx" , index=False  )
elif index == 1:
    print("Root user connected")
elif index == 2:
    print("Connection closed")
elif index == 3:
    print("timeout")
