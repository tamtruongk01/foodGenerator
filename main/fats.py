import random


def fats():
    myFats = ["Avocado", "Nuts", "Cheese", "Full fat yogurt", "Edamame"]
    return ("Fats: " + myFats[random.randrange(len(myFats))] + "\n")