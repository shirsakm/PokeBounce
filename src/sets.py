from src.sprite_loader import INSTANCE as sprites
from src.poke import Poke


class Sets:
    sets = {
        "pikachu": Poke(
            75, 450,
            sprites.get_battler("pikachu"),
            ["Thunderbolt", "Quick Attack", "Iron Tail"],
            "Pikachu"
        ),
        "staraptor": Poke(
            600, 450,
            sprites.get_battler("staraptor"),
            ["Quick Attack", "Brave Bird", "Close Combat"],
            "Staraptor"
        ),
        "infernape": Poke(
            600, 75,
            sprites.get_battler("infernape"),
            ["Flamethrower", "Stone Edge", "Close Combat"],
            "Infernape"
        ),
        "umbreon": Poke(
            75, 75,
            sprites.get_battler("umbreon"),
            ["Quick Attack", "Dark Pulse", "Shadow Ball"],
            "Umbreon"
        ),
        "mamoswine": Poke(
            700, 500,
            sprites.get_battler("mamoswine"),
            ["Ice Beam", "Stone Edge", "Iron Head"],
            "Mamoswine"
        ),
        "nidoking": Poke(
            1000, 200,
            sprites.get_battler("nidoking"),
            ["Bubble Beam", "Stone Edge", "Poison Sting"],
            "Nidoking"
        ),
        "scizor": Poke(
            1000, 400,
            sprites.get_battler("scizor"),
            ["U Turn", "Iron Head", "Close Combat"],
            "Scizor"
        ),
        "wigglytuff": Poke(
            1200, 300,
            sprites.get_battler("wigglytuff"),
            ["Dazzling Gleam", "Flamethrower", "Thunderbolt"],
            "Wigglytuff"
        ),
        "decidueye": Poke(
            1200, 150,
            sprites.get_battler("decidueye"),
            ["Razor Leaf", "Brave Bird", "Shadow Ball"],
            "Decidueye"
        ),
        "kingdra": Poke(
            1200, 650,
            sprites.get_battler("kingdra"),
            ["Dragon Pulse", "Ice Beam", "Bubble Beam"],
            "Kingdra"
        ),
        "smeargle": Poke(
            700, 100,
            sprites.get_battler("smeargle"),
            [
                "Thunderbolt", "Quick Attack", "Flamethrower", "Shadow Ball",
                "Razor Leaf", "Bubble Beam", "U Turn", "Ice Beam", "Dragon Pulse",
                "Brave Bird", "Stone Edge", "Dazzling Gleam", "Close Combat",
                "Poison Sting", "Dark Pulse", "Iron Tail", "Iron Head",
                "Earthquake", "Sandstorm", "Waterfall", "Zen Headbutt",
                "Bonemerang", "Hyper Beam"
            ],
            "Smeargle"
        ),
        "marowak": Poke(
            700, 650,
            sprites.get_battler("marowak"),
            ["Bonemerang", "Flamethrower", "Shadow Ball"],
            "Marowak"
        ),
        "quagsire": Poke(
            300, 650,
            sprites.get_battler("quagsire"),
            ["Earthquake", "Poison Sting", "Waterfall"],
            "Quagsire"
        ),
        "porygonz": Poke(
            1000, 650,
            sprites.get_battler("porygonz"),
            ["Hyper Beam", "Thunderbolt", "Ice Beam"],
            "Porygon-Z"
        ),
        "tyranitar": Poke(
            850, 500,
            sprites.get_battler("tyranitar"),
            ["Sandstorm", "Dark Pulse", "Stone Edge"],
            "Tyranitar"
        ),
        "metagross": Poke(
            850, 100,
            sprites.get_battler("metagross"),
            ["Earthquake", "Zen Headbutt", "Iron Head"],
            "Metagross"
        ),
    }

    @staticmethod
    def get(set_id) -> Poke:
        if (set_id not in Sets.sets.keys()):
            raise ValueError(f"Invalid set id '{set_id}' referenced!")

        if (Sets.sets[set_id] is None):
            raise ValueError(f"Found set was None?? Id:'{set_id}'")

        return Sets.sets[set_id]
