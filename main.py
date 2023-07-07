with open('recipes.txt', 'r') as recipes:
    cook_book = {}
    for rec in recipes:
        if rec == '\n':
            continue
        else:
            dish_list = []
            name_recipes = rec.strip()
            count_ing = int(recipes.readline())
            for ing in range(count_ing):
                ingredient = recipes.readline().split('|')
                dish_dict = {'ingredient_name': ingredient[0],
                             'quantity': ingredient[1],
                             'measure': ingredient[2].strip()}
                dish_list.append(dish_dict)
                cook_book[name_recipes] = dish_list
    print(cook_book)
