def groupAnagrams(strs):
    temp = strs.copy()
    temp = ["".join(sorted(temp[i])) for i in range(len(temp))]
    print(temp)
    temp = set(temp)
    temp = [[temp.pop()] for i in range(len(temp))]
    print("temp =", temp)
    print("strs =", strs)
    
    for i in range(len(strs)):
        for j in range(len(temp)):
            temp2 = "".join(sorted(strs[i]))
            # print(temp2)
            if temp2 in temp[j]:
                temp[j].append(strs[i])

    for i in range(len(temp)):
        temp[i].pop(0)

    output = sorted(temp, key=len)
    
    for i in range(len(output)):
        output[i].sort()

    return output

# def groupAnagrams(strs):
#         ana_dict = dict()

#         for word in strs:            
#             new_word = "".join(sorted(word))
#             if new_word in ana_dict:
#                 ana_dict[new_word].append(word)
#             else:
#                 ana_dict[new_word] = [word]
#         return list(ana_dict.values())
    

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))