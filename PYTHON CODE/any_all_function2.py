def my_sum(*args):
    total=0
    for num in args:
        total += num
    return total
print(my_sum(1,2,3,4,5,6,6.8))


#print(my_sum(1,2,3,4,5,6,6.8,['deepak']))

# Solution

# def my_sum1(*args):
#     if all([(type(arg) == int or type(arg) == float) for arg in args]):
#        total=0
#        for num in args:
#           total += num
#        return total
#
#     return "wrong input"
# print(my_sum1(1,2,3,4,5,6,6.8,['deepak']))