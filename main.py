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
for item in items:
    space = item[1]
    points = item[2]
    space_points = points / space
    item.append(int(space_points))
start_points = 15 + 5  # 5 очков за ингалятор
inventory = [
    ['и', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
print(items)