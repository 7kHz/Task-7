with open('recipes.txt', 'rt', encoding='cp1251') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        dish_count = int(file.readline())
        dishes = []
        for _ in range(dish_count):
            ingr_list = file.readline().strip().split(' | ')
            ingridient, quantity, measure = ingr_list
            dishes.append({'ingridient_name': ingridient,
                           'quantity': quantity,
                           'measure': measure
                           })
        file.readline()
        cook_book[dish] = dishes

    print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    dct_dish = {}
    for dish_ in dishes:
        for values in cook_book.setdefault(dish_):
            ingridient_ = values.setdefault('ingridient_name')
            quantity_ = int(values.setdefault('quantity'))
            measure_ = values.setdefault('measure')
            dct = {'measure': measure_, 'quantity': quantity_ * person_count}
            dct_dish[ingridient_] = dct
    return dct_dish


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

