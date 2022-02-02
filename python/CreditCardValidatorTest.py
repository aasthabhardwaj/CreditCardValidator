import unittest
import CreditCardValidator


class TestValidator(unittest.TestCase):
    def test_validate_all(self):
        self.assertTrue(CreditCardValidator.isValid({"user_name": "Shubman Gill",
                                                         "card_number": "79927398713",
                                                         "cvv": "775",
                                                         "valid_until": "08/29"}))
        self.assertFalse(CreditCardValidator.isValid({"user_name": "Shubman Gill 77",
                                                         "card_number": "79927398711",
                                                         "cvv": "3313",
                                                         "valid_until": "01/25"}))

    def test_is_name_valid(self):
        self.assertTrue(CreditCardValidator.isNameValid("Aastha Bhardwaj"))
        self.assertFalse(CreditCardValidator.isNameValid("AasMan-0577"))

    def test_is_card_number_valid(self):
        self.assertTrue(CreditCardValidator.isCardValid("79927398713"))
        self.assertFalse(CreditCardValidator.isCardValid("79927398714"))

    def test_is_cvv_valid(self):
        self.assertTrue(CreditCardValidator.isCvvValid(123))
        self.assertTrue(CreditCardValidator.isCvvValid(1431))
        self.assertFalse(CreditCardValidator.isCvvValid(42))
        self.assertFalse(CreditCardValidator.isCvvValid(12345))

    def test_is_exp_date_valid(self):
        # self.assertTrue(credit_card_validation.is_exp_date_valid("02/21"))
        self.assertTrue(CreditCardValidator.isExpDateValid("06/23"))
        self.assertFalse(CreditCardValidator.isExpDateValid("02-21"))
        self.assertFalse(CreditCardValidator.isExpDateValid("02/20"))
        self.assertFalse(CreditCardValidator.isExpDateValid("01/21"))


if __name__ == '__main__':
    unittest.main()
