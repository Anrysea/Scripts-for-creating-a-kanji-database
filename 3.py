import random


def select():
    # Базовые веса и значения для элементов с нулевым шансом встроены в функцию
    base_weights = [0, 2, 1, 0.8]
    elements_for_zero_chance_dict = {0: 0, 2: 5, 1: 10, 0.8: 15}

    # Формируем группы на основе переданных элементов
    elements = [getCountByGroupNumber(i + 1) for i in range(4)]
    groups = list(zip(base_weights, elements))

    # Если во всех группах нет элементов, возвращаем 5
    if sum(elements) == 0:
        return 5

    total_elements = sum(group[1] / elements_for_zero_chance_dict[group[0]] for group in groups[1:])
    total_weight = sum(group[0] * group[1] for group in groups[1:])

    prob_group1 = 0 if groups[0][1] == 0 else max(0, 1 - total_elements)

    choice = random.uniform(0, 1)

    if choice < prob_group1:
        return 1

    choice = random.uniform(0, total_weight)

    for group in groups[1:]:
        if choice < group[0] * group[1]:
            return groups.index(group) + 1
        choice -= group[0] * group[1]

    return 4


# Определяем вашу функцию getCountByGroupNumber
def getCountByGroupNumber(groupNumber):
    # Здесь какой-то код для определения количества элементов в группе.
    # В качестве примера, пусть функция возвращает 3 для первой группы, 0 для второй, 5 для третьей и 1 для четвертой.
    if groupNumber == 1:
        return 0
    elif groupNumber == 2:
        return 0
    elif groupNumber == 3:
        return 1
    elif groupNumber == 4:
        return 0

# Выбираем элемент из системы
print(select())
