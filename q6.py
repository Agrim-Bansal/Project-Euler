sq_s=0
s=0
for i in range (1,101):
    sq_s += i**2
    s += i

print(s**2 - sq_s)