def big(a,b):
    if a>b:
        return a
    else:
        return b

num1= int(input("enter first number:"))

num2= int(input("enter second number:"))

greater=  big(num1,num2)
print(f"{greater} is greater")

