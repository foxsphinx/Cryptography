alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l=len(alphabet)

def encrypt(s):
    res=''
    for i in s:
        if i in alphabet:
            res+=alphabet[l - alphabet.index(i)-1]
        else:
            res+=i
    return res

def decrypt(s):
    return encrypt(s)

if __name__=='__main__':
    text='this is a test!'
    en=encrypt(text)
    print decrypt(en)