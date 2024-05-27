def isPalindrome(n:int):

    if str(n) == str(n)[::-1]:
        return True
    return  False



nums = []
for i in range(100,1000):
    for j in range(100,1000):
        if isPalindrome(i*j):
            nums.append(i*j)

print(max(nums))