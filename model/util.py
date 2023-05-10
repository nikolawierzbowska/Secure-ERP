import random


def generate_id():
    number_of_special_chars = ["_", "+", "-", "!"]
    small_letters_list = [chr(random.randint(97, 122)) for _ in range(4)]
    capital_letters_list = [chr(random.randint(65, 90)) for _ in range(2)]
    digits_list = [str(random.randint(0, 10)) for _ in range(2)]
    special_chars_list = [str(random.choice(number_of_special_chars)) for _ in range(2)]
    list_of_elements = small_letters_list + capital_letters_list + digits_list + special_chars_list
    shuffled_list = random.sample(list_of_elements, len(list_of_elements))
    generated_id = "".join(shuffled_list)
    return generated_id

