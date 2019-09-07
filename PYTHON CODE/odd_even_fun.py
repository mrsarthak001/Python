def odd_even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
a = int(input("enter number:"))
#=================================
#def odd_even(num):
   # if num%2==0:
       # return "even"

   # return "odd"
#=================================

print(odd_even(a))

#==============================
#without value passing
def song():
    return "party song"
print(song())
