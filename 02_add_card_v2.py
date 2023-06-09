"""Component 2 (Add Combo)
Based on 02_add_card_v1
Added boundaries to the integers
so that answer is between 1-25.
"""


import easygui as eg


def main_menu(cards_roll_):
    while True:
        menu_choice = eg.buttonbox("Welcome to Monster Cards!\nPlease choose "
                                   "from below:", "Main Menu",
                                   choices=["Add Card",
                                            "Delete Card",
                                            "Find Card",
                                            "Output Cards",
                                            "Exit System"])
        if menu_choice == "Add Card":
            add_card(cards_roll_)

        elif menu_choice == "Delete Card":
            print("Proceed to 'Delete Card' function/component.")

        elif menu_choice == "Find Card":
            print("Proceed to 'Find Card' function/component.")

        elif menu_choice == "Output Cards":
            print("Proceed to 'Output Cards' function/component.")

        elif menu_choice == "Exit System":
            print("Proceed to 'Exit System' function/component.")
            break


def add_card(cards_roster):
    monster_name = eg.enterbox("Name of Monster:", "Add Card")
    cards_roster[monster_name] = {}

    monster_strength = eg.integerbox("Monster Strength level:", "Add Card"
                                     , lowerbound=1, upperbound=25)
    cards_roster[monster_name]["Strength"] = monster_strength

    monster_speed = eg.integerbox("Monster Speed level:", "Add Card"
                                  , lowerbound=1, upperbound=25)
    cards_roster[monster_name]["Speed"] = monster_speed

    monster_stealth = eg.integerbox("Monster Stealth level", "Add Card"
                                    , lowerbound=1, upperbound=25)
    cards_roster[monster_name]["Stealth"] = monster_stealth

    monster_cunning = eg.integerbox("Monster Cunning level", "Add Card"
                                    , lowerbound=1, upperbound=25)
    cards_roster[monster_name]["Cunning"] = monster_cunning


# Main Routine

cards_roll = {
    "Stoneling":
        {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
    "Vexscream":
        {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
    "Dawnmirage":
        {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
    "Blazegolem":
        {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
    "Websnake":
        {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
    "Moldvine":
        {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
    "Vortexwing":
        {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "Rotthing":
        {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "Froststep":
        {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
    "Wispghoul":
        {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2},
}

main_menu(cards_roll)
