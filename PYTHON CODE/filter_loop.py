def is_even(a):
    return a%2==0
number=[1,2,3,4,5,6,7,8,9,11,23,55,66,]

new=(filter(is_even,number))


for i in new:
    print(i)

#===============================

new=tuple(filter(is_even,number))

for i in new:
    print(i)

for j in new:
    print(j)