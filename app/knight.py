def calculate_protection(knight):
    return sum(piece["protection"] for piece in knight["armour"])


def calculate_power(knight):
    power = knight["power"] + knight["weapon"]["power"]
    if knight["potion"] is not None:
        power += knight["potion"]["effect"].get("power", 0)
    return power


def calculate_hp(knight):
    hp = knight["hp"]
    if knight["potion"] is not None:
        hp += knight["potion"]["effect"].get("hp", 0)
    return hp


def apply_battle_stats(knight):
    protection = calculate_protection(knight)
    if knight["potion"] is not None:
        protection += knight["potion"]["effect"].get("protection", 0)

    knight["protection"] = protection
    knight["power"] = calculate_power(knight)
    knight["hp"] = calculate_hp(knight)
    return knight
