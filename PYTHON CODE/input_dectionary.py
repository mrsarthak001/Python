user={}

name= input("enter your name")
age= input("enter your age")
fev_movie= input("enter your fev movies saperated by ,").split(",")

user['name']=name
user['age']=age
user['fev_movie']=fev_movie

#print(user)
for key,value in user.items():
    print(f"{key} : {value}")