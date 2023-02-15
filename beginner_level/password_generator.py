import random
import string
from more_itertools import random_permutation

def generate_password(min_length, max_length, use_numbers=True, 
                                        use_special_characters=True):
    """Generates random password of length between min_length and max_length.

    Args:
        min_length (int): the minimum length of the password
        max_length (int): the maximum length of the password
        use_numbers (bool, optional): Whether to include numbers or not. Defaults to True.
        use_special_characters (bool, optional): Whether to include special characters or not. Defaults to True.

    Returns:
        string: the generated password
    """
    assert 3<min_length<max_length

    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    print('letters :', letters)
    print('digits :', digits)
    print('special_chars :', special_chars)

    length = random.randint(min_length, max_length)

    print("length :", length)

    MIN_LETTERS_LENGTH = 2

    if use_numbers:
        digits_length = random.randint(1,min(length-MIN_LETTERS_LENGTH, len(digits))) #1-12 => 3
    else:
        digits_length = 0

    print('length digits :', digits_length)

    if use_special_characters:
        if length-2-digits_length >=1:
            special_chars_length = random.randint(1,min(length-MIN_LETTERS_LENGTH-digits_length, len(special_chars))) #1-9 => 5
        else:
            special_chars_length=1
    else:
        special_chars_length = 0

    letters_length = length-digits_length-special_chars_length #1-6 => 3

    print("lengths : letters :", letters_length,"digits:", digits_length, 'special:', special_chars_length)

    random_digits = ""
    random_special_chars = ""
    random_letters = "".join([random.choice(letters) for _ in range(letters_length)]) # random.sample(letters, letters_length)

    if use_numbers:
        random_digits= "".join([random.choice(digits) for _ in range(digits_length)]) #random.sample(digits, digits_length))

    if use_special_characters:
        random_special_chars="".join([random.choice(special_chars) for _ in range(special_chars_length)]) #random.sample(special_chars, special_chars_length))

    password = random_letters+random_digits+random_special_chars

    print("password :", password)
    # random.shuffle(password)

    return ''.join(random_permutation(password))

print(generate_password(5,10))