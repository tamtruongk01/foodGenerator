import random


def carb():
    myCarb = ["Rice", "Sweet potatoes", "Potatoes", "Lentil"]
    return ("Carb: " + myCarb[random.randrange(len(myCarb))] + "\n")