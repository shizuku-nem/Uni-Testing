import unittest

def count_money(type, number):
    dict_price = {
        1: 30000,
        2: 40000
    }
    if number < 2:
        return dict_price[type]
    elif number >= 2:
        return dict_price[type] * number * 0.75
    elif number >= 4:
        return dict_price[type] * number * 0.5

class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertEqual(count_money(1, 1), 30000)

    def test2(self):
        self.assertEqual(count_money(1, 2), 45000)

    def test3(self):
        self.assertEqual(count_money(1, 3), 67500)

    def test4(self):
        self.assertEqual(count_money(1, 4), 60000)

    def test5(self):
        self.assertEqual(count_money(1, 5), 75000)

if __name__ == '__main__':
    unittest.main(verbosity=2)


    # class Drink():
    # name: str
    # price: int
    # type: int


    # def __init__(self,name = "", price = 0,type = 0):
    #     self.name = name
    #     self.price = price
    #     self.type = type