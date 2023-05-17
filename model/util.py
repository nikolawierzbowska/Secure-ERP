import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_specialchars=r"+-!"):
    chars = random.choices(string.ascii_lowercase, k=number_of_small_letters) \
            + random.choices(string.ascii_uppercase, k=number_of_capital_letters) \
            + random.choices(string.digits, k=number_of_digits) \
            + random.choices(allowed_specialchars, k=number_of_special_chars)
    random.shuffle(chars)
    return "".join(chars)
