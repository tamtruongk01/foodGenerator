import veggies
import protein
import fats
import carb


def foodGenerator(i):
    print(str(i) + " Meal:\n" + veggies.veggies() + protein.protein() + fats.fats() + carb.carb())

for i in range(1, 3 + 1):
    foodGenerator(i)


