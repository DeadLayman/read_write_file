with open('recipes.txt', 'r') as recipes:
    cook_book = {}
    for rec in recipes:
        if rec == '\n':
            continue
        else:
            list_dict = []
            name_recipes = rec.strip()
            count_ing = int(recipes.readline())
            for ing in range(count_ing):
                ingredient = recipes.readline().split('|')
                ing_dict = {'ingredient_name': ingredient[0],
                            'quantity': ingredient[1],
                            'measure': ingredient[2].strip()}
                list_dict.append(ing_dict)
                cook_book[name_recipes] = list_dict
    print(cook_book)


def shop_list(dishes, person_count):
    amount_ingredients = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for i in cook_book.get(dish):
                dict_count = {'quantity': int(i.get('quantity')) * person_count, 'measure': i.get('measure')}
                amount_ingredients[i.get('ingredient_name')] = dict_count
    print(amount_ingredients)


print()
shop_list(['Запеченный картофель', 'Омлет'], 5)
