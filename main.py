from pprint import pprint

# Задание №1

cook_book = {}
with open('file.txt', encoding='utf-8') as file:
    for line in file:
        name = line.strip()
        counter = int(file.readline())
        dish = []
        for ingredients in range(counter):
            ingred_dict = {}
            ing = file.readline().split('|')
            ingred_dict['ingredient_name'] = ing[0].strip()
            ingred_dict['quantity'] = ing[1].strip()
            ingred_dict['measure'] = ing[2].strip()
            dish.append(ingred_dict)
        file.readline()
        cook_book[name] = dish
pprint(cook_book)



# Задание №2

def get_shop_list_by_dishes(dishes,person_count):
    cooking_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] not in cooking_list:
                    val = {'quantity': int(ingredient['quantity'])*person_count, 'measure': ingredient['measure']}
                    cooking_list[ingredient['ingredient_name']] = val
                else:
                    cooking_list[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity'])*person_count
    return cooking_list

print(get_shop_list_by_dishes(['Омлет','Омлет','Запеченный картофель'], 2))




# Задание №3

def add_two_files(files1, files2):
    cook_book1= {}
    cook_book2 = {}
    date = 0
    data = 0
    with open(files1, encoding='utf-8') as file:
        s = []
        for line in file:
            date += 1
            s.append(line.strip())
            cook_book1[files1] = s
    with open(files2, encoding='utf-8') as file:
        b = []
        for line in file:
            data += 1
            b.append(line.strip())
            cook_book2[files2] = b
        if data > date:
            with open('file3.txt', 'w', encoding='utf-8') as file3:
                for name,line in cook_book1.items():
                    file3.write(f'{name.strip()} \n {date} \n')
                    for lin in line:
                        a = lin
                        file3.write(f'{a} \n')
                for name,line in cook_book2.items():
                    file3.write(f'{name.strip()} \n {data} \n')
                    for lin in line:
                        a = lin
                        file3.write(f'{a} \n')
        else:
            with open('file3.txt', 'w', encoding='utf-8') as file3:
                for name, line in cook_book2.items():
                    file3.write(f'{name.strip()} \n {data} \n')
                    for lin in line:
                        a = lin
                        file3.write(f'{a} \n')
                for name, line in cook_book1.items():
                    file3.write(f'{name.strip()} \n {date} \n')
                    for lin in line:
                        a = lin
                        file3.write(f'{a} \n')


# Для проверки задания №3
add_two_files('1.txt', '2.txt')
with open('file3.txt', encoding='utf-8') as file:
    a = file.read()
    print(a)










