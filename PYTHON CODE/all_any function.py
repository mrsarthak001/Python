num1=[2,4,6,8,10]
num2=[1,2,3,4,5,6,7,8]
#even=[n%2==0 for n in num1]

even=all([n%2==0 for n in num2])
odd=any([n%2==0 for n in num2])

print(even)
print(odd)