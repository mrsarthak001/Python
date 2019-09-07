num=[1,2,3,4] #list , tuple , string are iterables
squ=map(lambda a:a**2,num)  # Iterator
#=============================
print(next(squ))
print(next(squ))
print(next(squ))
print(next(squ))
#=================================
# num list is not iterator
# print(next(num))
#====================================

# step 1 call iter function
# iter(num) ----> iterator
# next(iter(num))

 #============================

# num_iter=iter(num)
# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter))

