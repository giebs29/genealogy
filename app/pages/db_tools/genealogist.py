import os
import gui_add_person

# Greeter is a terminal application that greets old friends warmly,
#   and remembers new friends.


### FUNCTIONS ###

def root_menu():
    # Let users know what they can do.
    print("[1] Add person")
    print("[2] List orphans")
    print("[Q] Quit")

    return raw_input("What would you like to do? ")


### MAIN PROGRAM ###

choice = ''
os.system('clear')
while choice != 'q':

    choice = root_menu()

    # Respond to the user's choice.
    if choice == '1':
        gui_add_person.add_person()
    elif choice == '2':
        list_orphans()
    elif choice.upper() == 'Q':
        os.system('clear')
    else:
        print("\nI didn't understand that choice.\n")
