import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> []:
    random_digits=[]
    try:
        if min>= 1 \
            and max<=1000 \
            and min<quantity<max:
            while len(random_digits)<quantity:
                random_digit=random.randint(min, max)
                if random_digit not in random_digits:
                    random_digits.append(random_digit)
            random_digits.sort()
    except TypeError:
        error_message()
    finally:
        error_message()
    return random_digits

def error_message():
    print("Please use three integer arguments: min, max, quantity:")
    print(" - 1 <= min < max")
    print(" - min < max <= 1000")
    print(" - min < quantity < max")
