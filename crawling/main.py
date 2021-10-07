import random
import re

import requests
from bs4 import BeautifulSoup

log_file = open('pages_log.txt', 'a', encoding='utf-8')
content_folder = './pages_content'


def scrapeWikiArticle(url, current_pages, n_pages):
    if current_pages >= n_pages:
        return
    response = requests.get(
        url=url,
    )

    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id="firstHeading")
    print(f"{current_pages}-{title.text}", file=log_file)
    print(f"{current_pages}th page requested: {title.text}")

    page_text = ''
    for paragraph in soup.find_all('p'):
        page_text += paragraph.text
    page_text = re.sub(r'\[.*?\]+', '', page_text)
    page_text = page_text.replace('\n', '')

    with open(f"{content_folder}/{current_pages}.txt", 'w', encoding='utf-8') as file_content:
        file_content.write(page_text)
        print('\tPage content saved')

    allLinks = soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)
    linkToScrape = None

    for link in allLinks:
        slug = link['href']
        if link['href'].find("/wiki/") != -1 and 'Categoría:Wikipedia' not in slug and 'Archivo' not in slug:
            linkToScrape = link
            break

    if linkToScrape is None:
        print('No link founded')
        return
    print('\tNext Selected link: ', linkToScrape['href'])
    scrapeWikiArticle("https://es.wikipedia.org" +
                      linkToScrape['href'], current_pages+1, n_pages)


scrapeWikiArticle(
    "https://es.wikipedia.org/wiki/Virgen_Blanca", 13, 20)
