import easygui
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

final_output = ""

for monster_name in cards_roll:
    card_info = f"-={monster_name.upper()}=-\n"
    total_stat_points = 0

    for key in cards_roll[monster_name]:
        card_info += f"{key}:{cards_roll[monster_name][key]}, "
        total_stat_points += cards_roll[monster_name][key]
    final_output += f"{card_info}\n" \
                    f"Total Stat for {monster_name}: {total_stat_points}\n\n"
easygui.msgbox(final_output, "Title")
