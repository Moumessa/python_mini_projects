import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    print('letters :', letters)
    print('digits :', digits)
    print('special_chars :', special_chars)

    length = min_length + random.randint(0, 10)

    print('length :', length)

    if numbers :
        if special_characters :
            return "".join(random.sample(letters+digits+special_chars, length))
        else:
            return "".join(random.sample(letters+digits, length))
    else:
        if special_characters :
            return "".join(random.sample(letters+special_chars, length))
        else:
            return "".join(random.sample(letters, length))

print(generate_password(6))