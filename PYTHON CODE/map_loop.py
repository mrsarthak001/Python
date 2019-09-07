#iterable function because we can apply loop on it

names=['deepak','govind','naresh']
def fun(name):
    return name
length=tuple (map(fun,names))
print(length)

# you can only run loop single time on map object
for j in length:
    print(j)
