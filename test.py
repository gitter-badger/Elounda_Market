#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import time
from random import randint
import time
from random import random
from random import seed

type = "random"
card = ""

card_types = ["random"]


def prefill(t):
    # typical number of digits in credit card
    def_length = 16

    if t == card_types[0]:
        # discover card starts with 6011 and is 16 digits long
        return [4, 0, 4, 0], def_length - 4

    else:
        # this section probably not even needed here
        return [], def_length


def finalize(nums):
    check_sum = 0

    # is_even = True if (len(nums) + 1 % 2) == 0 else False

    check_offset = (len(nums) + 1) % 2

    for i, n in enumerate(nums):
        if (i + check_offset) % 2 == 0:
            n_ = n * 2
            check_sum += n_ - 9 if n_ > 9 else n_
        else:
            check_sum += n
    return nums + [10 - (check_sum % 10)]


# main body
t = type.lower()
if t not in card_types:
    print("Unknown type: '%s'" % type)
    print("Please pick one of these supported types: %s" % card_types)

else:
    initial, rem = prefill(t)
    so_far = initial + [randint(1, 9) for x in range(rem - 1)]
    card = "".join(map(str, finalize(so_far)))
    print("Card:", card)

for i in range(100):
    percent = int((100 * (i + 1)) / 100)
    filler = "█" * percent
    remaining = '-' * (100 - percent)
    print(f'\rLoading:\t{filler}{remaining}]{percent}%', end='', flush=True)
    time.sleep(.1)
