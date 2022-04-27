import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}

sites = ['https://obozrevatel.com', 'https://segodnya.ua', 'https://korrespondent.net', 'https://censor.net.ua', 'https://tsn.ua', 'https://24tv.ua',
         'https://telegraf.com.ua', 'https://rbc.ua', 'https://bigmir.net']

sites_title = []
def parse():
    for i in range(len(sites)):
        response = requests.get(sites[i], headers=headers).text
        soup = BeautifulSoup(response, 'html.parser')
        titles = soup.find('title').text
        sites_title.append(titles)

    with open("sites_titles.html", "w+", encoding='utf-8') as f:
        for j in sites_title:
            f.write(f'{j}<br>')
    print(sites_title)

if __name__ == '__main__':
    parse()




