from pwn import *
X=bytes.fromhex('1c0111001f010100061a024b53535009181c')
Y=bytes.fromhex('686974207468652062756c6c277320657965')
xord=xor(X,Y)
answer = bytes.hex(xord)
correctanswer = '746865206b696420646f6e277420706c6179'
if (answer == correctanswer):
    print("correct")
else:
    print("hang yourself")
