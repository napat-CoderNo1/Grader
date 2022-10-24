# not accepted by my self

def isPrime(n):
    if n==1 or n==0:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True

def isUgly(n):
    if n<=0:
        return False
    if n==1:
        return True
    # temp=[]
    for i in range(1, n+1):
        if n%i==0:
            if isPrime(i):
                if i>5:
                    return False
    return True
            # temp.append(i)
    # for i in range(len(temp)):
    #     if isPrime(temp[i]):
    #         if temp[i]>5:
    #             return False
    return True

print(isUgly(214797179))

# n=7

# ถ้า n เป็น 1 หรือ 0 -> True
# แยกตัวประกอบทั้งหมด+เก็บลง list
    # for ตั้งแต่ 1-(n+1) เช็คว่าตัวไหนหาร  n ลงตัวบ้าง
        # หารลงเก็บลง tempList = [1,7]
    # for ไล่ใน tempList ว่า มีตัวที่เป็น จำนวนเฉพาะและมากกว่า 5 หรือไม่
        # มี False
        # ไม่มี True

# Best Version
# def isUgly(self, n: int) -> bool:
#     if n <= 0: return False
#     for i in [2,3,5] :
#         while n % i==0 :
#             n = n//i
#     return n==1

# def isUgly(self, n: int) -> bool:
#     if n==1:
#         return True
#     if n<=0:
#         return False
#     while n%2==0:
#         n/=2
#     while n%3==0:
#         n/=3
#     while n%5==0:
#         n/=5
#     if n==1:
#         return True
#     else:
#         return False