#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import subprocess
import re
from Private import stores_sensitive_info
from DISCORD.INTERNET import slack


def run():
    class Store:
        def __init__(self, name, area, ip):
            self.name = name
            self.area = area
            self.ip = ip
            self.ping = 'ΑΓΝΩΣΤΟ'
            self.response_time = ''

        def __str__(self):
            return f'ΚΑΤΑΣΤΗΜΑ: {self.name} || ΠΕΡΙΟΧΗ: {self.area} || ΚΑΤΑΣΤΑΣΗ: {self.ping} || ΑΠΟΚΡΙΣΗ: {self.response_time} ms'

        def check_internet_status(self):
            command = ['ping', '-c', '4', self.ip]
            try:
                output = subprocess.check_output(command)
                output = output.decode('utf8')
                statistic = re.search(r'(\d+\.\d+/){3}\d+\.\d+', output).group(0)
                avg_time = re.findall(r'\d+\.\d+', statistic)[1]
                self.response_time = float(avg_time)
                self.ping = 'ONLINE'
            except subprocess.CalledProcessError:
                self.response_time = float('inf')
                self.ping = 'OFFLINE'

    ELOUNDA_MARKET = Store(name='Elounda Market',
                           area='Ελούντα',
                           ip=stores_sensitive_info.ip['Elounda Market']
                           )

    LATO_01 = Store(name='Lato 01',
                    area='Αγ. Νικόλαος',
                    ip=stores_sensitive_info.ip['Lato 01']
                    )

    LATO_02 = Store(name='Lato 02',
                    area='Αγ. Νικόλαος',
                    ip=stores_sensitive_info.ip['Lato 02']
                    )

    ELOUNDA_MARKET.check_internet_status()
    LATO_01.check_internet_status()
    LATO_02.check_internet_status()

    # ----------------SLACK BOT----------------------------
    slack.app(ELOUNDA_MARKET, LATO_01, LATO_02)
