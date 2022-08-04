from drones.dependencies.constants import *

# Drone Model Choices
MODELS = [
    (LIGHTWEIGHT, "Lightweight"),
    (MIDDLEWEIGHT, "Middleweight"),
    (CRUISERWEIGHT, "Cruiserweight"),
    (HEAVYWEIGHT, "Heavyweight")
]

# Drone State Choices
STATES = [
    (IDLE, "IDLE"),
    (LOADING, "LOADING"),
    (LOADED, "LOADED"),
    (DELIVERING, "DELIVERING"),
    (DELIVERED, "DELIVERED"),
    (RETURNING, "RETURNING")
]