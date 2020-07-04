#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import datetime
import time

x = datetime.datetime.now().strftime('%H:%M:%S')

time.sleep(10)

y = datetime.timedelta(datetime.datetime.now()).strftime('%H:%M:%S')

z = x - y
print(z)