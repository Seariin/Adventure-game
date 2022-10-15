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
