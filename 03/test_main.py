import unittest

from main import CustomList


class SubAddTest(unittest.TestCase):
    def setUp(self):
        self.mod_list_1 = CustomList([1, 2, 3, 4])
        self.mod_list_2 = CustomList([5, 6, 7, 8])
        self.mod_list_empty = CustomList([])
        self.list_1 = [1, 2, 3, 4]
        self.list_empty = []

    def test_result(self):
        self.assertEqual(self.mod_list_1 - self.mod_list_2, CustomList([-4, -4, -4, -4]))
        self.assertEqual(self.mod_list_1 - self.mod_list_empty, CustomList([1, 2, 3, 4]))
        self.assertEqual(self.mod_list_empty - self.mod_list_1, CustomList([-1, -2, -3, -4]))
        self.assertEqual(self.mod_list_1 + self.mod_list_2, CustomList([6, 8, 10, 12]))
        self.assertEqual(self.mod_list_1 + self.mod_list_empty, CustomList([1, 2, 3, 4]))
        self.assertEqual(self.list_empty - self.mod_list_empty, CustomList([]))
        self.assertEqual(self.list_1 + self.mod_list_1, CustomList([2, 4, 6, 8]))
        self.assertEqual(self.list_1 - self.mod_list_1, CustomList([0, 0, 0, 0]))
        self.assertEqual(self.mod_list_1 - self.list_1, CustomList([0, 0, 0, 0]))


class CompareTest(unittest.TestCase):
    def setUp(self):
        self.mod_list_1 = CustomList([1, 2, 3, 4])
        self.mod_list_2 = CustomList([5, 6, 7])
        self.list_1 = [10, -10, 3, 4]
        self.list_2 = [1, 2, 3, 4]
        self.list_3 = [10, -20, 5, -1]
        self.mod_list_empty = CustomList([])
        self.list_empty = []

    def test_result(self):
        self.assertFalse(self.mod_list_1 > self.mod_list_2)
        self.assertTrue(self.mod_list_1 == self.list_2)
        self.assertTrue(self.mod_list_1 >= self.list_2)
        self.assertTrue(self.mod_list_empty == self.list_empty)
        self.assertTrue(self.mod_list_empty > self.list_3)
        self.assertFalse(self.mod_list_2 < self.list_2)
        self.assertTrue(self.list_3 != self.mod_list_2)
        self.assertTrue(self.list_3 <= self.mod_list_1)
        self.assertTrue(self.mod_list_1 <= self.mod_list_2)
        self.assertFalse(self.list_empty > self.mod_list_1)
        self.assertFalse(self.mod_list_1 != self.list_2)
        self.assertFalse(self.mod_list_2 < self.list_3)


class Test(unittest.TestCase):
    def setUp(self):
        self.mod_list = CustomList([2, 3, 4, 5])

    def test_str(self):
        self.assertEqual(str(self.mod_list),
                         f'Элементы списка: {self.mod_list.copy()} \nСумма элементов {sum(self.mod_list)}')


if __name__ == "__main__":
    unittest.main()
