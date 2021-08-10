d={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
a=sorted(d.items(), key=lambda x: x[1])
b=sorted(d.items(), key=lambda x: x[1],reverse=True)   
print(a)
print(b)
