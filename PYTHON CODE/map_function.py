# numbers=[2,3,4,5,6,7]
# def square(a):
#     return a**2
# print(map(square,numbers))

#==================================

numbers=[2,3,4,5,6,7]
def square(a):
    return a**2
squ=list(map(square,numbers))
print(squ)

# With the Help of lambda

numbers=[2,3,4,5,6,7]
squ=list(map(lambda a:a**2,numbers))
print(squ)

#list comprihension

new_squ=[i**2 for i in numbers]
print(new_squ)

#simple
new_list=[]
for num in numbers:
    new_list.append(square(num))
print(new_list)

