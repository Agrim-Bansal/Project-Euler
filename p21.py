def factorise(k):
    factors=[]
    a = 1
    b=k

    while a < b:
        b = k//a
        if k%a ==0:
            if a != b:
                factors.append(a)
                factors.append(b)
            else:
                factors.append(a)
        a+=1
    factors.sort()

    return factors


def factorise_2(Dividend, factors: dict):
    if Dividend == 1:
        return factors
    else:
        i=2
        while Dividend%i != 0:
            i+=1
        if i not in factors:
            factors[i] = 1
        else:
            factors[i] += 1
        return factorise_2(Dividend/i, factors)


n = int(input("What is the upper limit?"))
sum_of_factors = []
numbers = [i for i in range(1, n+2)]
amicable_numbers = []

for i in range(1, n+2):
    s = 1
    factors = factorise_2(i, {})
    
    for j in factors:
        s *= int((j**(factors[j]+1)-1)/(j-1))
    s -= i
    sum_of_factors.append(s)

print(sum_of_factors)

for i in range(1, len(numbers)+1):
    try:
        if sum_of_factors[sum_of_factors[i-1]-1] == i and sum_of_factors[i-1] != i:
            amicable_numbers.append(i)
    except(IndexError):
        continue


print(amicable_numbers)
print(sum(amicable_numbers))