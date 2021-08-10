dict1 =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
counter=0
for keys,value in dict1.items():
    for i in value:
        counter+=1
print(counter)