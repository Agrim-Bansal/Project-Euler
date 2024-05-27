f = open("numbers.txt", "r") 

list = [i.split(' ') for i in f.read().split('\n')]
#list.pop(len(list)-1)

print(list)

for i in range(0,len(list)):
  list[i] = [int(j) for j in list[i]]

for i in range(len(list)-2, -1, -1):
  for j in range(0, len(list[i])):
    list[i][j] += max(list[i+1][j], list[i+1][j+1])

print(list[0])