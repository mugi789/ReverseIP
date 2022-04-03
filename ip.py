import requests
import json

# Reverse IP
# by Mugi F.
# github.com/mugi789
# 2022-04-01

print("""\
\033[31m    ▄▄▄  ▄▄▄ . ▌ ▐·▄▄▄ .▄▄▄  .▄▄ · ▄▄▄ .\033[0m▪   ▄▄▄·
\033[31m    ▀▄ █·▀▄.▀·▪█·█▌▀▄.▀·▀▄ █·▐█ ▀. ▀▄.▀·\033[0m██ ▐█ ▄█
\033[31m    ▐▀▀▄ ▐▀▀▪▄▐█▐█•▐▀▀▪▄▐▀▀▄ ▄▀▀▀█▄▐▀▀▪▄\033[0m▐█· ██▀·
\033[31m    ▐█•█▌▐█▄▄▌ ███ ▐█▄▄▌▐█•█▌▐█▄▪▐█▐█▄▄▌\033[0m▐█▌▐█▪·•
\033[31m    .▀  ▀ ▀▀▀ . ▀   ▀▀▀ .▀  ▀ ▀▀▀▀  ▀▀▀ \033[0m▀▀▀.▀   \n""")
web = input(' Enter URL / IP : ')
head = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0'
    }
payload = {
    'remoteAddress': web,
    'key': ''
}
rek = requests.post('https://domains.yougetsignal.com/domains.php', headers=head, data=payload)
total = json.dumps(json.loads(rek.text)['domainCount'])
list = json.dumps(json.loads(rek.text)['domainArray']).replace('[["', ' ').replace('", ""], ["', '\n ').replace('", ""]]', '')
print(" "+"="*15+" \033[35mResult\033[0m "+"="*15)
print(list)
print(" "+"="*38)
print(" "+"Total : \033[33m"+total.replace('"', '')+"\033[0m")
print(" "+"="*16+" \033[35mMenu\033[0m "+"="*16)
def pilihan():
        print(" 1. Save to file")
        print(" 2. Exit")
        choice = input(" >>> ")
        choice = int(choice)
        if choice == 1:
                f = open(web+".txt", "w")
                f.write(list.replace(' ', ''))
                print(" OK! File saved")
                f.close()
        elif choice == 2:
                print(" Bye")
                exit()
        else:
                print(" \033[31m Wrong input number\033[0m")
                pilihan()
pilihan()