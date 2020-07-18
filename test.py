#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

a = ['loop', 'troop', 'soup', 'hello']

b = ['loop', 'troop', 'soup', 'hello']
def kommas():
    for i in a:
        print(i)
        if i in b:
            a.remove(i)
            return kommas()
    return a

print(kommas())
