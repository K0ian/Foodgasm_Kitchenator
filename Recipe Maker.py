import random  # Importing the random module for random selection

# ------------------------------
# Reference Databases for Food Lists
# ------------------------------

# Dictionary containing different types of alcoholic beverages and their brands
alcohol_db = {
    "Whiskey": [
        "Jack Daniel’s Tennessee Whiskey", "Johnnie Walker Red Label", "Johnnie Walker Black Label",
        "Johnnie Walker Blue Label", "Johnnie Walker Green Label", "Johnnie Walker Gold Label",
        "Jameson", "Macallan", "Chivas Regal", "Maker’s Mark", "Buffalo Trace", "Glenfiddich"
    ],
    "Vodka": ["Grey Goose", "Belvedere", "Absolut", "Smirnoff", "Cîroc", "Ketel One", "Tito’s Handmade Vodka"],
    "Rum": [
        "Bacardi (Superior, Gold, Black, Spiced)", "Captain Morgan (Original Spiced, Black Spiced, Private Stock)",
        "Mount Gay (Eclipse, XO, Black Barrel)", "Appleton Estate", "Havana Club"
    ],
    "Tequila": [
        "Patrón (Silver, Reposado, Añejo)", "Don Julio (Blanco, Reposado, 1942)",
        "Jose Cuervo (Especial, Reserva de la Familia)", "Casamigos (Blanco, Reposado, Añejo)", "Clase Azul"
    ],
    "Gin": ["Tanqueray", "Hendrick’s", "Bombay Sapphire", "Beefeater", "Gordon’s"],
    "Beer": ["Budweiser", "Corona", "Heineken", "Guinness", "Stella Artois", "Coors Light"],
    "Wine": {
        "Red Wine": ["Cabernet Sauvignon", "Merlot", "Pinot Noir", "Malbec"],
        "White Wine": ["Chardonnay", "Sauvignon Blanc", "Riesling", "Pinot Grigio"],
        "Rosé": ["Provence Rosé", "White Zinfandel"],
        "Sparkling Wine": ["Champagne (Moët & Chandon, Veuve Clicquot)", "Prosecco", "Cava"]
    },
    "Champagne": {
        "Brut": ["Moët & Chandon Brut Impérial", "Veuve Clicquot Yellow Label", "Taittinger Brut Réserve",
                 "Louis Roederer Brut Premier", "Bollinger Special Cuvée Brut", "Piper-Heidsieck Brut"],
        "Extra Brut": ["Laurent-Perrier Ultra Brut", "Billecart-Salmon Extra Brut", "Pol Roger Pure Extra Brut"],
        "Demi-Sec": ["Moët & Chandon Nectar Impérial", "Veuve Clicquot Demi-Sec", "Taittinger Nocturne Sec"],
        "Rosé": ["Laurent-Perrier Cuvée Rosé", "Billecart-Salmon Brut Rosé", "Ruinart Brut Rosé",
                 "Perrier-Jouët Blason Rosé"],
        "Blanc de Blancs": ["Ruinart Blanc de Blancs", "Taittinger Comtes de Champagne Blanc de Blancs",
                            "Salon Le Mesnil Blanc de Blancs", "Pierre Gimonnet & Fils Blanc de Blancs"],
        "Blanc de Noirs": ["Bollinger Vieilles Vignes Françaises Blanc de Noirs",
                           "Egly-Ouriet Grand Cru Blanc de Noirs",
                           "Aubry Brut Blanc de Noirs"],
        "Prestige Cuvée": ["Dom Pérignon Vintage", "Louis Roederer Cristal", "Krug Grande Cuvée",
                           "Perrier-Jouët Belle Epoque"]
    }
}

# List of available soda brands
sodas_db = ["Coca-Cola", "Coca-Cola Zero", "Pepsi", "Sprite", "Fanta"]

# List of healthy drinks
healthy_drinks_db = [
    "Water", "Coconut Water", "Green Tea", "Herbal Tea", "Orange Juice", "Apple Juice", "Kombucha", "Almond Milk",
    "Whole Milk", "Skim Milk"
]

# Dictionary containing different types of pasta
pastas_db = {
    "Long Pastas": ["Spaghetti", "Linguine", "Fettuccine", "Tagliatelle", "Pappardelle", "Angel Hair (Capellini)",
                    "Bucatini", "Vermicelli"],
    "Short Pastas": ["Penne", "Rigatoni", "Ziti", "Macaroni (Elbow Macaroni)", "Cavatappi", "Orecchiette", "Fusilli",
                     "Rotini", "Casarecce", "Campanelle"],
    "Stuffed Pastas": ["Ravioli", "Tortellini", "Tortelloni", "Agnolotti", "Mezzelune"],
    "Flat & Sheet Pastas": ["Lasagna", "Malfadine (Reginette)", "Cannelloni", "Manicotti"],
    "Mini Pastas": ["Orzo", "Ditalini", "Acini di Pepe", "Fregola", "Pastina"]
}

# Dictionary containing different types of cereals
cereals_db = {
    "Classic": ["Corn Flakes", "Rice Krispies", "Grape Nuts", "Cheerios", "Life Cereal"],
    "Oat-Based": ["Old-Fashioned Oats", "Rolled Oats", "Instant Oatmeal"],
    "Sweetened": ["Froot Loops", "Cocoa Krispies", "Lucky Charms", "Frosted Flakes", "Count Chocula"],
    "High-Fiber": ["Fiber One", "All-Bran", "Special K"],
    "Granola/Muesli": ["Nature Valley Granola", "Kashi Go Lean", "Bear Naked Granola", "Bob's Red Mill Muesli"],
    "Wheat/Bran": ["Wheaties", "Bran Flakes", "Cracklin' Oat Bran"],
    "Protein-Packed": ["Cheerios Protein", "Special K Protein", "Kashi Go Lean Crunch"],
    "Organic/Healthy": ["Annie's Homegrown Organic Bunny Cereal", "Nature's Path Organic Granola",
                        "Kashi Organic Promise Cereal"],
    "Kids": ["Frosted Mini Wheats", "Cinnamon Toast Crunch", "Apple Jacks", "Trix"],
    "Gluten-Free": ["Chex (various)", "Gluten-Free Cheerios"]
}

# Dictionary containing different types of pizzas
pizzas_db = {
    "Classic Italian": ["Margherita", "Marinara", "Quattro Formaggi", "Napolitana", "Romana", "Diavola", "Capricciosa",
                        "Quattro Stagioni"],
    "American-Style": ["Pepperoni", "Meat Lover’s", "BBQ Chicken", "Hawaiian", "Buffalo Chicken", "Supreme",
                       "Cheese Pizza", "White Pizza (Bianca)"],
    "Gourmet/Specialty": ["Truffle Pizza", "Fig & Prosciutto", "Pesto Chicken", "Spinach & Ricotta", "Mediterranean",
                          "Egg & Bacon Pizza"],
    "Deep Dish/Thick Crust": ["Chicago Deep Dish", "Detroit-Style", "Sicilian (Sfincione)", "Grandma Pizza"],
    "Flatbread/Alternative": ["Flatbread Pizza", "Cauliflower Crust Pizza", "Gluten-Free Pizza", "Vegan Pizza"]
}

# Dictionary containing different types of soups
soups_db = {
    "Classic": ["Tomato Soup", "Chicken Noodle Soup", "Minestrone", "French Onion Soup", "Split Pea Soup",
                "Lentil Soup", "Potato Soup", "Beef and Barley Soup", "Clam Chowder"],
    "Cream-Based": ["Cream of Mushroom Soup", "Cream of Broccoli Soup", "Cream of Chicken Soup",
                    "Cream of Asparagus Soup", "Potato Leek Soup"],
    "International": ["Tom Yum", "Pho", "Borscht", "Gazpacho", "Avgolemono", "Sopa de Lima", "Ramen", "Caldo Gallego",
                      "Harira"],
    "Hearty/Meaty": ["Beef Stew", "Chicken and Rice Soup", "Cheddar Broccoli Soup", "Chili", "Sausage and Bean Soup",
                     "Pork Pozole"],
    "Cold": ["Chilled Cucumber Soup", "Vichyssoise", "Ajo Blanco", "Cantaloupe Soup"],
    "Brothy": ["Chicken Consommé", "Beef Consommé", "Egg Drop Soup", "Hot & Sour Soup"]
}

# Dictionary containing different types of salads
salads_db = {
    "Classic": ["Caesar Salad", "Greek Salad", "Cobb Salad", "Waldorf Salad", "Caprese Salad", "Spinach Salad",
                "House Salad", "Garden Salad"],
    "Leafy": ["Arugula Salad", "Chopped Salad", "Lettuce Wedge Salad", "Endive Salad", "Mixed Greens Salad"],
    "Fruit-Based": ["Fruit Salad", "Apple Walnut Salad", "Strawberry Spinach Salad", "Watermelon Feta Salad",
                    "Citrus Salad", "Pineapple and Shrimp Salad"],
    "Grain-Based": ["Quinoa Salad", "Tabbouleh", "Couscous Salad", "Farro Salad", "Rice Salad", "Barley Salad"],
    "Protein-Packed": ["Chicken Salad", "Tuna Salad", "Egg Salad", "Chickpea Salad", "Salmon Salad", "Tofu Salad"],
    "Specialty": ["Pasta Salad", "Potato Salad", "Coleslaw", "Cauliflower Salad", "Cabbage Salad"],
    "Warm": ["Warm Kale Salad", "Warm Sweet Potato Salad", "Grilled Vegetable Salad", "Warm Bacon Spinach Salad"]
}

# Dictionary containing different types of sandwiches
sandwiches_db = {
    "Classic": ["BLT", "Club Sandwich", "Grilled Cheese", "Turkey and Swiss", "Ham and Cheese", "Egg Salad Sandwich",
                "Tuna Salad Sandwich", "Chicken Salad Sandwich", "Roast Beef and Cheddar", "Veggie Sandwich"],
    "Hot": ["Reuben Sandwich", "Philly Cheesesteak", "Pulled Pork Sandwich", "Meatball Sub", "French Dip",
            "Grilled Chicken Sandwich", "Cuban Sandwich", "Sloppy Joe", "Chicken Parmesan Sandwich",
            "Toasted Veggie Sandwich"],
    "Regional": ["Monte Cristo", "Shawarma Sandwich"],
    "Vegetarian/Vegan": ["Avocado Toast", "Hummus and Veggie Sandwich", "Caprese Sandwich", "Vegan 'Chicken' Sandwich",
                         "Peanut Butter and Jelly", "Falafel Sandwich", "Grilled Veggie Sandwich", "Vegan BLT",
                         "Eggplant Parmesan Sandwich", "Tempeh Bacon Sandwich"],
    "Sweet": ["Nutella Sandwich", "Banana Peanut Butter Sandwich", "S’mores Sandwich", "Cinnamon Sugar Toast",
              "Apple Cinnamon Sandwich"],
    "Wraps/Alternatives": ["Chicken Caesar Wrap", "Veggie Wrap", "Buffalo Chicken Wrap", "Falafel Wrap", "Burrito"]
}

# Dictionary containing different types of meat
meats_db = {
    "Red Meat": {
        "Beef": ["Ribeye Steak", "T-bone Steak", "Filet Mignon", "Sirloin Steak", "Ground Beef", "Flank Steak",
                 "Skirt Steak", "Chuck Roast", "Brisket", "Beef Ribs", "Corned Beef", "Beef Wellington"],
        "Lamb": ["Lamb Chops", "Lamb Shank", "Leg of Lamb", "Lamb Ribs", "Ground Lamb", "Lamb Shoulder",
                 "Lamb Stew Meat"],
        "Pork": ["Pork Tenderloin", "Pork Chops", "Bacon", "Ham", "Pork Ribs", "Sausages", "Pulled Pork", "Pork Belly",
                 "Pork Shoulder"],
        "Game Meat": ["Venison", "Wild Boar", "Bison", "Elk", "Kangaroo", "Ostrich", "Camel"]
    },
    "White Meat": {
        "Poultry": ["Chicken Breast", "Chicken Thighs", "Chicken Wings", "Whole Chicken", "Duck Breast", "Goose",
                    "Turkey", "Quail", "Pheasant", "Cornish Hen", "Chicken Sausage"],
        "Others": ["Rabbit"]
    }
}

# Dictionary containing different types of fish
fish_db = {
    "Fish": ["Salmon", "Tuna", "Cod", "Trout", "Snapper", "Sea Bass", "Grouper", "Pollock", "Flounder", "Sole",
             "Anchovies", "Chilean Sea Bass", "Barramundi", "Herring", "Rainbow Trout", "Arctic Char"],
    "Shellfish": ["Shrimp", "Lobster", "Crab", "Clams", "Mussels", "Oysters", "Scallops", "Crawfish", "Abalone",
                  "Octopus", "Squid (Calamari)", "King Crab"]
}

# Dictionary containing different types of vegetables and fruits
veg_fruits_db = {
    "Vegetables": {
        "Leafy": ["Spinach", "Kale", "Lettuce (Romaine, Iceberg, Butterhead)", "Swiss Chard", "Collard Greens",
                  "Mustard Greens", "Arugula", "Watercress"],
        "Cruciferous": ["Broccoli", "Cauliflower", "Brussels Sprouts", "Cabbage (Green, Red, Napa, Savoy)", "Bok Choy",
                        "Kohlrabi", "Radish"],
        "Root": ["Carrots", "Beets", "Turnips", "Radishes", "Sweet Potatoes", "Yams", "Parsnips", "Rutabaga", "Daikon"],
        "Allium": ["Onions (Red, White, Yellow, Sweet, Green)", "Garlic", "Shallots", "Leeks", "Chives"],
        "Nightshades": ["Tomatoes", "Bell Peppers (Red, Green, Yellow, Orange)",
                        "Chili Peppers (Jalapeño, Habanero, Serrano, Poblano)", "Eggplant", "Tomatillo"],
        "Squashes": ["Zucchini", "Pumpkin", "Butternut Squash", "Cucumber"],
        "Legumes": ["Green Beans", "Snap Peas", "Snow Peas", "Edamame", "Lentils", "Chickpeas", "Black Beans",
                    "Kidney Beans"],
        "Starchy": ["Potatoes (Russet, Yukon Gold, Red, Fingerling)", "Corn", "Cassava", "Jicama", "Plantains"],
        "Others": ["Celery", "Asparagus", "Mushrooms (Portobello, Cremini, Shiitake, Button)", "Okra", "Artichoke",
                   "Fennel"]
    },
    "Fruits": {
        "Citrus": ["Oranges", "Lemons", "Limes", "Grapefruits", "Tangerines", "Clementines", "Pomelo"],
        "Berries": ["Strawberries", "Blueberries", "Raspberries", "Blackberries", "Cranberries", "Gooseberries"],
        "Stone": ["Peaches", "Plums", "Cherries", "Apricots", "Nectarines", "Mangoes"],
        "Tropical": ["Pineapple", "Banana", "Papaya", "Coconut", "Guava", "Passion Fruit", "Dragon Fruit", "Starfruit"],
        "Melons": ["Watermelon", "Cantaloupe", "Galia Melon"],
        "Apples/Pears": ["Apples", "Pears"],
        "Grapes": ["Red Grapes", "Green Grapes", "Black Grapes", "Concord Grapes"],
        "Exotic": ["Pomegranate", "Lychee", "Persimmon", "Fig", "Rambutan", "Mangosteen"]
    }
}

# Dictionary containing different types of chips
chips_db = {
    "Lays": ["Classic", "Sour Cream & Onion", "BBQ", "Cheddar & Sour Cream", "Salt & Vinegar", "Flamin’ Hot",
             "Dill Pickle", "Honey BBQ", "Chile Limón", "Wavy Original", "Wavy Ranch"],
    "Ruffles": ["Original", "Cheddar & Sour Cream", "Sour Cream & Onion", "All Dressed", "Flamin’ Hot Cheddar",
                "Jalapeño Ranch", "Lime & Jalapeño", "Queso"],
    "Pringles": ["Original", "Sour Cream & Onion", "Cheddar Cheese", "BBQ", "Pizza", "Salt & Vinegar", "Jalapeño",
                 "Ranch", "Hot & Spicy", "Honey Mustard"],
    "Doritos": ["Nacho Cheese", "Cool Ranch", "Spicy Sweet Chili", "Flamin’ Hot Nacho", "Salsa Verde", "Spicy Nacho",
                "Blazin’ Buffalo & Ranch", "Tapatío", "Dinamita Chile Limón", "Flamas"],
    "Takis": ["Fuego (Hot Chili Pepper & Lime)", "Nitro (Habanero & Lime)", "Blue Heat (Extreme Hot Chili)",
              "Crunchy Fajitas", "Guacamole"]
}

# Dictionary containing different types of candy
candy_db = {
    "Chocolate Bars": ["Snickers", "Milky Way", "Twix", "Kit Kat", "Mars", "Hershey’s Milk Chocolate",
                       "Reese’s Peanut Butter Cups", "Nestlé Crunch"],
    "Gummy Candies": ["Haribo Gold Bears", "Trolli Sour Brite Crawlers", "Swedish Fish", "Sour Patch Kids",
                      "Jolly Rancher Gummies"],
    "Hard Candies": ["Jolly Rancher", "Lollipops", "Smarties"],
    "Chewy Candies": ["Starburst", "Airheads", "Laffy Taffy", "Now and Later", "Hi-Chew", "Sour Patch Watermelon",
                      "Brach’s Jelly Beans", "Tootsie Rolls"],
    "Sour Candies": ["Warheads", "Sour Patch Kids", "Trolli Sour Brite Crawlers", "Sour Skittles", "Sour Punch Straws",
                     "SweetTarts", "Toxic Waste"],
    "Caramel Candies": ["Werther’s Original Caramel", "Milk Duds", "Rolos", "Caramel Kisses", "Twix Caramel"]
}

# Dictionary containing different types of sauces
sauces_db = {
    "Tomato-Based": ["Marinara Sauce", "Tomato Ketchup", "Pizza Sauce", "Tomato Basil Sauce", "Salsa"],
    "Creamy": ["Alfredo Sauce", "Ranch Dressing", "Caesar Dressing", "Mayonnaise", "Blue Cheese Dressing"],
    "Barbecue": ["Sweet BBQ Sauce", "Spicy BBQ Sauce", "Honey BBQ Sauce", "Mustard-Based BBQ Sauce",
                 "Mesquite BBQ Sauce"],
    "Vinegar-Based": ["Balsamic Glaze", "Apple Cider Vinegar Sauce", "Chili Vinegar Sauce", "Vinaigrette"],
    "Hot Sauces": ["Tabasco Sauce", "Sriracha Sauce", "Frank's RedHot Sauce", "Cholula Hot Sauce", "Tapatío"],
    "Asian": ["Soy Sauce", "Teriyaki Sauce", "Oyster Sauce", "Hoisin Sauce", "Peanut Sauce", "Sweet Chili Sauce"]
}

# ------------------------------
# Helper Functions
# ------------------------------

def flatten_list(nested):
    """Flatten a nested list or dictionary of lists into a single list."""
    flat = []  # Initialize an empty list to store the flattened elements

    if isinstance(nested, dict):  # Check if the input is a dictionary
        for value in nested.values():  # Iterate through dictionary values
            flat.extend(flatten_list(value))  # Recursively flatten each value and add to the list

    elif isinstance(nested, list):  # Check if the input is a list
        for item in nested:  # Iterate through list elements
            if isinstance(item, (list, dict)):  # If an item is a list or dictionary, recursively flatten it
                flat.extend(flatten_list(item))  # Extend the flat list with the flattened item
            else:
                flat.append(item)  # If the item is not a list or dict, add it directly to the flat list

    return flat  # Return the fully flattened list


def get_random_protein(diet_preference, available_ingredients):
    """Select a protein from available ingredients based on dietary preference."""
    protein_candidates = []  # Initialize an empty list for protein options

    # Determine protein options based on the user's diet preference
    if diet_preference in ["non vegetarian", "i eat everything", "high protein"]:
        protein_candidates = flatten_list(meats_db) + fish_db["Fish"]  # Include meats and fish options
    elif diet_preference in ["vegetarian", "vegan"]:
        protein_candidates = ["tofu", "tempeh", "chickpeas", "lentils"]  # Include plant-based protein options

    # Filter the protein options based on available ingredients
    filtered_proteins = [prot for prot in protein_candidates if
                         any(ing.lower() in prot.lower() for ing in available_ingredients)]

    # If filtered options exist, select a random one; otherwise, select from all candidates; default to tofu if empty
    return random.choice(filtered_proteins) if filtered_proteins else (
        random.choice(protein_candidates) if protein_candidates else "tofu")


# ------------------------------
# Dynamic Meal Generation Functions
# ------------------------------

def dynamic_breakfast(diet_preference, available_ingredients):
    """Generate a random breakfast meal dynamically."""
    option = random.choice(["cereal", "smoothie"])  # Randomly select between cereal or smoothie

    if option == "cereal":
        cereal = random.choice(flatten_list(cereals_db))  # Choose a random cereal from the database

        # Select a milk-based drink if available; otherwise, choose any healthy drink
        milk_options = [d for d in healthy_drinks_db if "milk" in d.lower()]
        drink = random.choice(milk_options) if milk_options else random.choice(healthy_drinks_db)

        meal_name = f"{cereal} Bowl"  # Format the meal name
        instructions = f"Pour {drink} over a bowl of {cereal} and enjoy your breakfast."  # Instructions
        ingredients = [cereal, drink]  # List of ingredients used

    else:  # If smoothie is selected
        fruit = random.choice(flatten_list(veg_fruits_db["Fruits"]))  # Choose a random fruit
        drink = random.choice(healthy_drinks_db)  # Choose a random healthy drink

        meal_name = f"{fruit} Smoothie"  # Format the meal name
        instructions = f"Blend {fruit} with {drink} and some ice to make a refreshing smoothie."  # Instructions
        ingredients = [fruit, drink, "ice"]  # List of ingredients

    # Return the meal name and a dictionary with meal details
    return meal_name, {
        "ingredients": ingredients,
        "instructions": instructions,
        "diet": [diet_preference, "i eat everything"],  # Supported diet preferences
        "individuals": ["student", "student-athlete", "busy professional"]  # Suitable for specific individuals
    }


def dynamic_lunch_dinner(diet_preference, available_ingredients):
    """Generate a lunch or dinner meal using only available ingredients."""

    protein = get_random_protein(diet_preference, available_ingredients)  # Get a random protein based on diet

    # Filter available starches, vegetables, and sauces based on user-provided ingredients
    available_starches = [item for item in flatten_list(pastas_db) if
                          any(ing.lower() in item.lower() for ing in available_ingredients)]
    available_vegetables = [item for item in flatten_list(veg_fruits_db["Vegetables"]) if
                            any(ing.lower() in item.lower() for ing in available_ingredients)]
    available_sauces = [item for item in flatten_list(sauces_db) if
                        any(ing.lower() in item.lower() for ing in available_ingredients)]

    # Select a starch, vegetable, and sauce, or use default values if none are available
    starch = random.choice(available_starches) if available_starches else "any available grain or pasta"
    vegetable = random.choice(available_vegetables) if available_vegetables else "any fresh vegetable"
    sauce = random.choice(available_sauces) if available_sauces else "olive oil and salt"

    meal_name = f"{protein} with {starch}, {vegetable}, and {sauce}"  # Format the meal name
    instructions = (
        f"Cook {protein} as desired (grill, bake, or sauté). Prepare {starch} if available. "
        f"Lightly cook or serve {vegetable} raw. Add {sauce} for flavor."
    )  # Instructions for cooking the meal

    ingredients = [protein, starch, vegetable, sauce]  # List of ingredients used

    # Return the meal name and a dictionary with meal details
    return meal_name, {
        "ingredients": ingredients,
        "instructions": instructions,
        "diet": [diet_preference, "i eat everything"],  # Supported diet preferences
        "individuals": ["student", "student-athlete", "busy professional"]  # Suitable for specific individuals
    }


def dynamic_snack(diet_preference, available_ingredients):
    """Generate a random snack dynamically."""
    option = random.choice(["chips", "candy", "healthy"])  # Randomly choose between chips, candy, or a healthy snack

    if option == "chips":
        chip_brand = random.choice(list(chips_db.keys()))  # Select a random chip brand
        flavor = random.choice(chips_db[chip_brand])  # Select a random flavor from that brand

        meal_name = f"{chip_brand} {flavor} Chips"  # Format the snack name
        instructions = f"Enjoy a serving of {chip_brand} chips in {flavor} flavor."  # Instructions
        ingredients = [f"{chip_brand} {flavor}"]  # List of ingredients used

    elif option == "candy":
        candy_category = random.choice(list(candy_db.keys()))  # Select a random candy category
        candy_item = random.choice(candy_db[candy_category])  # Select a random candy from that category

        meal_name = f"{candy_item}"  # Format the snack name
        instructions = f"Have a sweet treat: {candy_item} from the {candy_category} category."  # Instructions
        ingredients = [candy_item]  # List of ingredients used

    else:  # If healthy snack is selected
        fruit = random.choice(flatten_list(veg_fruits_db["Fruits"]))  # Choose a random fruit

        meal_name = f"Fresh {fruit}"  # Format the snack name
        instructions = f"Enjoy a healthy snack of fresh {fruit}."  # Instructions
        ingredients = [fruit]  # List of ingredients used

    # Return the snack name and a dictionary with meal details
    return meal_name, {
        "ingredients": ingredients,
        "instructions": instructions,
        "diet": [diet_preference, "i eat everything"],  # Supported diet preferences
        "individuals": ["student", "student-athlete", "busy professional"]  # Suitable for specific individuals
    }


def dynamic_date_meal(diet_preference, available_ingredients):
    """Generate a meal for 'Chilling with BAE' using only available ingredients."""

    # Convert all available ingredients to lowercase for matching
    available_ingredients = [ing.lower() for ing in available_ingredients]

    # Filter available dishes strictly based on user-provided ingredients
    available_pizzas = [item for item in flatten_list(pizzas_db) if
                        any(ing in item.lower() for ing in available_ingredients)]
    available_salads = [item for item in flatten_list(salads_db) if
                        any(ing in item.lower() for ing in available_ingredients)]
    available_sandwiches = [item for item in flatten_list(sandwiches_db) if
                            any(ing in item.lower() for ing in available_ingredients)]
    available_pastas = [item for item in flatten_list(pastas_db) if
                        any(ing in item.lower() for ing in available_ingredients)]
    available_proteins = [item for item in flatten_list(meats_db) + flatten_list(fish_db) if
                          any(ing in item.lower() for ing in available_ingredients)]
    available_sauces = [item for item in flatten_list(sauces_db) if
                        any(ing in item.lower() for ing in available_ingredients)]

    # Prioritize pasta, pizza, or salad depending on available ingredients
    if available_pastas and available_proteins and available_sauces:
        starch = random.choice(available_pastas)  # Choose a random pasta
        protein = random.choice(available_proteins)  # Choose a random protein
        sauce = random.choice(available_sauces)  # Choose a random sauce

        meal_name = f"{protein} Pasta with {sauce}"  # Format meal name
        instructions = f"Cook the {starch} per package instructions, prepare {protein}, and mix with {sauce}."  # Instructions
        ingredients = [starch, protein, sauce]  # Ingredients used

    elif available_pizzas:
        dish = random.choice(available_pizzas)  # Choose a pizza
        meal_name = f"{dish} Pizza"
        instructions = f"Prepare a {dish} pizza using your available ingredients and bake it."
        ingredients = [dish]

    elif available_salads:
        dish = random.choice(available_salads)  # Choose a salad
        meal_name = f"{dish} Salad"
        instructions = f"Toss together a fresh {dish} salad with your ingredients."
        ingredients = [dish]

    else:  # Default to a custom meal if no structured meal is available
        random_ingredients = random.sample(available_ingredients, min(len(available_ingredients), 3))
        meal_name = "Custom Dish with " + ", ".join(random_ingredients)
        instructions = f"Use your available ingredients ({', '.join(random_ingredients)}) to prepare a custom meal."
        ingredients = random_ingredients

    # Choose a drink strictly from available ingredients
    available_beverages = [item for item in healthy_drinks_db + sodas_db if
                           any(ing in item.lower() for ing in available_ingredients)]
    # Filter drinks based on user-provided ingredients by checking if any ingredient matches

    beverage = random.choice(available_beverages) if available_beverages else "water"
    # If any matching drinks are found, select one randomly; otherwise, default to "water"

    # Update meal name and instructions with the selected beverage
    meal_name += f" with {beverage}"  # Append the selected drink to the meal name
    instructions += f" Serve with a refreshing glass of {beverage}."  # Add serving instructions

    ingredients.append(beverage)  # Add the selected beverage to the list of ingredients

    # Return meal details in a dictionary format
    return meal_name, {
        "ingredients": ingredients,  # List of ingredients used in the meal
        "instructions": instructions,  # Step-by-step instructions for preparing the meal
        "diet": [diet_preference, "i eat everything"],  # Supported dietary preferences
        "individuals": ["student", "student-athlete", "busy professional"]  # Suitable for specific individuals
    }

# ------------------------------
# Main Dynamic Meal Generator
# ------------------------------

def dynamic_meal_planner():
    """Main function to generate a dynamic meal based on user input."""

    # Display welcome message
    print("🍽 Welcome to your Friendly Neighborhood Foodgasm Kitchenator! 🍽\n")

    # Prompt user for their profile type and format the input
    user_type = input("Enter your profile (student, student-athlete, busy professional): ").strip().lower()

    # Prompt user for meal type and format input with title case
    meal_type = input(
        "Enter the meal type (Breakfast, Lunch, Dinner, Midday Snack, Pre-Gym Snack, Post Gym Snack, Chilling with BAE): "
    ).strip().title()

    # Prompt user for dietary preference and format input in lowercase
    diet_preference = input(
        "Enter your dietary preference (vegetarian, non vegetarian, vegan, high protein, gluten-free, i eat everything): "
    ).strip().lower()

    # Prompt user to enter available ingredients in a specific format
    ingredients_input = input(
        "Enter available ingredients in this format:\n"
        "Grain choice, Protein choice, Vegetable choice, Snack choice, Sauce choice, Drink choice.\n"
        "Type 'none' if missing an ingredient: "
    ).lower()

    # Convert user input into a list by splitting on commas and removing extra spaces
    available_ingredients = [i.strip() for i in ingredients_input.split(",") if i.strip()]

    # Choose the appropriate dynamic meal generation function based on meal type
    if meal_type == "Breakfast":
        meal_name, details = dynamic_breakfast(diet_preference, available_ingredients)
    elif meal_type in ["Lunch", "Dinner"]:
        meal_name, details = dynamic_lunch_dinner(diet_preference, available_ingredients)
    elif meal_type in ["Midday Snack", "Pre-Gym Snack", "Post Gym Snack", "Snacks"]:
        meal_name, details = dynamic_snack(diet_preference, available_ingredients)
    elif meal_type == "Chilling With Bae":
        meal_name, details = dynamic_date_meal(diet_preference, available_ingredients)
    else:
        # If meal type is not recognized, default to generating a random snack
        print("Meal type not recognized. Generating a random snack.")
        meal_name, details = dynamic_snack(diet_preference, available_ingredients)

    # Print meal details
    print("\n🍽 Generated Meal:")
    print("Meal Name:", meal_name)  # Display the meal name
    print("Ingredients:", ", ".join(details["ingredients"]))  # Display ingredients as a comma-separated string
    print("Instructions:", details["instructions"])  # Display cooking/preparation instructions
    print("Dietary Preference:", ", ".join(details["diet"]))  # Display applicable diet preferences
    print("Suitable For:", ", ".join(details["individuals"]))  # Display the target audience for the meal
    print("Bon Appétit! 🍽")  # Print a friendly closing message


# Run the dynamic meal generator
dynamic_meal_planner()  # Execute the function to start the meal generation process
