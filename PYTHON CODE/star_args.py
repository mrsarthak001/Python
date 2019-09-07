def all_total(*args):
    total=0
    for num in args:
        total += num
    return total

print(all_total(1,2,3,4,5,7,8))
#==================================

def multiply(*args):
    total=1
    for num in args:
        total *= num
    return total

print(multiply(1,2,3,4,5,7,8))