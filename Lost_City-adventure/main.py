import time

def game():
    print('------------------------------')
    print('Welcome to the Lost Artifact!')
    print('------------------------------')

    name = input("What is the name of your character?")

    time.sleep(3)

    print('You are searching for an ancient artifact that was passed down from your family. You are being guided by your ancestors.')
    print('You come apon a cave, seemingly calling for you. Instead of giving off a creepy vibe, it seems more welcoming.')

    choice = print_choice('Do you enter the cave?')
    print(choice)

inventory = {
    'torch': 0,
    'compass (uses)': 3,
    'sword': 1,
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
        user_input = input(f"{choice} [yes/no] \n Enter 'i' to see your inventory") # '\n' means 'new line'
        if (user_input == 'i'):
            print_inventory()
    if user_input in ['Y', 'y', 'yes', 'YES', 'yES', 'yeS', 'Yes', 'yEs', 'YeS', 'YEs', 'ye', 'YE', 'yE', 'Ye']:
        return True
    return False