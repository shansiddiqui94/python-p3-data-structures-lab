foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_food_names = []
    for food_dict in spicy_foods:
        if food_dict["heat_level"] > 5:
            spicy_food_names.append(food_dict["name"])  
    return spicy_food_names

def get_spiciest_foods(spicy_foods):
    spicy_food_names = []
    for food in spicy_foods: # we are using spicy_foods because that is the foods data coming in
        if food["heat_level"] > 3:
            spicy_food_names.append(food["name"])
    # return spicy_food_names

def print_spicy_foods(spicy_foods):
    for food_dict in spicy_foods:
        peppers = '🌶' * food_dict['heat_level']
        print(f"{food_dict['name']} ({food_dict['cuisine']}) | Heat Level: {peppers}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    spicy_food_names = []
    for food in spicy_foods:
        spicy_food_names.append(food["cuisine"])  


def print_spiciest_foods(spicy_foods):
    spiciest_food = None
    for food in spicy_foods:
        if spiciest_food is None or food['heat_level'] > spiciest_food['heat_level']:
            spiciest_food = food
    if spiciest_food is not None:
        print(f"The spiciest food is {spiciest_food['name']} with a heat level of {spiciest_food['heat_level']}")
    else:
        print("No spicy foods found")

def get_average_heat_level(spicy_foods):
    total = 0
    for food_dict in spicy_foods:
        total += food_dict['heat_level']
    print(total / len(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    # Add the new spicy food to the existing list of spicy foods
    spicy_foods.append(spicy_food)
