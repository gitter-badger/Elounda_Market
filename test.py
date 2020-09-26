#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import time
text = ' Start Hacking FBI Server '

for i in range(len(text)):
    print(f'\r {text[:i]}', end="")
    time.sleep(.3)
print()
for counter in range(100):
    percent = int((100 * (counter + 1)) / 100)
    filler = "█" * (percent)
    remaining = '-' * (100 - percent)
    print(f'\rHACKING FBI:[{filler}{remaining}]{percent}% ', end='', flush=True)
    time.sleep(.1)
print('\nFBI SUCCESSFULLY HACKED')
