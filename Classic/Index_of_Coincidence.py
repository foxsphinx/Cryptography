import Vigenere
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def IC(s):
    l=len(alphabet)
    res=0
    freq=[0 for i in range(l)]
    N=0
    for c in s:
        if c in alphabet:
            freq[alphabet.index(c)]+=1
            N+=1
    for i in freq:
        res+=i*(i-1)
    res = float(res)/N/(N-1)
    return res


def check_IC(ic):
    if ic > 0.65:
        print 'single-passcode'
    elif 0.038<= ic and ic <=0.065:
        print 'multi-passcode'    
        
        
if __name__=='__main__':
    text='''When we leftNewport, it was a thriving cotton town, and I hated to leave. 
    We had built a life there, andit was so disturbing to have to walk away from it. 
    I have said that time and time again. I still have goodfriends there from those days.
    "HELEN WALTONI came out of thatNewportexperience with my pride a little damaged, 
    but I had made money on the saleof the Ben Franklinmore than $50,000. 
    The whole thing was probably a blessing. I had a chance for abrand-new start, 
    and this time I knew what I was doing. Now, at the age of thirty-two, 
    I was afull-fledged merchant; all I needed was a store. Helen and the kids and 
    I started driving around in thespring of 1950 hunting in earnest for one, 
    and northwestArkansasappealed to us for several reasons.'''
    text='thisistheplaintext'
    text=text.lower()
    enc=Vigenere.encrypt(text,'hold')
    ic = IC(enc)
    check_IC(ic)
    print ic