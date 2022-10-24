def mergeAlternately(word1, word2):
    output = ""
    lword = [len(word1), len(word2)]
    l = min(lword)
    for i in range(l):
        output+=word1[i]
        output+=word2[i]
    
    if len(word1)>l:
        output+=word1[l:]
    elif len(word2)>l:
        output+=word2[l:]

    return output

def mergeAlternately2(word1, word2):
    output = ""
    lword = [len(word1), len(word2)]
    l = min(lword)
    for i in range(l):
        output+=word1[i]
        output+=word2[i]
    
    output+=word1[l:]
    output+=word2[l:]

    return output

print(mergeAlternately2("ab","pqrs"))
    
