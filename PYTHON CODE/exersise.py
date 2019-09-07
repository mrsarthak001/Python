name , char = input("enter comma saperated name and charactor: ").split(",")
print(f"length of your name is {len(name)}")
print(f"cherector count :  {name.count(char)}")#case sensitive

#name.lower()
# .count()
#char.lower()

#name.lower().count(char.lower())
print(f"cherector count :  {name.lower().count(char.lower())}")