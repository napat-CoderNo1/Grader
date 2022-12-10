n = int(input("Enter number: "))

lis = []

if n>2:
    temp=[]
    x=[]
    n=n-2
    temp.append(2)
    x.append(2)
    x.append(n)
    for i in range(n):
        temp.append(1)
    lis.append(temp)
    print(x)

print(lis)