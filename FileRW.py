
def get_recipe():
    cook_book = {}


    with open("recipes.txt", "r", encoding="utf-8") as file:
        for line in file:
            main_dish = line.strip()
            ingridient_quantity = int(file.readline().strip())
            ingridient_list = []
            for ingridient in range(ingridient_quantity):
                position = {}
                ingridient_info = []
                ingridient_line = file.readline().strip()
                ingridient_info = ingridient_line.split('|')
                position['ingridient_name'] = ingridient_info[0]
                position['quantity'] = ingridient_info[1]
                position['measure'] = ingridient_info[2]
                ingridient_list.append(position)
            file.readline()
            cook_book[main_dish] = ingridient_list

    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    ingridient_list = {}
    cook_book = get_recipe()
    for dish in dishes:
        ingridient_list = cook_book.get(dish)
        for ingridient in ingridient_list:
            ingridient['quantity'] = int(ingridient['quantity']) * person_count
            if ingridient['ingridient_name'] not in shop_list.keys():
                shop_list[ingridient['ingridient_name']] = {'measure': ingridient['measure'], 'quantity': ingridient['quantity']}
            else:
                shop_list[ingridient['ingridient_name']]['quantity'] = shop_list[ingridient['ingridient_name']]['quantity'] + ingridient['quantity']
    return shop_list

print(get_recipe())
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

