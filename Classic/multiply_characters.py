alphabet=['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def gen(key):
    substitution=[]
    for i in range(5):
        for j in range(5):
            if 5*i+j<9:
                substitution.append(key[i]+key[j])
            else:
                substitution.append(key[i]+key[j])
    return substitution
    
    
def encrypt(s,key):
    if len(set(key)) !=5:
        print "key must be 5 characters and there can't be duplicated charaters in the word!!"
        return ''
    res=''
    table=gen(key)
    for i in s:
        if i == 'j':
            i='i'
        if i in alphabet:
            res+=table[alphabet.index(i)]
        else:
            res+=i
    return res

def decrypt(s,key):
    if len(set(key)) !=5:
        print "key must be 5 characters and there can't be duplicated charaters in the word!!"
        return ''
    res=''
    table=gen(key)
    l=len(s)
    separate=[]
    i=0
    res=''
    while i <l:
        if i == l-1:
            res+=s[i]
            return res
        tmp=s[i]+s[i+1]
        if tmp in table:
            res+=alphabet[table.index(tmp)]
            #separate.append(tmp)
            i+=2
        else:
            #separate.append(s[i])
            res+=s[i]
            i+=1
    return res
    
       

if __name__=='__main__':
    key='times'
    text='this is a test!'
    en=encrypt(text,key)
    print en
    de=decrypt(en,key)
    print de