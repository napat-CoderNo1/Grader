'''
lis1 = [[1,2,3],[3,2,1],[1,3,2]]

lis2 = [[1,1,1],[1,1,1],[1,1,1]]
'''

matrix = input().split()
row = int(matrix[0])
column = int(matrix[1])

lis1=[]
lis2=[]

for i in range(row*2):
    x = [int(i) for i in input().split()]
    if i>=row:
        lis2.append(x)
    else:
        lis1.append(x)

for i in range(len(lis1)):
    for j in range(len(lis1[i])):
        print(lis1[i][j]+lis2[i][j], end=' ')
    print("")