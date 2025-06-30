import time

def game():
    print('------------------------------')
    print('Welcome to the Lost Artifact!')
    print('------------------------------')

    name = input("What is the name of your character?")

    time.sleep(3)
    print('\n--- LOCATION 1: Entrance of the Cave ---')
    print('You are searching for an ancient artifact that was passed down from your family, being guided by your ancestors.')
    print('You come apon a cave, seemingly calling for you. Instead of giving off a creepy vibe, it seems more welcoming.')

    choice = print_choice('\n  Do you: \n  1) Enter the cave. \n  2) Ignore the cave.')
    print(choice)
    
    if choice == 1:
        print('\n--- LOCATION 2: The Cave ---')
        print('You wander into the cave and can make out a silhouette, seemingly not dangerous.')

        choice = print_choice('\n Will you: \n  1) Approach them. \n  2) Run away.')

        if choice == 1:
            print('You approuch the figure, and when it notices you, it comes towards you.')
            print(f'\n"Hello, {name}," they say, and you can make out a warm smile. Your grandma. "I am here to give you a quest. I am aware you are already on one, but this should help you.')
            print(f'\n"There is a lost city you need to find," she continues. "To complete this quest, you must find a.. sidekick, as you call them these days."')

            choice = print_choice("\n  Will you say: \n  1) 'I'll do it.' \n  2) 'No thank you, I already have enough to deal with.' \n  3) 'I'll do it, but no sidekick.'")
            
            if choice == 1:
                print('"Good," she says, and then points to your compass. "This compass is magical. When you click the button on top, it grants you a wish. It only has 3 uses, so use it wisely."')
                print('"I have to leave now. Good luck. I belive it you," she smiles, and then disapears.')

            if choice == 2:
                print('"Very well," she says. "Good luck on your journey."')

            if choice == 3:
                print('"If you are sure you want to do that, then you may," she says. "Goodbye, and good luck. I belive in you."')

    elif choice == 2:
        print('\n--- LOCATION 3: The Forest ---')
        print('You explore the forest beyond the cave and soon get tired, so you make a camp and go to sleep.')
        print('')
        print('-THE NEXT DAY-')
        print('')
        print('The next day, you wake up to see a spirit wandering around. When it notices you watching them, they approach toward you.')
        print(f'\n"Hello, {name}," they say, and you can make out a warm smile. Your grandma. "I have come here to give you a quest. I am aware you are already on one, but this should help you.')
        print(f'\n"There is a lost city you need to find," she continues. "To complete this quest, you must find a.. sidekick, as you call them these days."')

        choice = print_choice("\n  Will you say: \n  1) 'I'll do it.' \n  2) 'No thank you, I already have enough to deal with.' \n  3) 'I'll do it, but no sidekick.'")

        if choice == 1:
            print('"Good," she says, and then points to your compass. "This compass is magical. When you click the button on top, it grants you a wish. It only has 3 uses, so use it wisely."')
            print('"I have to leave now. Good luck. I belive it you," she smiles, and then disapears.')
        if choice == 2:
            print('"Very well," she says. "Good luck on your journey."')

        if choice == 3:
            print('"If you are sure you want to do that, then you may," she says. "Goodbye, and good luck. I belive in you."')

inventory = {
    'torch': 0,
    'compass (uses)': 3,
    'sword': 1
}

def print_inventory():
    global inventory
    print()
    print('--------------------')
    for (k, v) in inventory.items():
        print(f'{k}: {v}')
    print('--------------------')

def print_choice(choice):
    user_input = 'i'
    while (user_input == 'i'):
        user_input = input(f"{choice} \n  Choose: [1/2/3] \n  Enter 'i' to see your inventory ") # '\n' means 'new line'
        if (user_input == 'i'):
            print_inventory()
    if user_input in ['1', 'one', 'ONE', 'One']:
        return 1
    elif user_input in ['2', 'two', 'TWO', 'Two']:
        return 2
    elif user_input in ['3', 'three', 'THREE', 'Three']:
        return 3
    else:
        print('Please enter a valid answer [1/2/3].')

game()

def main():
    alive = True

    while alive:
        resume = game()

if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------------#

# Welcome to the Lost City Adventure!
'''Location 1'''
# You are seraching for an ancient artifact that was passed down from your family, being guiding by your ancenstors.
# You come apon a cave, seemingly calling fo ryou. Instead of giving off a creepy vibe, it seems more welcoming.
'''Question 1'''
# Do you enter the cave?
    # yes = You enter the cave.
    # no = You avoid the cave.
'''Location One (no)'''
# You explore the forest beyond the cave and soon get tired, so you make a camp and go to sleep. The next day, you wake up to see a spirit wandering around.
# When it notices you watching them, they approach toward you.
# 'Hello,' they say, and you can make out a warm smile. Your grandma. 'I have come here to give you a quest. I am aware you are already on one,
# but this should help you.

'''Location Two (yes)'''
# You wander into the cave and can make out a silhouette, seemingly not dangerous.