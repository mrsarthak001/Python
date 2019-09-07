id=['user1','user2','user3']
name=['deepak','govind','naresh']
l_name=['rajput','kumar','verma']
# zip is the iterator
print(list(zip(id,name,l_name)))

# u can't convert it into dictionary bcouz length is 3

#print(dict(zip(id,name,l_name)))
l1=[1, 3, 5, 7]
l2=[2, 4, 6, 8]
print(list(zip(l1,l2)))

# example
exmp=[('abc',1),('xyz',2)]

print(dict(exmp))

