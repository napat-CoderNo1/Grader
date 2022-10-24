# Tips Loop from the back

def romanToInt(rNum: str):
    roman = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }

    interger = 0
    # C M X L I V
    # 0 1 2 3 4 5
    for i in range(len(rNum)-1, -1, -1):
        if i == len(rNum)-1:
            interger+=roman[rNum[i]]
            continue
        if roman[rNum[i]] < roman[rNum[i+1]]:
            interger-=roman[rNum[i]]
        else:
            interger+=roman[rNum[i]]
    return interger

print(romanToInt("MCMXCIV"))
