import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
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

    if numbers:
        chars+=digits

    if special_chars:
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
