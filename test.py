#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

def add_ten(my_dictionary):
    print(f'printint my_dictionary as it is: {my_dictionary}')
    for key in my_dictionary.keys():
        print(f'printing key = {key}')
        print(f'my_dictionary of that key before = {my_dictionary[key]}')
        my_dictionary[key] += 10
        print(f'my_dictionary of that key after = {my_dictionary[key]}')
    return my_dictionary


print(add_ten({'first':5, 'second':2, 'third':3}))
