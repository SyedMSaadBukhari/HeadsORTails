print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
option1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right"\n').lower()

if option1 == "right":
    print("You fell into a hole. GAME OVER")
elif option1 == "left":
    option2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for the boat. Type"SWIM" to swim across.\n').lower()
    if option2 == "swim":
        print("You got attacked by an angry trout. GAME OVER")
    elif option2 == "wait":
        option3 = input("You arrive at the island unharmed. There is a house with 3 doors. Choose a door. Red, Blue, or Yellow\n").lower()
        if option3 == "red" or option3 == "blue":
            print("It's a room full of fire. GAME OVER")
        elif option3 == "yellow":
            print("YOU WIN. Treasure is yours")
        else:
            print("Door does not exist.")
    else:
        print("That's not an option.")
else:
    print("Cannot go there. NO TREASURE FOR YOU")