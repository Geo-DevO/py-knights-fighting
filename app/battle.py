from typing import Tuple

from app.knight import Knight


def fight(knight_a: Knight, knight_b: Knight) -> Tuple[Knight, Knight]:
    damage_to_a = knight_b["power"] - knight_a["protection"]
    damage_to_b = knight_a["power"] - knight_b["protection"]

    knight_a["hp"] = max(0, knight_a["hp"] - damage_to_a)
    knight_b["hp"] = max(0, knight_b["hp"] - damage_to_b)

    return knight_a, knight_b
