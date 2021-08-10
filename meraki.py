# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:'organisation'}
# result = person['age'] 
# x = person.get("gender")
# print(person[4])
# print(x)
# print(result)


# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:{
#         'organisation':'navgurukul','place':'dharamsala'
#         }
#     }
# print(person['gender'])
# print(person[4])
# result = person[4]['place']
# print(result) 


# dic= {
#     'Name': 'RAM', 
#     'Age': 17,
#     }
# dic['ORGANIZATION'] = "NAV GURUKUL"
# dic['place'] = 'dharamsala'
# print(dic) 


# dic= {
#    'Name': 'RAM',
#    'Age': 17,
#     }
# dic['student']={
#        'id':22, 
#        'place':'dharamsala'
#    }
# print(dic) 


# car ={
#     "brand":  "ford",
#     "model":  "mustang",
#     "year":  1964
# }
# if "model" in car:
#     print("Yes, 'model' is one of the keys in the car dictionary.")
# else:
#     print("No, 'model' key dictionary mai nahi hai.") 


# classes ={
#     "room1":  "6th",
#     "room2":  "7th",
#     "room3":  "8th"
#         }
# mydict=classes.copy()
# print(mydict) 


# new={ }
# Dic={ }
# Range=int(input("Enter rang of the dictionary=:"))
# i=1
# while i<=Range:
#     Name=input("enter name=:")
#     Marks=int(input("Enter number=:"))
#     new.update({Name:Marks})
#     Dic.update(new)
#     i+=1
# print(Dic)

# new={ }
# Dic={ }
# Range=int(input("Enter rang of the dictionary=:"))
# i=1
# while i<=Range:
#     # Name=input("enter name=:")
#     Marks=int(input("Enter number=:"))
#     square=Marks**2
#     new.update({Marks:square})
#     Dic.update(new)
#     i+=1
# print(Dic)

# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
# print(x)


# my_dict = {
#     'a':50, 
#     'b':58, 
#     'c':56,
#     'd':40, 
#     'e':100, 
#     'f':20
#     }
# i=0
# Max=0
# S_max=0
# third_max=0
# while i<len(my_dict):
#     if my_dict.values()>Max:
#         S_max=Max
#         Max=my_dict.values()
#     if S_max<my_dict.values() and Max>my_dict.values():
#         S_max=my_dict.values()
#     if my_dict.values()>third_max:
#         if third_max<S_max and S_max>Max:
#             third_max=S_max 
#     i+=1
# print(Max)
# print(S_max)
# print(third_max)

# a = {(1,2):1,(2,3):2}
# print(a[1,2]) 

# a = {'a':1,'b':2,'c':3}
# print (a['a','b']) 


# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')
# print (len(fruit))
# print(fruit) 


# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age
# print (len(Details["Student"])) 
 