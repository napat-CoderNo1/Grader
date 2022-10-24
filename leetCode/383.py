def canConstruct(ransomNote, megazine):
    for i in ransomNote:
        count1 = ransomNote.count(i)
        count2 = megazine.count(i)
        if count2<count1:
            return False
    return True

ransomNote = "a"
megazine = "b"

print(canConstruct(ransomNote, megazine))