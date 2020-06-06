import subprocess
import re
from Private import slack_app, stores_sensitive_info


class Store:
    def __init__(self, name, area, ip):
        self.name = name
        self.area = area
        self.ip = ip
        self.ping = 'ΑΓΝΩΣΤΟ'
        self.response_time = 'None'

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
        except subprocess.CalledProcessError:
            pass
        self.ping = ('ONLINE' if subprocess.call(command) == 0 else 'OFFLINE')


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
output = f"""
ΕΛΕΓΧΟΣ INTERNET ΣΤΑ ΚΑΤΑΣΤΗΜΑΤΑ
{ELOUNDA_MARKET}
{LATO_01}
{LATO_02}
"""
slack_app.post_message_to_slack(output)
