word="MISSISSIPPI"
i=0
new={ }
while i<len(word):
    j=0
    counter=0
    total={ }
    while j<len(word):
        if word[j]==word[i]:
            counter+=1
        j+=1
    total.update({word[i]:counter})
    new.update(total)
    i+=1
print(new)