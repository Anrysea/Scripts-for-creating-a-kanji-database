import random

class Group:
    def __init__(self, base_weight, elements):
        self.base_weight = base_weight
        self.elements = elements

    @property
    def weight(self):
        return self.base_weight * self.elements

class System:
    def __init__(self, groups, elements_for_zero_chance_dict):
        self.groups = groups
        self.elements_for_zero_chance_dict = elements_for_zero_chance_dict

    def select(self):
        # считаем сумму всех "взвешенных" элементов в группах 2-4
        total_elements = sum(group.elements / self.elements_for_zero_chance_dict[group.base_weight]
                             for group in self.groups[1:])
        total_weight = sum(group.weight for group in self.groups[1:])

        # если нет элементов в группах 2-4, выбираем из 1-й группы
        if total_elements == 0:
            self.print_probabilities([1, 0, 0, 0])
            return 1

        # вычисляем вероятность выбора из 1-й группы
        prob_group1 = max(0, 1 - total_elements)

        # выбираем случайное число от 0 до 1
        choice = random.uniform(0, 1)

        # если число меньше вероятности выбора из 1-й группы, выбираем из 1-й группы
        if choice < prob_group1:
            self.print_probabilities([prob_group1,
                                      (1 - prob_group1) * self.groups[1].weight / total_weight,
                                      (1 - prob_group1) * self.groups[2].weight / total_weight,
                                      (1 - prob_group1) * self.groups[3].weight / total_weight])
            return 1

        # иначе выбираем из групп 2-4 с учетом их веса
        choice = random.uniform(0, total_weight)

        for group in self.groups[1:]:
            if choice < group.weight:
                self.print_probabilities([prob_group1,
                                          (1 - prob_group1) * self.groups[1].weight / total_weight,
                                          (1 - prob_group1) * self.groups[2].weight / total_weight,
                                          (1 - prob_group1) * self.groups[3].weight / total_weight])
                return self.groups.index(group) + 1
            choice -= group.weight

        self.print_probabilities([prob_group1,
                                  (1 - prob_group1) * self.groups[1].weight / total_weight,
                                  (1 - prob_group1) * self.groups[2].weight / total_weight,
                                  (1 - prob_group1) * self.groups[3].weight / total_weight])
        return 4

    def print_probabilities(self, probs):
        for i in range(4):
            print(f'Вероятность выбора группы {i+1}: {probs[i] * 100:.2f}%')


# создаем систему с 4 группами
system = System([
    Group(0, 3),  # 1-я группа имеет 3 элемента и базовый вес 0
    Group(2, 0),  # 2-я группа имеет 1 элемент и базовый вес 2
    Group(1, 5),  # 3-я группа имеет 2 элемента и базовый вес 1
    Group(0.8, 1)  # 4-я группа имеет 10 элементов и базовый вес 0.5
], {0: 0, 2: 5, 1: 10, 0.8: 15})  # элементов для нулевого шанса выбора первой группы в зависимости от веса

# выбираем элемент из системы
print(system.select())
