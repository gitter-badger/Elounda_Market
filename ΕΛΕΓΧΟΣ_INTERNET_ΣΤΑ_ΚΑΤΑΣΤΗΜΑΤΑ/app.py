import platform  # For getting the operating system name
import subprocess  # For executing a shell command
from Private import slack_app, stores_sensitive_info


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0


class Store:
    def __init__(self, name, area, ip):
        self.name = name
        self.area = area
        self.ip = ip

    def check_internet_status(self):
        if ping(self.ip):
            return f'ΚΑΤΑΣΤΗΜΑ: {self.name} || ΠΕΡΙΟΧΗ: {self.area} || ΚΑΤΑΣΤΑΣΗ: OK \n'
        return f'ΚΑΤΑΣΤΗΜΑ: {self.name} || ΠΕΡΙΟΧΗ: {self.area} || ΚΑΤΑΣΤΑΣΗ: ERROR \n'


ELOUNDA_MARKET = Store(name='Elounda Market',
                       area='Ελούντα',
                       ip= stores_sensitive_info.ip['Elounda Market']
                       )

LATO_01 = Store(name= 'Lato 01',
                area= 'Αγ. Νικόλαος',
                ip= stores_sensitive_info.ip['Lato 01']
                )

LATO_02 = Store(name= 'Lato 02',
                area= 'Αγ. Νικόλαος',
                ip= stores_sensitive_info.ip['Lato 02']
                )
output = f"""

ΕΛΕΓΧΟΣ INTERNET ΣΤΑ ΚΑΤΑΣΤΗΜΑΤΑ
{ELOUNDA_MARKET.check_internet_status()}
{LATO_01.check_internet_status()}
{LATO_02.check_internet_status()}
"""
slack_app.post_message_to_slack(output)
