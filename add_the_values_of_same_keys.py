dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
result = {}
for x,y in dic1.items():
    for i,j in dic2.items():
        if  x==i:
            a=y+j
            result.update({x:a})
            print(result)
        result.update(dic1)
        result.update(dic2)
        result.update(dic3)
