#    [1st question]
# a = {(1,2):1,(2,3):2}
# print(a[1,2]) 

#     #  [2nd question]
# a = {'a':1,'b':2,'c':3}
# print (a['a','b']) 

#     # [3rd question]
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

#     # [4th question]
# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age
# print (len(Details["Student"])) 
 

    # [5th question]
my_dict = {}
my_dict[(1,2,4)] = 8
my_dict[(4,2,1)] = 10
my_dict[(1,2)] = 12
sum = 0
for k in my_dict:
    sum += my_dict[k]
print (sum)
print(my_dict) 

    # [6th question]
# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print (len(crates['box'])) 


# rec = {
# "Name" : "Python", 
# "Age":"20",
# "Addr" : "NJ", 
# "Country" :"USA"
# }
# id1 = id(rec)
# del rec
# rec = {
#     "Name" : "Python", 
#     "Age":"20", 
#     "Addr" : "NJ", 
#     "Country" : "USA"
#     }
# id2 = id(rec)
# print(id1 == id2)


# details={
#     "name":"Shanti",
#     "age":12,
#     "email":"shanti@navgurukul.org",
#     }


# print(details["name"])
# print(details["email"])
# print(details["age"])


# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():    
#     sum=sum+i
# print(sum) 


# c=dict()
# for i in range(1,16):
#     s=i**2
#     c.update({i:s})
# print(c)  



# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
#     c={**s,**a}
# print(c) 


# List=[
#      {"first":1}, 
#      {"second": 2}, 
#      {"third": 1}, 
#      {"four": 5}, 
#      {"five":5}, 
#      {"six":9},
#      {"seven":7}
# ] 
# New_List=[]
# for x in List:
    
#     New_List.append(x)
    # if 
    # print(x)

    # for y in List.values():
    #     if y not in New_List:
    #         print(x)
# empty=[]
# for i in List:
#     for j in List.values():
#         if j not in empty:
#             empty.append(j)
#     print(empty)


