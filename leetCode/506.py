def findRelativeRanks(score):
    real = score.copy()
    score.sort(reverse=True)
    # print(score)
    tempDict = {}
    for i in range(len(score)):
        if i==0:
            tempDict.update({score[i]:"Gold Medal"})
        elif i==1:
            tempDict.update({score[i]:"Silver Medal"})
        elif i==2:
            tempDict.update({score[i]:"Bronze Medal"})
        else:
            tempDict.update({score[i]:str(i+1)})
    # print(tempDict)
    # print(real)
    for i in range(len(real)):
        real[i] = tempDict[real[i]]
    return real

def findRelativeRanks2(score):
    output = []
    real = score.copy()
    score.sort(reverse=True)

    for i in range(len(real)):
        if real[i]==score[0]:
            output.append("Gold Medal")
        elif real[i]==score[1]:
            output.append("Silver Medal")
        elif real[i]==score[2]:
            output.append("Bronze Medal")
        else:
            for j in range(len(score)):
                if real[i]== score[j]:
                    output.append(str(j+1))
    return output

def findRelativeRanks(score):
    output = []
    real = score.copy()
    score.sort(reverse=True)

    for i in range(len(real)):
        if real[i]==score[0]:
            output.append("Gold Medal")
        elif real[i]==score[1]:
            output.append("Silver Medal")
        elif real[i]==score[2]:
            output.append("Bronze Medal")
        else:
            output.append(str(score.index(real[i])+1))
    return output


print(findRelativeRanks([10,3,8,9,4]))

'''
 0  1 2 3 4
[10,3,8,9,4]

 0  1 2 3 4
[10,9,8,4,3]

{10:gold, 9:silver, 8:bronze, 4:index+1, 3:index+1}

ยัดค่าคืนให้ list แรกสุด
'''
