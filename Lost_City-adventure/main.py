import time

def game():
    print('------------------------------')
    print('Welcome to the Lost Artifact!')
    print('------------------------------')

    name = input("What is the name of your character?")

    time.sleep(3)

    print('You are searching for an ancient artifact that was passed down from your family, being guided by your ancestors.')
    print('You come apon a cave, seemingly calling for you. Instead of giving off a creepy vibe, it seems more welcoming.')

    choice = print_choice('Do you enter the cave?')
    print(choice)
    
    if choice == True:
        print('You wander into the cave and can make out a silhouette, seemingly not dangerous.')

    elif choice == False:
        print('You explore the forest beyond the cave and soon get tired, so you make a camp and go to sleep.')
        print('')
        print('-THE NEXT DAY-')
        print('')
        print('The next day, you wake up to see a spirit wandering around. When it notices you watching them, they approach toward you.')
        print(f'"Hello, {name}," they say, and you can make out a warm smile. Your grandma. "I have come here to give you a quest. I am aware you are already on one, but this should help you.')
        print(f'"There is a lost city you need to find," she continues. "To complete this quest, you must find a.. sidekick, as you call them these days."')

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
        user_input = input(f"{choice} [yes/no] \nEnter 'i' to see your inventory ") # '\n' means 'new line'
        if (user_input == 'i'):
            print_inventory()
    if user_input in ['Y', 'y', 'yes', 'YES', 'yES', 'yeS', 'Yes', 'yEs', 'YeS', 'YEs', 'ye', 'YE', 'yE', 'Ye']:
        return True
    return False

game()


# --------------------------------------------------------------------------------#

# Welcome to the Lost City Adventure!
'''Location One'''
# You are seraching for an ancient artifact that was passed down from your family, being guiding by your ancenstors.
# You come apon a cave, seemingly calling fo ryou. Instead of giving off a creepy vibe, it seems more welcoming.
'''Question One'''
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