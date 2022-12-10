# def toGoatLatin(sentence):
#     output=[]
#     vowel = ['a', 'e', 'i', 'o', 'u']
#     x = sentence.split()
#     print(x)
#     for i in range(len(x)):
#         if x[i][0].lower() in vowel:
#             temp = x[i]+"ma"
#             temp +=('a'*(i+1))
#             output.append(temp)
#         else:
#             temp = x[i][0]
#             temp1 = x[i][1:]
#             temp1 = temp1+temp+"ma"
#             temp1+=("a"*(i+1))
#             output.append(temp1)
    
#     return " ".join(output)


def toGoatLatin(sentence):
    ret = [str(word) for word in sentence.split()]
    for i in range(len(ret)):
        if(ret[i][0].lower() in "aeiou"):
            ret[i] += "ma"
        else:
            ret[i] = ret[i][1:] + ret[i][0] + "ma"
        ret[i] += "a" * (i+1)
    return " ".join(ret)

def toGoatLatin(sentence):
    ret=[]
    sen = sentence.split()
    for i in range(len(sen)):
        output = sen[i]
        print(output)
        if output[0].lower() in "aeiou":
            output+="ma"
        else:
            output = output[1:] + output[0] + "ma"
        output = output+('a'*(i+1))
        ret.append(output)
    return " ".join(ret)
            
print(toGoatLatin("I speak Goat Latin"))