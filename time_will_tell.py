import socket
import time
import string

HOST = "challenge.ctf.games"
PORT = 31224

letters = string.ascii_lowercase + string.digits

secret = ""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(s.recv(300))
    
    while len(secret) < 8:
        for i in range(len(letters)):
            test = letters[i]
            pad_len = 7-len(secret)
            pad = b"a"*pad_len
            trial = secret.encode() + test.encode() + pad + b"\n"
            #print(trial.decode())
            start = time.time()
            s.send(trial)
            s.recv(100)
            delta = time.time() - start
            #print(delta)
            if delta > (0.26 + 0.1*len(secret)):
                #print(delta)
                secret += test
                print(secret)
                break

    
    s.send(secret.encode()+b"\n")
    print(s.recv(200))  
