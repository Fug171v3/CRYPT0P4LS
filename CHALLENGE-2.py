import codecs
def xor():
    code1=codecs.decode("1c0111001f010100061a024b53535009181c","hex")
    code=int.from_bytes(code1, "big")
    print(code)
    code2=int("686974207468652062756c6c277320657965",16)
    f=code2^code
    print(hex(f))
xor()
