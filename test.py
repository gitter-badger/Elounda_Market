#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import time
x = range(20,0,-1)

for i in x:
    print(f'\r{i:2}', end='')
    time.sleep(1)
