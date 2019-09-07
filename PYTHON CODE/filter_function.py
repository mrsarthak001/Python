def is_even(a):
    return a%2==0
number=[1,2,3,4,5,6,7,8,9,11,23,55,66,]

new=list(filter(is_even,number))

#new=tuple(filter(lambda a:a%2==0,number))

print(tuple(filter(is_even,number)))

# list comprehension
new_list=[i for i in number if i%2==0]
print(new_list)