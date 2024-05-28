#This is the code for a stealth mission game. 
#You are playing as the thief and working toward stealing a prized artifact.

player = 0
guard = 0

player_win = 25
guard_win = 20

print("~~A THIEF IN THE NIGHT~~")
print("You are a theif trying to break into a musuem and steal an artifact that used to belong to your great, great, great, great, great, grandfather. It was donated to the musuem by your crazy uncle who's trying to use the tax deduction from the donation to avoid paying taxes. After staking out the location, you know there's going to be one oblivious guard, and the artifact is under a security mechanism that unlocks about the same time every night. Don't get caught!")
print("~~RULES~~")
print("To select your answer, please enter the number associated with the option.")

while True:
    try:
        print("~SCENARIO 1~")
        situation_one = int(input("""You arrive in the museum through the ceiling and land on the ground. You see the artifact you are looking for at the end of the hall, but you hear the nightguard coming. You have a few options of how you can advance toward the artifact:
1) Walk down the corridor
2) Hide behind the nearby exhibit
3) Sneak in the shadows
How will you proceed? Type your answer.\n"""))

        if situation_one in [1, 2, 3]:
            if situation_one == 1: 
                player += 4
                guard += 2
            elif situation_one == 2:
                player += 0
            elif situation_one == 3:
                player += 2
            break #This is used to exit the loop if a valid choice was made
        else:
            print("INVALID INPUT! Please enter 1, 2, or 3.")
    except ValueError:
        print("Please choose one of the mentioned numbers above")

while True:
    try:
        print("SCENARIO 2")
        situation_two = int(input("""The guard finally walks into the cooridor and starts doing his routine rounds. He has not seen you yet. You have a few options of how you can advance toward the artifact:
1) Walk down the corridor
2) Hide behind the nearby exhibit
3) Sneak in the shadows
How will you proceed? Type your answer.\n"""))  

        if situation_two in [1, 2, 3]:
            if situation_two == 1: 
                player += 4
                guard += 4
            elif situation_one == 2 and situation_two == 2:
                player += 0
                guard += 3
            elif situation_two == 2:
                player += 0
            elif situation_two == 3:
                player += 2
                guard += 1
            break #This is used to exit the loop if a valid choice was made
        else:
            print("INVALID INPUT! Please enter 1, 2, or 3.")
    except ValueError:
        print("Please choose one of the mentioned numbers above")

while True:
    try:
        print("SCENARIO 3")
        situation_three = int(input("""The guard is making his way toward the artifact, slowly but surely cheking all the exhibits along the way. You have a few options of how you can advance toward the artifact:
1) Walk down the corridor
2) Hide behind the nearby exhibit
3) Sneak in the shadows
How will you proceed? Type your answer.\n"""))  

        if situation_three in [1, 2, 3]:
            if situation_two == 1 and situation_three == 1:
                player += 5
                guard += 8
            elif situation_three == 1: 
                player += 4
                guard += 4
            elif situation_one == 2 and situation_two == 2 and situation_three == 2:
                player += 0
                guard += 5
            elif situation_three == 2:
                player += 0
            elif situation_three == 3:
                player += 2
                guard += 1
            break #This is used to exit the loop if a valid choice was made
        else:
            print("INVALID INPUT! Please enter 1, 2, or 3.")
    except ValueError:
        print("Please choose one of the mentioned numbers above")

while True:
    try:
        print("SCENARIO 4")
        situation_four = int(input("""You watch as the guard stops and admires some of the exhibits. He seems to be distracted. You have a few options of how you can advance toward the artifact:
1) Walk down the corridor
2) Hide behind the nearby exhibit
3) Sneak in the shadows
How will you proceed? Type your answer.\n"""))  

        if situation_four in [1, 2, 3]:
            if situation_two == 1 and situation_three == 1 and situation_four == 1:
                player += 5
            elif situation_four == 1: 
                player += 4
            elif situation_one == 2 and situation_two == 2 and situation_three == 2 and situation_four == 2:
                player += 0
                guard += 100
            elif situation_four == 2:
                player += 0
            elif situation_four == 3:
                player += 1
            break #This is used to exit the loop if a valid choice was made
        else:
            print("INVALID INPUT! Please enter 1, 2, or 3.")
    except ValueError:
        print("Please choose one of the mentioned numbers above")

#This last statement is used to deter the user from hiding behind the nearby exhibit too long or walking in plain sight for too long
if player == 0 and guard > guard_win:
    print("Guard says: If you stay here long enough, you'll become one of the exhibits! LOL Get Bent Loser!")
    quit()
elif guard >= 100:
    print("Guard says: Halt! You're under arrest for tresspassing.")
    quit()

while True:
    try:
        print("SCENARIO 5")
        situation_five = int(input("""The guard sneezes, knocking over a vase that's nearby. When it shatters, the guard becomes startled and starts looking around frantically. You have a few options of how you can advance toward the artifact:
1) Walk down the corridor
2) Hide behind the nearby exhibit
3) Sneak in the shadows
How will you proceed? Type your answer.\n"""))  

        if situation_five in [1, 2, 3]:
            if situation_two == 1 and situation_three == 1 and situation_four == 1 and situation_five == 1:
                player += 5
                guard += 100
            elif situation_five == 1: 
                player += 4
                guard += 4
            elif situation_two == 2 and situation_three == 2 and situation_four == 2 and situation_five == 2:
                player += 0
                guard += 100
            elif situation_five == 2:
                player += 0
            elif situation_five == 3:
                player += 2
                guard += 4
            break #This is used to exit the loop if a valid choice was made
        else:
            print("INVALID INPUT! Please enter 1, 2, or 3.")
    except ValueError:
        print("Please choose one of the mentioned numbers above")

#This last statement is used to deter the user from hiding behind the nearby exhibit too long or walking in plain sight for too long
if player == 0 and guard > guard_win:
    print("Guard says: If you stay here long enough, you'll become one of the exhibits! LOL Get Bent Loser!")
    quit()
elif guard >= 100:
    print("Guard says: Halt! You're under arrest for tresspassing.")
    quit()

while True:
    try:
        print("Scenario 6")
        situation_six = int(input("""The guard has calmed down. He makes a note over the radio that one of the exhibits has been broken and blames it on a guest who must have done it during visiting hours. You have a few options of how you can advance toward the artifact:
1) Walk down the corridor
2) Hide behind the nearby exhibit
3) Sneak in the shadows
How will you proceed? Type your answer.\n"""))  

        if situation_six in [1, 2, 3]:
            if situation_three == 1 and situation_four == 1 and situation_five == 1 and situation_six == 1:
                player += 5
                guard += 100
            elif situation_six == 1: 
                player += 4
                guard += 4
            elif situation_three == 2 and situation_four == 2 and situation_five == 2 and situation_six == 2:
                player += 0
                guard += 100
            elif situation_six == 2:
                player += 0
            elif situation_six == 3:
                player += 5
                guard += 1
            break #This is used to exit the loop if a valid choice was made
        else:
            print("INVALID INPUT! Please enter 1, 2, or 3.")
    except ValueError:
        print("Please choose one of the mentioned numbers above")

#This last statement is used to deter the user from hiding behind the nearby exhibit too long or walking in plain sight for too long
if player == 0 and guard > guard_win:
    print("Guard says: If you stay here long enough, you'll become one of the exhibits! LOL Get Bent Loser!")
    quit()
elif guard >= 100:
    print("Guard says: Halt! You're under arrest for tresspassing.")
    quit()

while True:
    try:
        print("Scenario 7")
        situation_seven = int(input("""You are one step away from reaching the artifact, and the guard doesn't seem any the wiser. You notice the security mechanism is still active, and you hope that once you reach it, it will be disengaged. You have a few options of how you can advance toward the artifact:
1) Walk down the corridor
2) Hide behind the nearby exhibit
3) Sneak in the shadows
How will you proceed? Type your answer.\n"""))  

        if situation_seven in [1, 2, 3]:
            if situation_four == 1 and situation_five == 1 and situation_six == 1 and situation_seven == 1:
                player += 5
                guard += 100
            elif situation_seven == 1: 
                player += 4
                guard += 4
            elif situation_four == 2 and situation_five == 2 and situation_six == 2 and situation_seven == 2:
                player += 0
                guard += 100
            elif situation_seven == 2:
                player += 0
            elif situation_seven == 3:
                player += 2
                guard += 1
            break #This is used to exit the loop if a valid choice was made
        else:
            print("INVALID INPUT! Please enter 1, 2, or 3.")
    except ValueError:
        print("Please choose one of the mentioned numbers above")

#This last statement is used to deter the user from hiding behind the nearby exhibit too long or walking in plain sight for too long
if player == 0 and guard > guard_win:
    print("Guard says: If you stay here long enough, you'll become one of the exhibits! LOL Get Bent Loser!")
    quit()
elif guard >= 100:
    print("Guard says: Halt! You're under arrest for tresspassing.")
    quit()

while True:
    try:
        print("SCENARIO 8")
        situation_eight = int(input("""The security mechanism has disengaged. You are able to finally get your hands on the artifact. You have a few options of how you can retreive the artifact:
1) Run up to the artifact
2) Hide behind the artifact
3) Sneak up to grab the artifact
How will you proceed? Type your answer.\n"""))  

        if situation_eight in [1, 2, 3]:
            if situation_five == 1 and situation_six == 1 and situation_seven == 1 and situation_eight == 1:
                player += 5
                guard += 100
            elif situation_eight == 1: 
                player += 4
                guard += 6
            elif situation_five == 2 and situation_six == 2 and situation_seven == 2 and situation_eight == 2:
                player += 0
                guard += 100
            elif situation_eight == 2:
                player += 0
            elif situation_eight == 3:
                player += 8
                guard += 3
            break #This is used to exit the loop if a valid choice was made
        else:
            print("INVALID INPUT! Please enter 1, 2, or 3.")
    except ValueError:
        print("Please choose one of the mentioned numbers above")

#This last statement is used to deter the user from hiding behind the nearby exhibit too long or walking in plain sight for too long
if player == 0 and guard > guard_win:
    print("Guard says: If you stay here long enough, you'll become one of the exhibits! LOL Get Bent Loser!")
    quit()
elif guard >= 100:
    print("Guard says: Halt! You're under arrest for tresspassing.")
    quit()

print(player)
print(guard)

if player >= player_win and guard <= guard_win:
    print("Congratulations! You've successfully stolen the artifact.")
elif player >= player_win and guard > guard_win:
    print("Drat! You got to the artifact, but the guard caught you. Better luck next time.")
elif player == 0 and guard > guard_win:
    print("Guard says: If you stay here long enough, you'll become one of the exhibits! LOL Get Bent Loser!")
elif player < player_win and guard > guard_win:
    print("The guard caught you before you could steal the artifact.")
elif player < player_win and guard < guard_win:
    print("You tripped on your way to the artifact, and the security mechanism was able to lock before you got back up. You were able to avoid getting caught, but you will have to try again another night.")
else:
    print("You still need to steal the artifact! Would you like to restart the game?")    
