from bs4 import BeautifulSoup
from bs4 import Comment


def extract_links():

    with open('./input.txt', mode='r', encoding='utf8' ) as file:  
        raw_html = file.read()

    soup = BeautifulSoup(raw_html, features="html.parser")

    link_titles = soup.find_all('div', class_='title')

    for link in link_titles:
        yield link.parent['href']


with open('./job_links.out', mode='w', encoding='utf8') as out:

    for link in extract_links():
        out.write(link + '\n')
