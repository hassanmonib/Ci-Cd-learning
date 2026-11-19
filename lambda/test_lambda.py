
import unittest
from unittest.mock import patch

with patch("boto3.client"):
    from lambda_function import calculate_bonus


class TestEmployeeBonus(unittest.TestCase):

    def test_annual_bonus(self):
        self.assertEqual(calculate_bonus(75000), 7500)

    def test_another_salary(self):
        self.assertEqual(calculate_bonus(90000), 9000)


if __name__ == "__main__":
    unittest.main()
