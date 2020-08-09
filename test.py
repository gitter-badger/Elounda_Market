#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved


list1 = [0, 1, 2, 3, 3, 2, 3, 1, 4, 5, 4]
print(type(set(list1)))
print(max(set(list1), key = list1.count))