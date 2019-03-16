from time import time
from time import sleep
n = 210

st = time()

def num_factors(n):
    num = n
    answer = 2
    i = 2

    temp = 0
    while not num%i:
        num //= i
        temp += 1

    answer *= temp+1



    i = 3             
    while i < num**0.5:
      
        # Reducing num to not multiple of i
        temp = 0
        while not num%i:
            num //= i
            temp += 1

        answer *= temp+1

        i += 2

    if not num**0.5%1:
        answer /= 2
        answer *= 3
        

    return answer
    print(answer)

    
print('________THE___________%s__________END________'%(time() - st))
