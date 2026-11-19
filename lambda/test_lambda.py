
import unittest

class TestEmployeeBonus(unittest.TestCase):

    def test_annual_bonus(self):
        salary = 75000
        annual_bonus = int(salary * 0.10)

        self.assertEqual(annual_bonus, 7500)

    def test_another_salary(self):
        salary = 90000
        annual_bonus = int(salary * 0.10)

        self.assertEqual(annual_bonus, 9000)

if __name__ == "__main__":
    unittest.main()
