alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(s,key):
    l=len(key)
    i=0
    res=''
    for c in s:
        if c in alphabet:
            res += chr((ord(c) - ord('a') + ord(key[i%l]) - ord('a'))%26+ord('a'))
            i+=1
        else:
            res += c
    return res


def decrypt(s,key):
    l=len(key)
    i=0
    res=''
    for c in s:
        if c in alphabet:
            res += chr((ord(c) - ord(key[i%l]))%26+ord('a'))
            i+=1
        else:
            res += c
    return res    
if __name__=='__main__':
    text='this is the plain text'
    key='hold'
    enc=encrypt(text,key)
    print enc
    dec=decrypt(enc,key)
    print dec
    