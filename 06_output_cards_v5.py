"""Component 6 (Output Cards)
Based on 06_output_cards_v1
Added formatting that made output
easier to read and interpret.
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
            delete_card(cards_roll_)
        elif menu_choice == "Find Card":
            find_card(cards_roll_)
        elif menu_choice == "Output Cards":
            output_cards(cards_roll_)
        elif menu_choice == "Exit System":
            print("Proceed to 'Exit System' function/component.")
            break


def add_card(card_roster):

    while True:
        monster_name = eg.enterbox("Name of Monster:", "Add Card")
        monster_strength = eg.integerbox("Monster Strength level:", "Add Card",
                                         lowerbound=1, upperbound=25)
        monster_speed = eg.integerbox("Monster Speed level:", "Add Card",
                                      lowerbound=1, upperbound=25)
        monster_stealth = eg.integerbox("Monster Stealth level", "Add Card",
                                        lowerbound=1, upperbound=25)
        monster_cunning = eg.integerbox("Monster Cunning level", "Add Card",
                                        lowerbound=1, upperbound=25)
        card_roster[monster_name] = {"Strength": monster_strength,
                                     "Speed": monster_speed,
                                     "Stealth": monster_stealth,
                                     "Cunning": monster_cunning}
        returned_keep_change = keep_change_card(card_roster, monster_name)

        if returned_keep_change == "Keep":
            break


def keep_change_card(card_roster_, monster_name_):
    card_information = ""

    for details in card_roster_[monster_name_]:
        monster_details = f"{details}: " \
                          f"{card_roster_[monster_name_][details]}\n"
        card_information += monster_details

    check_monster_information = eg.buttonbox(f"Monster: Information\n"
                                             f"Monster Name: {monster_name_}\n"
                                             f"{card_information}",
                                             "Check Monster Information",
                                             choices=["Keep", "Change"])
    if check_monster_information == "Change":
        del card_roster_[monster_name_]
        return "Change"
    elif check_monster_information == "Keep":
        return "Keep"


def delete_card(card_roster):

    card_names = []
    for names in card_roster.keys():
        card_names.append(names)
    card_to_delete = eg.choicebox("Name of monster you want to delete:",
                                  "Delete Card", choices=card_names)
    del card_roster[card_to_delete]
    eg.msgbox(f"'{card_to_delete}' has been deleted", "Card Deleted")


def find_card(card_roster):
    card_names = []
    for names in card_roster.keys():
        card_names.append(names)
    wanted_card = eg.choicebox("Name of monster you are looking for:",
                               "Find Card", choices=card_names)
    returned_keep_change = keep_change_card(card_roster, wanted_card)

    if returned_keep_change == "Change":
        add_card(card_roster)


def output_cards(card_roster):
    format_symbol = "="
    format_sides = format_symbol * 3

    for monster_name in card_roster:

        print(f"-----------------[{monster_name}]-----------------")

        total_stat_points = 0
        output_stats = ""

        for key in card_roster[monster_name]:
            card_stats = f"-{key}:{card_roster[monster_name][key]} "
            output_stats += card_stats
            total_stat_points += card_roster[monster_name][key]
        print(output_stats)

        print(f"*Total Stat: {total_stat_points}\n")


# Main Routine
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
