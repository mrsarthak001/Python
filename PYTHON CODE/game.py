#nested if else

win_number=38
guess=1
guess_number= int(input ("Guess a number between 1 to 100 : "))

game_over= False
while not game_over:
 if guess_number==win_number:
    print(f"you win !!!!!! you guess it in: {guess} th time")
    game_over= True
 else:


    if guess_number < win_number :
        print("Too low")
        guess += 1
        guess_number= int( input("guess again"))

    else:


         print("Too high")
         guess +=1
         guess_number= int( input("guess again"))

