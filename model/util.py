from random import *
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    small_letters = "abcdefghijklmnoprstuvxyz"
    capital_letters = "ABCDEFGHIJKLMNOPRSTUVXYZ"
    digits = "0123456789"
    result = sample(small_letters, number_of_small_letters) + sample(capital_letters, number_of_capital_letters) + sample(digits, number_of_digits) + sample(allowed_special_chars, number_of_special_chars)
    shuffle(result)

    return "".join(elem for elem in result)
