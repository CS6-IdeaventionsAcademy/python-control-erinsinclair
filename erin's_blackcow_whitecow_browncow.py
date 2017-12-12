#Erin J. Sinclair
#111417
#Brown Cow, White Cow, Black Cow
#Try to beat the other cow!

import random 

print ("""Welcome to Brown Cow, White Cow, Black Cow!
        it is a simple game -- White Cow beats Brown Cow,
        but Black Cow beats White Cow. And Brown Cow beats
        Black Cow!""")
choices = ["Brown Cow", "White Cow", "Black Cow"]

computer_choice=choices[random.randint(0,2)]

player_choice=input ("Now, choose either Brown Cow, White Cow, or Black Cow:")
print (computer_choice)

if computer_choice=="Brown Cow":
    if player_choice=="White Cow":
        print ("You win!")
    else:
        if player_choice=="Black Cow":
            print ("You loose!")
        else:
            if player_choice=="Brown Cow":
                print ("TIE!")
else:
    if computer_choice=="Black Cow":
        if player_choice=="Brown Cow":
            print ("You win!")
        else:
            if player_choice=="White Cow":
                print("You loose!")
            else:
                print ("you loose")
