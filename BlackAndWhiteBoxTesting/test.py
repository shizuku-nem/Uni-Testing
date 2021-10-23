import unittest
dict_price = {
        1: 30000,
        2: 40000
    }
def count_money(type, number):
    price = dict_price[type]
    if number < 2:
        return price
    elif number >= 2:
        return price * number * 0.75
    elif number >= 4:
        return price * number * 0.5

class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertEqual(count_money(1, 1), 30000)

    def test2(self):
        self.assertEqual(count_money(1, 2), 45000)

    def test3(self):
        self.assertEqual(count_money(1, 5), 75000)

    def test4(self):
        self.assertEqual(count_money(1, 9), 135000)

    def test5(self):
        self.assertEqual(count_money(1, 10), 150000)

    def test6(self):
        self.assertEqual(count_money(2, 1), 40000)

    def test7(self):
        self.assertEqual(count_money(2, 2), 60000)

    def test8(self):
        self.assertEqual(count_money(2, 5), 100000)

    def test9(self):
        self.assertEqual(count_money(2, 9), 180000)

    def test10(self):
        self.assertEqual(count_money(2, 10), 200000)

    def test_r1(self):
        self.assertEqual(count_money(1, 1), 30000)

    def test_r2(self):
        self.assertEqual(count_money(1, 2), 45000)

    def test_r3(self):
        self.assertEqual(count_money(1, 5), 75000)

    def test_r4(self):
        self.assertEqual(count_money(2, 1), 40000)

    def test_r5(self):
        self.assertEqual(count_money(2, 2), 60000)

    def test_r6(self):
        self.assertEqual(count_money(2, 5), 100000) 

    def test_whitebox_1(self):
        self.assertEqual(count_money(1, 1), 30000)

    def test_whitebox_2(self):
        self.assertEqual(count_money(1, 2), 45000)

    def test_whitebox_3(self):
        self.assertEqual(count_money(1, 4), 60000)

if __name__ == '__main__':
    unittest.main(verbosity=2)