"""Component 1 (Main Menu)
A main page that the program starts with
Displays multiple choices that the user
can choose from."""


import easygui as eg


menu_choice = eg.buttonbox("Welcome to Monster Cards!\nPlease choose from "
                           "below:", "Main Menu", choices=["Add Card",
                                                           "Delete Card",
                                                           "Find Card",
                                                           "Output Cards",
                                                           "Exit System"])

if menu_choice == "Add Card":
    print("Proceed to 'Add Card' function/component.")

elif menu_choice == "Delete Card":
    print("Proceed to 'Delete Card' function/component.")

elif menu_choice == "Find Card":
    print("Proceed to 'Find Card' function/component.")

elif menu_choice == "Output Cards":
    print("Proceed to 'Output Cards' function/component.")

elif menu_choice == "Exit System":
    print("Proceed to 'Exit System' function/component.")
