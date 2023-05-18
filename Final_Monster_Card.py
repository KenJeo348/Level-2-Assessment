"""Final version of the Monster Card program
Assembled with all the updated versions of the components
that have gone through testing and trialling.
This is a program that allows the user to add their own
monster cards or modify the existing monster cards.

Created by Kenny Jeong
16/05/2023
"""

import easygui as eg


# Function displaying main menu.
def main_menu(cards_roll_):
    # Display existing cards at the start of the program
    output_cards(cards_roll_)
    # Continuous loop of the main menu until the user chooses to exit.
    while True:
        # Find out what the user wants to do in the main menu.
        menu_choice = eg.buttonbox("Welcome to Monster Cards!\nPlease choose "
                                   "from below:", "Main Menu",
                                   choices=["Add Card",
                                            "Delete Card",
                                            "Find Card",
                                            "Output Cards",
                                            "Exit System"])
        # Depending on what the user chooses, proceed to the ~
        # ~ function/component that corresponds to their choice.
        if menu_choice == "Add Card":
            add_card(cards_roll_)
        elif menu_choice == "Delete Card":
            delete_card(cards_roll_)
        elif menu_choice == "Find Card":
            find_card(cards_roll_)
        elif menu_choice == "Output Cards":
            output_cards(cards_roll_)
        # If the user chooses to exit the system
        elif menu_choice == "Exit System":
            # Double check if the user really wants to exit.
            exit_system = eg.buttonbox("Would you like to exit the program:",
                                       "Exit system", choices=["Yes", "No"])
            # Show a farewell message and exit the system of user confirms.
            if exit_system == "Yes":
                eg.msgbox("Thank you for using our program!", "Farewell")
            break


# Function to add a new monster card to the dictionary.
def add_card(card_roster):

    # Continuous loop that asks the details of the card.
    # This loop repeats until the user chooses to keep the details of the ~
    # ~ card from the keep/change component.
    while True:
        # Ask for name of the monster for the card.
        monster_name = eg.enterbox("Name of Monster:", "Add Card")
        # If the user didn't answer anything or pressed cancel
        if monster_name is None:
            # Set the name as 'Name Not Entered'
            monster_name = "Name Not Entered"

        # Enter the stats (Strength, Speed, Stealth, Cunning) for the monster
        monster_strength = eg.integerbox("Monster Strength level:", "Add Card",
                                         lowerbound=1, upperbound=25)
        monster_speed = eg.integerbox("Monster Speed level:", "Add Card",
                                      lowerbound=1, upperbound=25)
        monster_stealth = eg.integerbox("Monster Stealth level", "Add Card",
                                        lowerbound=1, upperbound=25)
        monster_cunning = eg.integerbox("Monster Cunning level", "Add Card",
                                        lowerbound=1, upperbound=25)

        # Assign the stats entered to the monster, and add to a dictionary.
        card_roster[monster_name] = {"Strength": monster_strength,
                                     "Speed": monster_speed,
                                     "Stealth": monster_stealth,
                                     "Cunning": monster_cunning}
        # For each stat for the monster
        for stat in card_roster[monster_name].keys():
            # If user didn't answer anything or pressed cancel for the stats
            if card_roster[monster_name][stat] is None:
                # Give the stat a value of 0
                card_roster[monster_name][stat] = 0

        # Proceed to the 'keep_change_card' function.
        returned_keep_change = keep_change_card(card_roster, monster_name)

        # If the 'keep_change_card' function returns 'Keep'
        if returned_keep_change == "Keep":
            # Break the loop and return to main menu.
            break


# A function that displays the details of the card and allows user to change it
def keep_change_card(card_roster_, monster_name_):
    card_information = ""

    # Separating each stat of the monster for a cleaner output.
    for details in card_roster_[monster_name_]:
        monster_details = f"{details}: " \
                          f"{card_roster_[monster_name_][details]}\n"
        card_information += monster_details

    # Display the details of the card, and ask if user wants to keep or change
    check_monster_information = eg.buttonbox(f"Monster: Information\n"
                                             f"Monster Name: {monster_name_}\n"
                                             f"{card_information}",
                                             "Check Monster Information",
                                             choices=["Keep", "Change"])
    # Return 'Keep' or 'Change' depending on their choice.
    if check_monster_information == "Change":
        # Delete existing details, so that user can enter new details
        del card_roster_[monster_name_]
        return "Change"
    elif check_monster_information == "Keep":
        return "Keep"


# A function that allows the user to choose a function and then delete it
def delete_card(card_roster):
    # Make a list and store the names of all the existing monster cards
    card_names = []
    for names in card_roster.keys():
        card_names.append(names)
    # Use an easygui choice box to let the user choose a monster
    card_to_delete = eg.choicebox("Name of monster you want to delete:",
                                  "Delete Card", choices=card_names)
    # If the user presses 'Cancel' return to the main menu function.
    if card_to_delete is None:
        return
    # Remove the card that was selected by the user from the dictionary
    del card_roster[card_to_delete]
    eg.msgbox(f"'{card_to_delete}' has been deleted", "Card Deleted")


# A function where the user can find a card and choose to keep or change the
# details of that card.
def find_card(card_roster):
    # Make a list and store the names of all the existing monster cards
    card_names = []
    for names in card_roster.keys():
        card_names.append(names)
    # Use an easygui choice box to let the user choose a monster
    wanted_card = eg.choicebox("Name of monster you are looking for:",
                               "Find Card", choices=card_names)
    # If the user presses 'Cancel' return to the main menu function.
    if wanted_card is None:
        return
    # Proceed to the 'keep_change_card' function.
    returned_keep_change = keep_change_card(card_roster, wanted_card)

    # If the 'keep_change_card' function returns 'Change'
    # Proceed to the 'add_card' function to allow user to enter new details.
    if returned_keep_change == "Change":
        add_card(card_roster)


# A function that displays all the monsters details existing in the dictionary
def output_cards(card_roster):
    final_output = ""

    # Storing all names of monsters for the output variable
    for monster_name in card_roster:
        card_info = f"---------------------{monster_name.upper()}-----------" \
                    f"----------\n"
        # Resetting total stat points to 0 for each monster
        total_stat_points = 0

        # Storing stat details for each monster in the output variable
        for key in card_roster[monster_name]:
            card_info += f"{key}:{card_roster[monster_name][key]}, "
            total_stat_points += card_roster[monster_name][key]
        # Variable containing string of final output
        final_output += f"{card_info}\n" \
                        f"Total Stat: {total_stat_points}\n\n"
    # Final output (all monster details) displayed using easygui
    eg.msgbox(final_output, "Title")


# Main Routine

# Dictionary containing the pre-existing monster cards
cards_roll = {
    "Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
    "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
    "Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
    "Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
    "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
    "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
    "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
    "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2},
}

main_menu(cards_roll)
