import veggies
import protein
import fats
import carb


def foodGenerator():
    return "Meal:\n" + veggies.veggies() + protein.protein() + fats.fats() + carb.carb()



