def checkRecord(s):
    if 'LLL' in s or s.count('A') >= 2:
        return False
    return True

s="PPALLL"
print(checkRecord(s))