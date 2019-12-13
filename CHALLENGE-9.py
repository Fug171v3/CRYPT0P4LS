import base64
from Crypto.Cipher import AES
def padding(pt):
    a=len(pt)
    b=a%16
    if b==0:
        for i in range(16):
            pt=pt+chr(16)
    else:
        for i in range(16-b):
            pt=pt+chr(16-b)
    return pt
def depadding(pt):
    a=len(pt)
    c=pt[a-1]
    c=int(c)
    bt=""
    bt=pt[0:a-c]
    return bt
def encrypt(key,pt):
    pt=padding(pt)
    cipher = AES.new(key, AES.MODE_ECB)
    ct = cipher.encrypt(pt)
    print("the cipher text is ",ct)
    return ct
def decrypt(key,ct):
    cipher = AES.new(key, AES.MODE_ECB)
    pt = cipher.decrypt(ct)
    return pt
def main():
    pt=input("enter plain text")
    key="YELLOW SUBMARINE"
    ct=encrypt(key,pt)
    pt=decrypt(key,ct)
    pt=depadding(pt)
    print(pt)
main()
