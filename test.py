#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import time

for i in range(60):
    percent = int((100 * (i + 1)) / len(range(60)))
    filler = "█" * percent
    remaining = '-' * (100 - percent)
    print(f'\r\tLoading:\t[{filler}{remaining}]{percent}% \t{i+1}', end='', flush=True)
    # time.sleep(.1)





