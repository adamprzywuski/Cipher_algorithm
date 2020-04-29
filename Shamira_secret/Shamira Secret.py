import random
import math
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import base64
import shamir

#basic on https://medium.com/@apogiatzis/shamirs-secret-sharing-a-numeric-example-walkthrough-a59b288c34c4


def string_to_decimal(message):
    hex=str.encode(message)
    hex=hex.hex()
    return int(hex,16)

def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def wielomian(a,x,p,message):
    Y=0
    for i in range(0,len(a)):
         Y=Y+(a[i]*math.pow(x,len(a)-i))

    Y=(Y+message)

    return Y
def encoding(message,N,k):
    print(message)
    p=random.randint(message,message*2)
    a=[]
    #p=91994388364979

    print(p)
    #utworzenie  wielomianu
    for i in range(k-1):
        a.append(random.randint(0,p-10))
    #utworzenie D
    #a=[5481390490034,4103884901909]
    D=[]
    D.append(0)
    for i in range (1,N+1):
        D.append(wielomian(a,i,p,message))

    print(D)
    return D

def decoding(d,k):

    d1=int(float(d[1]))
    d2=int(float(d[2]))
    d3=int(float(d[3]))


    poly=lagrange([1,2,3],[d1,d2,d3])
    function=Polynomial(poly).coef
    print(function)
    score=(int(function[-1]))
    f=int_to_bytes(score)
    #v = base64.b64decode(f)
    #v.decode('utf-8')
    #final_score=score.decode("utf-8")
    #print(score)
    print(f)











if __name__ == '__main__':

    secret=input("Please write your secret to encrypt")
    mess=string_to_decimal(secret)

    #print(mess)
    D=encoding(mess,5,3)
    decoding(D,3)
