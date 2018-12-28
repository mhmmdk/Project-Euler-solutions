from time import time, sleep
from fractions import Fraction
itime = time()

def sieve(n):
    p = [5]
    i = 5
    while i < n - 2:
        #i += 2
        p += [i+2]
        i += 6
        p += [i]
    #p = (i+j for i in range(3, n, 6) for j in (2,4))
    sqrtN = int(n**0.5)+1
    pr = []
    yield 2
    yield 3

    for i in p:
        for j in pr:
            if not i%j:
                i = 0
                break
        if i:
            if i<sqrtN:
                pr += [i]
            yield i
            
siev = list(sieve(1))
#print(len(siev), siev[-10:])
#print(len(set(range(1000001))- set(siev)))

'''
def primeFactors(n):
    ans = set()
    if not n%2:
        n /=2
        ans.add(2)
    if not n%3:
        n/= 3
        ans.add(3)
    i = 5
    sq = n**0.5
    while i < sq+1:
        if not n%i:
            n /= i
            ans.add(i)
        i += 2
    for a in ans:
        while not n%a:
            n /= a
    if n != 1:
        ans.add(n)
    return ans
'''

ma = 0
trace = 0
for n in range(1,1000001):#9007198, 9007199):
    ans = []
    nn = n
    phi = Fraction(1)
    if not n%2:
        #n /=2
        phi *= 1-Fraction(1/2)
        '''while not n%2:
            n/=2'''
        ans += [2]
    if not n%3:
        #n/= 3
        phi *= 1-Fraction(1/3)
        '''while not n%3:
            n/=3'''
        ans += [3]
    i = 5
    sq = n**0.5 +1
    while i < sq:
        if not n%i:
            #n /= i
            phi *= 1-Fraction(1/i)
            '''while not n%i:
                n/= i'''
            ans += [i]
        i += 2
        if not n%i:
            #n /= i
            phi *= 1-Fraction(1/i)
            '''while not n%i:
                n/= i'''
            ans += [i]
        i += 4

        
    for a in ans:
        while not n%a:
            n /= a
    if n != 1:
        phi *= 1-Fraction(1/n)
        #ans += [n]
    if ma < 1/phi:
        ma = 1/phi
        trace = nn
    #print(1/phi)
    #print(nn, float(nn*phi))
print(float(ma), ma, trace)

'''count = 0
for i in range(1,100000):
    p = primeFactors(i)
    if len(p) < 2:
        count+=1
    #print(p)
print(count)'''









            
print(time()-itime)
