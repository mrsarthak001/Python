age= input ("Enter your age : ")
age = int(age)


if age==0 or age<0:
    print("You can't Watch:")

elif 0<=age<=3:
    print("Ticket Price : Free")

elif 3<age<=10:
  print("Ticket Price : 150 Rs")
elif 10<age<=20:
  print("Ticket Price : 250 Rs")
else:
    print("Ticket Price : 300 Rs")



#else:
#print("Ticket Price : 300 Rs")