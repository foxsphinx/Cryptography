alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encrypt(s,n):
    while n < 0:
        n+=26
    n%=26
    res=''
    for i in s:
        if i in alphabet:
            res+=chr(((ord(i)-ord('a'))+n)%26+ord('a'))
        else:
            res+=i
    return res

def decrypt(s,n):
    return encrypt(s,-n)

if __name__ == '__main__':
    a='this is a test!'
    b=encrypt(a,13)
    print b
    c=encrypt(b,13)
    print c