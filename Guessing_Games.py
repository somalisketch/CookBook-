import random

print("welcome to Guessing Game")
Number_OF_Guesses = 3
player_wins = False
correct_unswer = random.randint(1, 10)
while Number_OF_Guesses > 0:
    print("Guess the Number")

    guesing_number = input()
    guesing_number = int(guesing_number)
    if guesing_number == correct_unswer:
        print("you're Correct, You Got Me ")
        player_wins = True
        break
    elif guesing_number > 10:
        print("ERROR! #No:01; Please Don't Type More than 10")
    elif correct_unswer < guesing_number:
        print("Sorry Your Number Was Too High")
        #print("the Hidden Number is : " + str(correct_unswer))
    elif correct_unswer > guesing_number:
        print("Sorry Your Number Was Too Low")
        #print("the Hidden Number is :" + str(correct_unswer))

    Number_OF_Guesses = Number_OF_Guesses - 1
if player_wins == True:
    print("YOU WON!")
else:
    print("")
    print("")
    print("YOU LOST, UNLUCKY BITCh")

