"""
Author: Heather Hickman
Date: 3/20/19
Name: hickman_exam3
Summary: Create a dictionary that keeps names and email addresses as key-value pairs.
            Allow user to choose from a menu to look up, add new, change, delete, or
            display key-value pairs in said dictionary, or exit the program.

1. CONSTANTS
    MENU_OPTION_LOOKUP      = 1
    MENU_OPTION_ADD         = 2
    MENU_OPTION_CHANGE      = 3
    MENU_OPTION_DELETE      = 4
    MENU_OPTION_DISPLAY     = 5
    MENU_OPTION_EXIT        = 6

2. VARIABLES
    a. nameEmailDictionary = empty dictionary to add key/values to
    b. menuSelection = for the user to choose their menu selection
    c. name = persons name / key
    d. email = persons email / value

3. INPUTS
    a. menuSelection - for the user to select a menu option

4. PROCESSING
    a. Create a list of global constants to use as menu items.
    b. Menu function should print the full menu for the user to
        see and ask for the users input.
    c. Define the functions for each menu option: lookup, add new,
        change, delete, display, and quit.
    d. The main function should create the dictionary (empty until user adds key-value pairs).
        Use a while loop to loop through the menu until the user chooses to quit.
        Process the menu choices using if/elif.

5. OUTPUT
    a. display the menu for the user.
        1. Look up email address.
        2. Add a new name and email address.
        3. Change an existing email address.
        4. Delete an existing name and email address.
        5. Display a list of all names and email addresses.
        6. Exit the program.

"""
# global constants
MENU_OPTION_LOOKUP  = 1
MENU_OPTION_ADD     = 2
MENU_OPTION_CHANGE  = 3
MENU_OPTION_DELETE  = 4
MENU_OPTION_DISPLAY = 5
MENU_OPTION_EXIT    = 6

def getMenuSelection():
    # create the menu for the user to choose from
    print('-' * 50)
    print("Name & E-Mail Address Menu")
    print('-' * 50)
    print("1. Look up a name.")
    print("2. Add a name/email address.")
    print("3. Change a name/email address.")
    print("4. Delete a name/email address.")
    print("5. Print name and email address list.")
    print("6. Exit the program.")

    # get a menu selection from the user
    print()
    menuSelection = int(input("Please enter a menu selection:\t"))

    # while validation loops
    while menuSelection < MENU_OPTION_LOOKUP or menuSelection > MENU_OPTION_EXIT:
        menuSelection = int(input("Please enter an option between 1-6:\t"))

    # user entered a valid menu option, return it to calling program
    return menuSelection


def nameEmailLookup(nameEmailDictionary):
    # get the name to look up from the user
    name = input("Please enter a name to lookup:\t")

    # validate that the name is in the dictionary. if so, print out the associated email address.
    # if not, tell the user that the person was not found.
    if name in nameEmailDictionary:
        print(name,"'s email address is", nameEmailDictionary[name])
    else:
        print(name, "is not in the dictionary.")


def nameEmailAdd(nameEmailDictionary):
    # the user should input a name and email to be added to the dictionary
    name = input("Enter persons name:\t")
    email = input("Enter persons email:\t")

    # make sure the person is not already in the dictionary. if not, add them.
    # if so, tell the user the person is already in the dictionary.
    if name not in nameEmailDictionary:
        nameEmailDictionary[name] = email
    else:
        print(name, "is already in the dictionary.")


def nameEmailChange(nameEmailDictionary):
    # get the persons name to change from the user
    name = input("Enter a name to change:\t")

    # validate the person is in the dictionary
    # if in dictionary, display current email and allow user to input new email
    # if not in dictionary, tell user the person cannot be found
    if name in nameEmailDictionary:
        print(name,"'s current email address is:", nameEmailDictionary[name])
        email = input("Enter the new e-mail address:\t")
        nameEmailDictionary[name] = email
    else:
        print(name, "is not in the dictionary.")


def nameEmailDelete(nameEmailDictionary):
    # get input from user on which person to delete
    name = input("Please enter the persons name:\t")

    # validate the person is in the dictionary, if so, delete
    # if not, tell the user the person is not in the dictionary
    if name in nameEmailDictionary:
        del nameEmailDictionary[name]
    else:
        print(name, "is not in the dictionary.")


def nameEmailPrintList(nameEmailDictionary):
    #print list of people and email addresses that have been added to the dictionary
    print(format("Name", "40"), format("E-Mail Address","12"))
    for name in nameEmailDictionary:
        print(format(name,"40"), format(nameEmailDictionary[name],"12"))


def main():
    # create an empty dictionary to hold the names and email addresses
    nameEmailDictionary = {}

    # initialize a variable to hold users menu choice
    menuOptionSelected = 0

    # loop until user quits
    while menuOptionSelected != MENU_OPTION_EXIT:
        # call the display to get the menu option chosen by the user
        menuOptionSelected = getMenuSelection()

        # process our menu choice
        if menuOptionSelected == MENU_OPTION_LOOKUP:
            nameEmailLookup(nameEmailDictionary)
        elif menuOptionSelected == MENU_OPTION_ADD:
            nameEmailAdd(nameEmailDictionary)
        elif menuOptionSelected == MENU_OPTION_CHANGE:
            nameEmailChange(nameEmailDictionary)
        elif menuOptionSelected == MENU_OPTION_DELETE:
            nameEmailDelete(nameEmailDictionary)
        elif menuOptionSelected == MENU_OPTION_DISPLAY:
            nameEmailPrintList(nameEmailDictionary)

    # exit the program
    print("Thank you for using this program!")

main()