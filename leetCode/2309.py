'''
logic

"arRAzFif"

lis=[]
for loop
    a   -> check ว่าเป็นตัวเล็กหรือใหญ่ 
    เล็ก -> check ว่ามีตัวใหญ่อยู่ด้วยมั้ย
    ถ้ามี
        เก็บ a ลง list
ไปตัวถัดไป

lis=[a, r, f]
chceck ว่า list ว่างมั้ย
    ถ้าว่าง
        return ""
    ถ้าไม่ว่าง
        lis=['a','r','f']
        lis = [ord(i) for i in lis]
        output = max(lis)
        print(chr(output).upper())
'''

def greatestLetter(s):
    lis=[]
    for i in s:
        if i.islower():
            temp=i.upper()
        elif i.isupper():
            temp=i.lower()
        if temp in s and temp.upper() not in lis:
            lis.append(temp.upper())
    if len(lis) == 0:
        return ""
    lis = [ord(i) for i in lis]
    return max(chr(max(lis)))

print(greatestLetter("AbCdEfGhIjK"))