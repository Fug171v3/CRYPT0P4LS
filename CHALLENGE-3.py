import codecs
import string
def xor():
    a={'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    b= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max1=0
    k=""
    str1=codecs.decode("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736","hex")
    code=str1.decode("utf-8")
    for i in string.printable:
        sum1=0
        e=""
        a={'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
        for j in code:
            e=e+chr(ord(i)^ord(j))
        for letter in e.upper():
            if letter in b:
                a[letter] += 1
        for g in b:
            sum1=sum1+a[g]
        if i==0:
            max1=sum1
            c=i
        else:
            if max1>sum1:
                max1=max1
                c=c
            else:
                max1=sum1
                c=i
    for j in code:
        k=k+chr(ord(c)^ord(j))
    print(k)
xor()
