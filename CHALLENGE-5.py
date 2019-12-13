def main():
    pt=input("enter the string")
    key="ICE"
    size=len(pt)
    j=0
    ch=b''
    for i in pt:
        ch=ch+bytes(ord(i)^ord(key[j]))
        if (j+1) == len(key) :
            j=0
        else:
            j=j+1
    print(ch)
main()
