def cf(l1,l2):
    output=[]
    for i in l1:
        if i in l2:
            output.append(i)
    return output
print(cf([1,2,3,6,7,9],[1,3,4,5,7]))



