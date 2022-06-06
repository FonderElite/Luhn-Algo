import sys,time
from colorama import Fore,Back as bg 
bold_color = '\033[1m'
def show_banner(s):
    for c in s + '\n':
        sys.stdout.write(bg.BLACK + Fore.GREEN + c + Fore.WHITE)
        sys.stdout.flush()
        time.sleep(1 / 100)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("┃Made By FonderElite ┃ Github: https://github.com/FonderElite ┃")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(Fore.WHITE + "[" + Fore.GREEN + "+" + Fore.WHITE + ']'  + 'Generating Possibly Valid CCs')
    time.sleep(1)
show_banner("""
██╗     ██╗   ██╗██╗  ██╗███╗   ██╗       █████╗ ██╗      ██████╗  ██████╗ 
██║     ██║   ██║██║  ██║████╗  ██║      ██╔══██╗██║     ██╔════╝ ██╔═══██╗
██║     ██║   ██║███████║██╔██╗ ██║█████╗███████║██║     ██║  ███╗██║   ██║
██║     ██║   ██║██╔══██║██║╚██╗██║╚════╝██╔══██║██║     ██║   ██║██║   ██║
███████╗╚██████╔╝██║  ██║██║ ╚████║      ██║  ██║███████╗╚██████╔╝╚██████╔╝
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝      ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ 
""")
