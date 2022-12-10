num = int(input("Enter number of group: "))

lis=[]

for i in range(num):
    group = [int(i) for i in input().split()]
    x = max(group)
    y = min(group)
    group = x-y
    lis.append(group)

print(max(lis))
print(min(lis))
print(max(lis)-min(lis))

