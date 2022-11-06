items = [
    ["в", 3, 25],  # Винтовка
    ["п", 2, 15],  # Пистолет
    ["б", 2, 15],  # Боекомплект
    ["а", 2, 20],  # Аптечка
    ["н", 1, 15],  # Нож
    ["т", 3, 20],  # Топор
    ["о", 1, 25],  # Оберег
    ["ф", 1, 15],  # Фляжка
    ["д", 1, 10],  # Антидот
    ["к", 2, 20],  # Еда
    ["р", 2, 20]   # Арбалет
]  # Список всех предметов, кроме ингалятора (по 8 варианту его нужно брать обязательно)

for item in items:  # добавляем в таблицу показатель ценности предметов
    size = item[1]
    points = item[2]
    space_points = points / size
    item.append(int(space_points))

start_points = 15 + 5  # 5 очков за ингалятор
plus_points = 0  # очки, которые мы прибавим
minus_points = 0  # очки, которые мы вычтем
inventory = [
    ['и', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
space_left = 8

while space_left > 0:  # стрёмный цикл просто для того чтобы посчитать очки и расставить буковки в инвентаре))))))))))

    max_item = [' ', 0, 0, 0]
    for item in items:  # находим предмет с максимальной ценностью и ставим его в конец списка предметов
        if item[3] > max_item[3]:
            max_item = item
    items[items.index(max_item)], items[10] = items[10], items[items.index(max_item)]

    if space_left < items[10][1]:  # проверка на то, влезет ли предмет в инвентарь
        items[10][3] = 0
        continue

    for rows in range(3):
        for columns in range(3):

            if items[10][1] == 1:  # проверяем размер предмета от 1 до 3
                if inventory[rows][columns] == ' ':  # проверяем, свободна ли текущая ячейка/следующие ячейки
                    inventory[rows][columns] = items[10][0]  # заносим буковки в инвентарь
                    space_left -= items[10][1]  # считаем оставшееся место и очки за предмет
                    plus_points += items[10][2]
                    items[10][1], items[10][2], items[10][3] = 0, 0, 0  # обнуляем свойства предмета, мы его уже положили
                else:
                    continue

            if items[10][1] == 2:  # аналогично для предметов с размером 2
                if columns < 2:
                    if inventory[rows][columns] == ' ' and inventory[rows][columns + 1] == ' ':
                        inventory[rows][columns] = items[10][0]
                        inventory[rows][columns + 1] = items[10][0]
                        space_left -= items[10][1]
                        plus_points += items[10][2]
                        items[10][1], items[10][2], items[10][3] = 0, 0, 0
                    else:
                        continue
                else:
                    break

            if items[10][1] == 3:  # аналогично для предметов с размером 3
                if columns == 0:
                    inventory[rows][columns] = items[10][0]
                    inventory[rows][columns + 1] = items[10][0]
                    space_left -= items[10][1]
                    plus_points += items[10][2]
                    items[10][1], items[10][2], items[10][3] = 0, 0, 0
                else:
                    break

for item in items:  # считаем очки оставшихся предметов
    minus_points += item[2]

points = start_points + plus_points - minus_points  # считаем итоговый счёт

for i in range(3):  # выводим ответ
    print(inventory[i])
print('\nИтоговые очки выживания: ', points)
