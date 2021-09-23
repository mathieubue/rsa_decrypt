import math
import binascii 
from Crypto.Util.number import inverse
c = int("0x10891034ce51c23bfe2f7bf29a62938e".strip("0x"), 16)
e = int("0x10001".strip("0x"), 16)
n = int("0x25b8f38aed4a22b31dde75e46e276d0d".strip("0x"), 16) #50141758098469981608372237550616014093
#factordb.com/index.php?query=50141758098469981608372237550616014093&use=n&n=1&x=1&b=1&d=1&VP=on&VC=on&EV=on&OD=on&PR=on&FF=on&PRP=on&CF=on&U=on&C=on&perpage=20&format=1
p= 5665192965464669089
q= 8850847341676960237


#n=p*q
phi = (q-1)*(p-1)
d = inverse(e, phi)

m = pow(c, d, n)   # m=1179402567 
print('m='+str(m)) 
m_hex = hex(m)     # m_hex: 0x464c4147L 
m_hex = m_hex[2:]  # on retire 0x 
m_hex = m_hex.replace('L','')  # on retire L 
m_txt = repr(binascii.unhexlify(m_hex)) # m_txt ='FLAG' 
print ("Message en clair: "+m_txt) 



