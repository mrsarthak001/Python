string="my name is Deepak Kumar and i have done my B.Tech"
#print(string.replace(" ","_"))
#print(string.find("is"))
my_pos1= string.find("my")
#my_pos2=string.find("my",my_pos1)
my_pos2=string.find("my",my_pos1+1)
print(my_pos2)
