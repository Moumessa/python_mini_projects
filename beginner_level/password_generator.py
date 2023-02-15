import random
import string

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

    if use_numbers:
        digits_length = random.randint(1,length-2) #1-12 => 3
    else:
        digits_length = 0

    if use_special_characters:
        special_chars_length = random.randint(1,length-2-digits_length) #1-9 => 5
    else:
        special_chars_length = 0

    letters_length = length-digits_length-special_chars_length #1-6 => 3

    print("lengths : letters :", letters_length,"digits:", digits_length, 'special:', special_chars_length)

    random_digits = ""
    random_special_chars = ""
    random_letters = "".join(random.sample(letters, letters_length))

    if use_numbers:
        random_digits= "".join(random.sample(digits, digits_length))

    if use_special_characters:
        random_special_chars="".join(random.sample(special_chars, special_chars_length))

    password = random_letters+random_digits+random_special_chars

    print("password : ", password)

    # # print("rendom samples : letters :", random_letters,"digits:", random_digits, 'special:', random_special_chars)
    # random.shuffle(password)

    # return password

    # chars = letters

    # if use_numbers:
    #     chars+=digits

    # if use_special_characters:
    #     chars +=special_chars

    # return "".join(random.sample(chars, length))

    # if numbers :
    #     if special_characters :
    #         return "".join(random.sample(letters+digits+special_chars, length))
    #     else:
    #         return "".join(random.sample(letters+digits, length))
    # else:
    #     if special_characters :
    #         return "".join(random.sample(letters+special_chars, length))
    #     else:
    #         return "".join(random.sample(letters, length))

print(generate_password(10,15))



def partition(number):
    answer = set()
    answer.add((number, ))
    for x in range(1, number):
        for y in partition(number - x):
            answer.add(tuple(sorted((x, ) + y)))
    return answer


# print(partition(10))
