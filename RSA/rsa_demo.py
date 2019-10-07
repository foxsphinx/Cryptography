from common_math import *


modules='''35:56:f7:11:80:78:d3:82:30:5e:56:69:c4:f2:5e:
    53:9e:1b:9b:21:4c:bf:05:cb:19:40:47:7a:3c:be:
    2b:59:5d:99:12:24:7a:ee:73:16:1f:5e:ab:76:e5:
    75:75:bd:30:4e:7b:e3:9d:42:94:ca:b7:82:c0:8b:
    a6:7a:94:cf:bd:d9:b4:f8:08:b1:05:de:29:7c:8d:
    0e:a7:48:e1:0f:68:6c:4f:1e:71:d6:7e:98:61:e8:
    ba:1d:16:3f:f3:e3:2b:58:95:95:fe:79:20:b6:ba:
    ff:2c:a0:5c:b7:ab:85:52:54:63:74:fc:0f:6b:99:
    8f:5a:42:4b:8a:69:30:c2:02:c9:8d:cf:2a:3c:a7:
    e3:70:09:e0:02:1c:95:ba:7d:7d:7a:fd:cf:12:62:
    cd:2c:a1:7f:c3:8d:c1:a4:db:68:6f:8f:ef:c5:c0:
    ae:1b:29:52:f7:1a:20:f2:a5:c9:0c:82:88:a1:69:
    65:6c:8c:7a:9a:f6:40:da:4b:aa:54:c1:37:1c:64:
    06:02:42:85:da:09:53:30:b6:ef:da:d8:7d:b5:89:
    f0:c0:12:90:4a:fe:41:59:49:1c:5a:58:92:67:40:
    dc:74:ca:5c:b2:f4:b5:ca:05:eb:8e:38:76:12:3c:
    b7:75:f6:10:3c:22:0e:32:02:c9:5b:65:dc:58:36:
    23
    '''
privateExponent='''1c:de:5a:8e:20:68:44:a1:3b:a8:73:40:7f:95:65:
    b3:ff:e8:95:07:6a:d0:20:44:92:00:16:2f:74:5c:
    c0:7d:77:88:f7:26:c3:59:f6:f3:cc:3a:a2:b6:90:
    ee:07:b1:43:49:d7:07:93:ff:8b:24:44:3a:02:18:
    13:1c:59:1a:2e:78:7b:d7:9a:6c:a4:ee:5e:a9:c8:
    76:5b:d7:b7:e7:6c:ee:e1:cb:6a:75:5a:c3:02:8a:
    c0:e0:29:40:a7:b1:15:ae:b6:17:1e:49:54:89:51:
    9f:f5:f9:3c:f5:33:61:ce:f3:59:78:e1:4b:3f:43:
    37:30:f4:9c:89:e6:f0:ba:31:82:de:d8:e7:f0:32:
    dc:a3:31:bd:dd:c3:e0:6c:c9:08:00:f8:2a:86:9d:
    b8:f4:3d:ae:55:b8:ff:2f:92:e2:7f:3e:5e:0d:11:
    7c:af:8f:38:be:81:b1:6b:fe:31:2f:38:37:b7:4d:
    70:2a:9f:d4:d3:20:1e:85:ed:ce:83:3a:7c:fc:b6:
    ec:f9:a6:92:2c:f1:42:fd:18:85:18:e9:ee:fe:ad:
    e8:35:95:cb:3a:4d:ea:d4:1d:0c:00:f1:03:f2:4d:
    02:53:74:ec:a1:a6:27:ac:87:3f:cf:1e:18:ed:d0:
    33:ca:0e:43:d9:31:6f:63:28:11:05:a0:c7:9b:9e:
    31
    '''
prime1='''7e:63:af:09:d3:95:90:84:08:f6:f2:c2:4d:03:5f:
    8a:13:91:c4:a3:2a:60:ba:e6:5e:05:0b:a9:2f:79:
    e6:7d:d5:a8:2c:b4:c8:06:35:3b:3c:fb:10:b5:88:
    94:78:ea:05:ad:11:e0:9f:68:2b:df:02:6c:39:e3:
    f2:4a:e1:91:37:d8:61:84:02:20:4b:5a:97:d1:0a:
    37:f2:18:43:17:94:53:cc:1c:f8:24:30:80:68:57:
    b3:05:2f:05:f7:5c:21:28:bf:ef:d8:45:4a:1f:21:
    43:87:78:fb:8e:45:22:ae:ab:d3:e3:09:fc:5f:dc:
    77:7b:4f:f9:31:1f:6e:8d
    '''
prime2='''6c:09:f2:7d:85:1f:e3:ca:94:83:01:3b:01:83:b6:
    b3:b1:6f:64:98:46:d0:4a:01:da:51:74:27:cd:28:
    8f:5e:17:b2:a2:00:19:b6:92:1b:b2:8b:ac:75:de:
    0a:00:24:44:7b:b7:ae:f1:59:87:23:58:fd:9b:d0:
    1b:ef:78:e5:7b:c5:5f:df:b8:99:33:69:f4:42:3b:
    15:62:a6:06:35:01:00:47:dc:8d:ad:81:ad:5f:82:
    42:26:d4:bc:5c:ce:49:fa:0e:d8:59:f8:c0:f7:9c:
    c5:97:d0:7c:67:4d:c7:78:74:6f:20:f9:3c:78:20:
    a1:5f:d0:e4:a0:82:23:6f
    '''



def to_dec(modules):
    module=''
    for i in modules:
        if i in ('1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','A','B','C','D','E','F'):
            module=module+i
    module_int=int(module,16)
    return module_int



if __name__ == '__main__':
    module_int=to_dec(modules)
    privatekey=to_dec(privateExponent)
    publickey=65537
    prime1_int=to_dec(prime1)
    prime2_int=to_dec(prime2)
    message=9888567898760987898
    
    ################################################################
    # RSA Encryption and Decryption                                #
    ################################################################
    encrypted=cal_power_model(message,publickey,module_int)
    decrypted=cal_power_model(encrypted,privatekey,module_int)
    print 'RSA encryption and decryption'
    print encrypted
    print decrypted
    
    ################################################################
    # Calculate Private Key                                        #
    ################################################################
    phi=(prime1_int-1)*(prime2_int-1)
    priv,k,gcd=extendedGCD(publickey,phi)
    while priv<0:
        priv=priv+phi
    print 'Calculate the private key'
    print priv
    print priv == privatekey
    
    #################################################################
    # More recent way to calculate the private key                  #
    #################################################################
    n=LCM(prime1_int-1,prime2_int-1)
    priv,k,g=extendedGCD(publickey,n)
    print 'New private key'
    print priv
    print privatekey
    
    ##################################################################
    # Use new private key generate above to decrypted and check      #
    ##################################################################
    encrypted=cal_power_model(message,publickey,module_int)
    decrypted=cal_power_model(encrypted,priv,module_int)
    print 'Use new key to decrypt'
    print decrypted
    print decrypted==message