# SampleDic={0: 10, 1: 20}
# SampleDic[3]=30
# print(SampleDic)


# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# add={}
# for x in (dic1,dic2,dic3):
#     add={**dic1,**dic2,**dic3}
# print(add)


# Dic={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# def find_key(K):
#     if K in Dic:
#         print('Key is present in the dictionary')
#     else:
#         print('Key is not present in the dictionary')
# find_key(7)
# find_key(5)


# def iteretItem():
#     Dic={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#     for dicK,dicV in Dic.items():
#         print(dicK,':',dicV)
# iteretItem()


# Num=int(input("enter any number:-"))
# Dic=dict()
# for K in range(1,Num+1):
#     Dic[K]=K*K
# print(Dic)


# Dic=dict()
# for k in range(1,15+1):
#     Dic[k]=k*k
# print(Dic)

     
# def Merge(dict1, dict2):
#     return(dict2.update(dict1))
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}
# print(Merge(dict1, dict2))
# print(dict2)


# Dic={'red':10,'blue':20,'white':30,'green':40,'black':50,'yellow':60}
# for K,Y in Dic.items():
#     print(K,':',Y)


# Dic={'red':10,'blue':20,'white':30,'green':40,'black':50,'yellow':60}
# # print(sum(Dic.values()))
# Sum=0
# for Y in Dic:
#     Sum+=Dic[Y]
# print(Sum)

# Dic={'red':10,'blue':20,'white':30,'green':40,'black':50,'yellow':60}
# multiply=1
# for Y in Dic:
#     multiply*=Dic[Y]
# print(multiply)


# Dic={'red':10,'blue':20,'white':30,'green':40,'black':50,'yellow':60}
# if 'red' in Dic:
#     del Dic['red']
# print(Dic)


# Key={1,2,3,4,5,6,7,8,9,10}
# Value={"rahul","ranu","shona","kittu"}
# print(dict(zip(Key,Value)))


# import mymodule
# mymodule.greeting("Jonathan")

# import platform
# x = platform.system()
# print(x)

# import platform
# x = dir(platform)
# print(x)


# Company = {'GFG':10000, 'Hashd':2292, 'Infy': 200}  
# v = list(Company.values())  
# print("MAx value:",v[v.index(max(v))])
# print("min value:",v[v.index(min(v))])


# Company = {'GFG':10000, 'Hashd':2292, 'Infy': 200}
# for key in sorted(Company):
#     print(key,Company[key])


