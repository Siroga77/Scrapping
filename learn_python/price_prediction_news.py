import requests
from bs4 import BeautifulSoup
from colorama import init, Fore


headers = {'User-Agent': 'Mozilla/5.0'}

url = 'https://priceprediction.net/ru'

init()
lst = []

try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN + "\nSuccessfully connected!", response, "\n")
        soup = BeautifulSoup(response.text, 'lxml')
        news = soup.find('div', class_='ui grid').find_all('div', class_='col-md-12')

        count = 1
        for row in news:
            print(Fore.CYAN + f'{count}: {row.text.strip()}')
            lst.append(row.text.strip())
            links = soup.find_all('a', class_='catg_title')
            link = links[count].get('href')
            count += 1

            print(link)
            print("-" * 70)

        # with open('links.html', 'w', encoding='UTF-8') as f:
        #     for item in lst:
        #         f.write(item+"<br>")

        print(Fore.GREEN, f'Total news rows: {count}\n')
        print(lst)

    else:
        print("Please reconnect!")

except ConnectionError:
    print("Failed!")

finally:
    print(Fore.RED + '\nDisconnected!')
