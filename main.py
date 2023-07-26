#!venv/Scripts/python

import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator


print("\033c")

url_base = 'https://www.gwp.ge'
url = url_base + '/ka/gadaudebeli'

user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0 GLS/95.10.3509.10'}

page = requests.get(url, headers=user_agent)
soup = BeautifulSoup(page.content, 'html.parser')

all_tables = soup.find_all('table', {'class': 'samushaoebi'})

text = list()

for table in all_tables:
    href = table.find('a')['href']

    print(url_base + href)
    page2 = requests.get(url_base + href, headers=user_agent)
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    all_news = soup2.find_all('div', {'class', 'news-details'})
    for news in all_news:
        for p in news.find_all('p'):
            text.append(p.text)


ge_text = '\n'.join(text)
print(ge_text)

for line in text:
    translated = GoogleTranslator(source='ka', target='ru').translate(line)
    print(translated)

