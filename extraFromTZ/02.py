v = int(input("Enter number of vivek's lotterry: "))
vnum = input().split()
k=int(input("Enter k:"))
knum = input().split()

x=[vnum[i][3:] for i in range(len(vnum))]

count = 0

for i in range(len(x)):
    if x[i] in knum:
        count+=1

print(count)
