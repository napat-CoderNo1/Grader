cLetter = False
sLetter = False

txt = input()

for i in txt:
    if i.isupper():
        cLetter=True
    if i.islower():
        sLetter=True

if cLetter == True and sLetter == True:
    print("Mix")
elif cLetter == True:
    print("All Capital Letter")
else:
    print("All Small Letter")