import tomllib
import os
from src.resource_path import resource_path

try:
    config_path = resource_path("config.toml")
    with open(config_path, "rb") as f:
        config = tomllib.load(f)
except Exception as e:
    print(f"Failed to load config.toml: {e}")
    # Fallback configuration for web deployment
    config = {
        "Debug": {
            "overrideBattlers": False,
            "testMoves": False,
            "battlerOverride": ["Greninja", "Muk", "Kangaskhan"],
            "showHitboxes": False,
            "showCollisionBoxes": False,
        }
    }
