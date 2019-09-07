
def is_even(a):
    if a%2==0:
        return True
    else:
        return False
print(is_even(6))

#==============================

def is_even(a):
    if a%2==0:
        return True
    return False
print(is_even(7))
#=============================
def is_even(a):
    return a%2==0

print(is_even(6))

#==============================
is_even2 = lambda a : a%2==0

print(is_even2(9))
#=============================
#last char
last_char = lambda a: a[-1]
print(last_char('deepak'))



