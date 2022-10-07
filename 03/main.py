"""Домашнее задание #03"""


class CustomList(list):
    """Класс особого списка"""

    def __add__(self, other):
        new_mod_lst = CustomList([])
        min_len = min(len(self), len(other))
        new_mod_lst.extend([x + y for x, y in zip(self[:min_len], other[:min_len])])
        new_mod_lst.extend(self[min_len:])
        new_mod_lst.extend(other[min_len:])
        return new_mod_lst

    def __radd__(self, other):
        return self + CustomList(other)

    def __sub__(self, other):
        new_mod_lst = CustomList([])
        min_len = min(len(self), len(other))
        new_mod_lst.extend([x - y for x, y in zip(self[:min_len], other[:min_len])])
        new_mod_lst.extend(self[min_len:])
        new_mod_lst.extend([x - y for x, y in zip([0] * len(other[min_len:]), other[min_len:])])
        return new_mod_lst

    def __rsub__(self, other):
        return CustomList(other) - self

    def __str__(self):
        return f'Элементы списка: {self.copy()} \nСумма элементов {sum(self)}'

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)


if __name__ == "__main__":
    a = CustomList([1, 2, 3, 4, 5, 6])
    b = CustomList([9, 8, 7])
    print(f'Модифицированный список_1: {a}')
    print(f'Модифицированный список_2: {b}')
    print(f'Разность двух модифицированных списков: {a - b}')
    print(f'Сумма двух модифицированных списков: {a + b}')
    print(f'Сумма списка и модифицированного списка: {[1, 2, 3] + a}')
    print(f'Сумма модифицированного списка и списка: {a + [1, 2, 3]}')
    print(f'Разность списка и модифицированного списка: {[1, 2, 3, 4] - b}')
    print(f'Разность модифицированного списка и списка: {b - [1, 2, 3, 4]}')
    print(f'Сравниваем два списка: {[1, 5, 3, 2] < [20, 30, 40]}')
    print(f'Сравниваем два модифицированных списка:'
          f' {CustomList([20, 1, 3, 4]) < CustomList([2, 3, 4])}')
    print(f'Сравниваем два модифицированных списка:'
          f' {CustomList([20, 1, 3, 4]) != CustomList([2, 3, 4])}')
