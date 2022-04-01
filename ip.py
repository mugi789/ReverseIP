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
web = input(' Enter URL : ')
head = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0'
    }
payload = {
    'remoteAddress': web,
    'key': ''
}
rek = requests.post('https://domains.yougetsignal.com/domains.php', headers=head, data=payload)
total = json.dumps(json.loads(rek.text)['domainCount'])
list = json.dumps(json.loads(rek.text)['domainArray']).replace('[["', '').replace('", ""]]', '').replace('", ""], ["', '\r').replace('", "1"], ["', '\r').split()
print(" "+"="*15+" Result "+"="*15)
for domain in list:
    print(" "+domain)
print(" "+"="*38)
print(" "+"Total : \033[33m"+total.replace('"', '')+"\033[0m")