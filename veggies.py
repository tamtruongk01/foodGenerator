import random


def veggies():
    myVeggies = ["Broccoli ", "Asparagus", "Cauliflower", "Bell pepper", "Brussels sprout", "Collard", "Endive",
               "Lettuce", "Cabbage", "Spinach", "Celery", "Carrot", "Green bean"]

    return ("Veggies: " + myVeggies[random.randrange(len(myVeggies))] + " and " +
            myVeggies[random.randrange(len(myVeggies))] + "\n")