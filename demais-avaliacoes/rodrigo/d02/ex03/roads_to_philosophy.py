import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys
import subprocess

def getFirstValidLink(soup):
    for paragraph in soup.select('.mw-parser-output > p'):
        for element in paragraph.children:
            if element.name == 'a' and element.get('href', '').startswith('/wiki/') and not element.get('class'):
                return element.get('href').replace("/wiki/","")
    return None

def getMainTitle(soup):
    title_tag = soup.find('h1', id='firstHeading')
    if title_tag:
        return title_tag.text
    return None

def getArticleContent(url):
    
    name = f"{url.replace(' ', '_').lower()}"
    base_url = f'https://en.wikipedia.org/wiki/{name}'
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.text
    return None

def installRequirements(requirements_file='requirement.txt'):

    subprocess.check_call(['pip', 'install', '-r', requirements_file])

def main(start_article):
    
    visited_articles = set()
    current_article = start_article
    count = 0

    while True:
        visited_articles.add(current_article)

        content = getArticleContent(current_article)
        if not content:
            print("It leads to a dead end !")
            break

        soup = BeautifulSoup(content, 'html.parser')
        main_title = getMainTitle(soup)
        print(f"{main_title}")

        next_link = getFirstValidLink(soup)
        if not next_link:
            print("It leads to a dead end !")
            break

        next_article = urljoin(current_article, next_link)
        if next_article in visited_articles:
            print("It leads to an infinite loop !")
            break

        if next_article == "Philosophy":
            count += 1
            print(f"{count} roads from {start_article} to Philosophy")
            break

        current_article = next_article
        count += 1

if __name__ == "__main__":
    
  #  installRequirements()
    
    text = input().strip()
    if text:
        main(text)
    else:
        print("No argument")