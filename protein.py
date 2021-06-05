import random


def protein():
    myProtein = ["Chicken breast/thigh", "Beef", "Egg", "Fish"]
    return ("Protein: " + myProtein[random.randrange(len(myProtein))] + "\n")