import platform  # For getting the operating system name
import subprocess  # For executing a shell command
from Private import slack_app, stores_sensitive_info


class Store:
    def __init__(self, name, area, ip):
        self.name = name
        self.area = area
        self.ip = ip
        self.ping = 'ΑΓΝΩΣΤΟ'

    def check_internet_status(self):
        command = ['ping', '-c', '1', self.ip]
        if subprocess.call(command) == 0:
            self.ping = 'ONLINE'
        else:
            self.ping = 'OFFLINE'
        return f'ΚΑΤΑΣΤΗΜΑ: {self.name} || ΠΕΡΙΟΧΗ: {self.area} || ΚΑΤΑΣΤΑΣΗ: {self.ping} \n'


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

# ----------------SLACK BOT----------------------------
output = f"""
ΕΛΕΓΧΟΣ INTERNET ΣΤΑ ΚΑΤΑΣΤΗΜΑΤΑ
{ELOUNDA_MARKET.check_internet_status()}
{LATO_01.check_internet_status()}
{LATO_02.check_internet_status()}
"""
slack_app.post_message_to_slack(output)
