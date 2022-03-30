print("Welcome to adventure game !!")
#asking user their name
name = input("What is your name ?\n ")
#asking user their age
age = int(input("What is your age?\n "))
#printing name and age
print("Hey there", name, "you are", age, "years old.")
if age >= 21:  #if age in 21+ then ask question
    print("You can play the game! ")

    #asking user if they want to play
    want_to_play = input("Do you want to play?(yes/no) ").lower()

    #if user says yes then start the game
    if want_to_play == "yes":
        print("Let's start the game")
        #if user says something else then print answer
        #Assign health
        health = 10
        print("You are starting game with", health, "health")

        #user selects left or right
        left_right = input("Make a choice - left or right? ").lower()
        #if user selects left then carry on
        if left_right == "left":
            #correct choice by user and reached lake
            answer = input(
                "Good choice!! You are now at lake. Do you wanna swim across or go around it ? (Select across or around) "
            )
            #if user selects around
            if answer == "around":
                print(
                    "Good choice! You went around and reached other side of the lake."
                )
        #if user select across
            elif answer == "across":
                print("You are injured by fishes and lost half lives")
                #lost health
                health -= 5
                print("You have", health, "health left")

                #user meets person
            answer = input("Select red or blue color. ").lower()

            #user selects red and lost
            if answer == "red":
                print("You selected wrong color and you lost 5 health")
                #lost health
                health -= 5
                if health == 0:
                    print("You lost!")
                    exit()
                else:
                    print("You have", health, "health left. ")

            #user selects blue and moves next step
            elif answer == "blue":
                #user selects vehicle
                print("Good choice! You are keeping up ")
            answer = input("Select from car or motorcycle. ").lower()
            #user select car
            if answer == "car":
                print("You reach home and you survive. You win!!")
                #user select motorcycle
            elif answer == "motorcycle":
                print("You got into accident. You lost.")

        #if user selects nothing
            else:
                print("You lost")

        #if user select right then loose
        else:
            print("You choose wrong path and you lost")

    else:
        print("You can comeback later")

#if user in under 21 then they can't play
else:
    print("You are not old enough to play the game! ")
