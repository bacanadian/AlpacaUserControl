from datetime import datetime
from colorama import Fore


def log(self, status):
    try:
        if status == 1:
            print(Fore.WHITE + (datetime.now().strftime('%H:%M:%S.%f')[:-3]) + Fore.GREEN + ' ' + self)  #SUCCESS
        elif status == 2:
            print(Fore.WHITE + (datetime.now().strftime('%H:%M:%S.%f')[:-3]) + Fore.RED + ' ' + self)   #FAIL
        elif status == 3:
            print(Fore.WHITE + (datetime.now().strftime('%H:%M:%S.%f')[:-3]) + Fore.CYAN + ' ' + self)
        elif status == 4:
            print(Fore.WHITE + (datetime.now().strftime('%H:%M:%S.%f')[:-3]) + Fore.LIGHTRED_EX + ' ' + self)  #Minor fail
        elif status == 5:
            print(Fore.WHITE + (datetime.now().strftime('%H:%M:%S.%f')[:-3]) + Fore.MAGENTA + ' ' + self)
        else:
            print(Fore.WHITE + (
            datetime.now().strftime('%H:%M:%S.%f')[:-3]) + Fore.RED + ' INVALID LOG FORMAT. Please check int value.')
    except:
        print(Fore.WHITE + (datetime.now().strftime('%H:%M:%S.%f')[:-3]) + Fore.RED + ' Failed to understand log call. Wrong format when calling log')  # Wrong format
