import base64

# 32 Bytes taken from .bss segment @ 0804A00E
a = "U1FRVVJeVgcBBA0CAANWWw9QBwFTUAtQVQBRWwEGUwY="
# 32 Bytes taken from .bss segment @ 0804A02E
b = "MWVjZmY4YmVjZTk0ODYyODdkYzc2NTIxYTg0YmI3YzA="

flag = "flag{"

a = base64.b64decode(a)
b = base64.b64decode(b)

for i in range(32):

    q = a[i] ^ b[i]    
    flag += chr(q)

flag += "}"

print(flag)
