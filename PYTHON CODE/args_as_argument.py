def multiply(*args):
    total=1
    for num in args:
        total *= num
    return total
list=[2,3,4,5,7,8]

print(multiply(*list))
print(multiply(*list)) #  * will unpack the list