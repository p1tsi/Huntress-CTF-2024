import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("challenge.ctf.games", 31693))

d = s.recv(1024)
while d:
    try:
        txt = d.decode()
        print(txt)
        if "Opponent" in txt:
            move = txt.split("\n")[1].split(":")[1].strip()
            print(move)
            
            if move == "strike":
                print("block")
                s.send(b"block\r\n")
            elif move == "retreat":
                print("strike")
                s.send(b"strike\r\n")
            elif move == "advance":
                print("retreat")
                s.send(b"retreat\r\n")
            else:
                print("advance")
                s.send(b"advance\r\n")
            
    except:
        pass
        
    d = s.recv(1024)
