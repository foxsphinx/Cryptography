
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def gen(key,begin):
    keyGen=[]
    for i in key:
        if i not in keyGen:
            keyGen.append(i)
    for i in alphabet:
        if i not in keyGen:
            keyGen.append(i)
    k=ord(begin)-ord('a')
    for i in range(k):
        tmp=keyGen[-1]
        keyGen.pop()
        keyGen.insert(0,tmp)
    return keyGen

def encryt(plain_text,key):
    decrept_text=''
    for i in text:
        if i in alphabet:
            t=alphabet.index(i)
            decrept_text+=key[t]
        else:
            decrept_text+=i
    return decrept_text

def decrypt(encrypted,key):
    plain_text=''
    for i in encrypted:
        if i in key:
            t=key.index(i)
            plain_text+=alphabet[t]
        else:
            plain_text+=i    
    return plain_text


if __name__ == '__main__':
    key=gen("pacific",'k')
    text="help i am lost!"
    enc=encryt(text,key)
    print enc
    dec=decrypt(enc,key)
    print dec
    
    