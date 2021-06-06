from math import gcd
lcm = 1

for i in range(1,20):
    lcm = lcm * (i//gcd(lcm,i))

print(lcm*2)