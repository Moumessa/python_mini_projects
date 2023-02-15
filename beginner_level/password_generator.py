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
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    print('letters :', letters)
    print('digits :', digits)
    print('special_chars :', special_chars)


    length_range = random.randint(0, 10)
    length = min_length + length_range

    m1 = random.randint(1,length_range)
    m2 = random.randint(1,length_range-m1)
    m3 = random.randint(1,length_range-m1-m2)

    print(" the ms = ", m1, m2, m3)

    print('length :', length)

    chars = letters

    if use_numbers:
        chars+=digits

    if use_special_characters:
        chars +=special_chars

    return "".join(random.sample(chars, length))

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

print(generate_password(6))



def partition(number):
    answer = set()
    answer.add((number, ))
    for x in range(1, number):
        for y in partition(number - x):
            answer.add(tuple(sorted((x, ) + y)))
    return answer


print(partition(10))
