def factorise(k):
    factors=[]
    a = 1
    b=k

    while a < b:
        b = k//a
        if k%a ==0:
            factors.append(a)
            factors.append(b)
        
        a+=1
    factors.sort()
    
    return factors

def isPrime(n):
    if len(factorise(n)) == 2:
        return True
    return False

f = factorise(600851475143)

pf = [i for i in f if isPrime(i)]
print(pf)