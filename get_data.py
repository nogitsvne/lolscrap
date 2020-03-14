from bs4 import BeautifulSoup
import requests

print('Digite o nome do campeão que deseja saber a história (a história está em en-us):')
champ = str(input('[+] -> '))

url = f'https://lol.gamepedia.com/{champ}'

response = requests.get( url )
bs4obj = BeautifulSoup(response.text, 'lxml')

get = bs4obj.find('div', class_='content1 active')
get = get.find('tr')

resultado = get.text

print(resultado)
