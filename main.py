# cook_book = {
#   'Омлет': [
#     {'ingridient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingridient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingridient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingridient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingridient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingridient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingridient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'},
#     {'ingridient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ],
#   'Фахитос': [
#     {'ingridient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
#     {'ingridient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'},
#     {'ingridient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
#     {'ingridient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л'},
#     {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'},
#     ]
# }
#
# dishes = input('Введите блюдо ')
# person_count = input('Введите количество персон ')
#
# def get_shop_list_by_dishes(dishes, person_count):
#   for item in cook_book:
#     if number == item['number']:
#       result = 'ingridient_name: ' + item['measure'] + item['quantity']
#   print(result)


def get_cook_book():
    cook_book = {}
    with open('cook_book.txt', encoding='utf-8') as f:
        for line in f:
            key = line.strip()
            index = f.readline().strip()
            temp_list = []
            for i in range(int(index)):
                value = f.readline().strip()
                split_value = value.split(' | ')
                temp_dict = {
                    'ingridient_name': split_value[0],
                    'quantity': int(split_value[1]),
                    'measure': split_value[2]
                }
                temp_list.append(temp_dict)
            f.readline()
            cook_book[key] = temp_list
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, dishes_dict):
    shop_list = {}
    cook_book = dishes_dict
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[
                    new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']][
                    'quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print(
            f"{shop_list_item['ingridient_name']} {shop_list_item['quantity']} {shop_list_item['measure']}"
        )


def input_person_count():
    return int(input('Сколько человек?: '))


def user_input():
    dishes = input('Какие блюда  на одного человека? (через запятую):').split(
        ', ')
    return [dish.capitalize() for dish in dishes]


if __name__ == '__main__':
    print_shop_list(
        get_shop_list_by_dishes(user_input(), input_person_count(),
                                get_cook_book()))
