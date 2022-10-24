'''
k = 3
mat = 
[
    index 0 -> [1,1,1],
    index 1 -> [1,0,0],
    index 2 -> [1,1,1],
    index 3 -> [1,0,0]
]

1. สร้างก้อนนี้ออกมา [3,1,3,1]
1.1 สร้างตัวจำลอง [3,1,3,1]

2. หาตัว min = 1

3. for loop หา 1 ใน list

4. เจอปุ็บเก็บค่า index ของมันใน อีก list

[1, 3]

4.1 remove 1 ออกจากตัวหลัก [3,3]
4.2 หาค่า min อีกรอบ [3]

for หา 3 ใน ตัวสำรองอีกรอบ [3,1,3,1]

เจอปุ็บเก็บค่า index ของมันใน อีก list

[1,3,0,2]

'''

def kWeakestRows(mat, k):
    temp = []
    output = []
    for i in range(len(mat)):
        temp.append(mat[i].count(1))
    second = temp.copy()

    while len(second)>0:
        if len(output)==k:
            break
        x = min(second)
        for i in range(len(temp)):
            if len(output)==k:
                break
            if temp[i] == x:
                output.append(i)
                second.remove(temp[i])

    return output

print(kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 2))