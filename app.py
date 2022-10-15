name = input("Type your name: ")
print("Welcome", name, "to this wonderful adventure!")

answer = input("You are on a crossroads. You can go left or right. Which way would you like to go (left / right)? ")

if answer == "left":
    answer = input(
        "You come to a forest, you can either go around it or go through it (walk / through)? ")

    if answer == "walk":
        print("While you're walking around the forest you step into a trap and get robbed by bandits.")
    elif answer == "through":
        answer = input("You stumble upon a hooded stranger. Are you going to talk or run away (talk / run)? ")
        if answer == "talk":
            print("The stranger is friendly and guides you out of the forest. You win.")
        elif answer == "run":
            print("While running you fall down and lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input(
        "You come to village and stumble upon a tavern. Do you decide to come inside or leave (inside / leave)? ")
    if answer == "inside":
        answer = input("You go in and meet your long lost friend. He offers to go on an adventure with you. Are you going to accept the offer (yes / no)? ")
        if answer == "yes":
            print("The friends gives you gold and a new weapon. You win!")
        elif answer == "no":
            print("The friend is disappointed and bids you farewell. You lose.")
        else:
            print("Not a valid option. You lose.")
    elif answer == "leave":
        answer = input(
            "You get caught by guards and thrown out of the village. You lose.")
    else:
        print("Not a valid option. You lose.")

    print("Thank you for playing", name)