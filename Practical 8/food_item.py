class food_item:
    """
    A class to represent a food item with its nutritional information.
    
    Attributes:
        name (str): Name of the food item
        calories (float): Calories per serving (kcal)
        protein (float): Protein content per serving (g)
        carbohydrates (float): Carbohydrate content per serving (g)
        fat (float): Fat content per serving (g)
    """
    def __init__(self, name, calories, protein, carbohydrates, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat


def calculate_daily_nutrition(food_list):
    """
    Calculate and report total daily nutritional intake from a list of food items.
    Issues warnings if calorie intake > 2500 kcal or fat intake > 90 g.
    
    Args:
        food_list (list): List of food_item instances consumed in 24 hours
        
    Returns:
        tuple: (total_calories, total_protein, total_carbs, total_fat)
    """
    # Initialize total nutritional counters
    total_calories = 0.0
    total_protein = 0.0
    total_carbs = 0.0
    total_fat = 0.0

    # Accumulate values from all consumed food items
    for food in food_list:
        total_calories += food.calories
        total_protein += food.protein
        total_carbs += food.carbohydrates
        total_fat += food.fat

    # Print formatted nutrition summary
    print("=" * 45)
    print("          24-Hour Nutrition Summary          ")
    print("=" * 45)
    print(f"Total Calories:    {total_calories:>7.1f} kcal")
    print(f"Total Protein:    {total_protein:>7.1f} g")
    print(f"Total Carbs:      {total_carbs:>7.1f} g")
    print(f"Total Fat:        {total_fat:>7.1f} g")
    print("=" * 45)

    # Check and print intake warnings
    if total_calories > 2500:
        print("⚠️  WARNING: Calorie intake exceeds 2500 kcal daily limit!")
    if total_fat > 90:
        print("⚠️  WARNING: Fat intake exceeds 90 g daily limit!")

    # Return totals for potential further analysis
    return total_calories, total_protein, total_carbs, total_fat


# Required Usage Example 
if __name__ == "__main__":
    # 1. Create food_item instances with real nutritional data
    apple = food_item("Apple (1 medium)", 60, 0.3, 15, 0.5)
    cheeseburger = food_item("Cheeseburger", 500, 30, 40, 25)
    whole_milk = food_item("Whole Milk (250ml)", 150, 8, 12, 8)
    medium_fries = food_item("French Fries (medium)", 365, 4, 48, 17)
    dark_chocolate = food_item("Dark Chocolate (100g)", 546, 4.9, 61, 31)
    pepperoni_pizza = food_item("Pepperoni Pizza (1 slice)", 285, 12, 30, 15)

    # 2. List of food consumed in 24 hours
    daily_intake = [apple, cheeseburger, whole_milk, medium_fries, dark_chocolate, pepperoni_pizza]

    # 3. Calculate and display daily nutrition
    calculate_daily_nutrition(daily_intake)