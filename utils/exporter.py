import os
from datetime import datetime

def save_result(directory,result,ip):

    if not os.path.exists(directory):
        os.mkdir(directory)

    ip = str(ip).replace("/", "_").replace(":", "-")

    date_format = datetime.now().strftime('%Y-%m-%d__%H:%M:%S')
    file_name = f"{ip}:{date_format}.txt"

    with open(f"{directory}/{file_name}","a",encoding="utf-8") as f:

        f.write(date_format + "\n")
        f.write(ip + "\n\n")

        for line in result:
            f.write(f"{line}\n")
    print (f"[+] Data appended to: {file_name}")
