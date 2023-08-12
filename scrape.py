import time

from bs4 import BeautifulSoup
import requests
import re
import numpy as np
from collections import Counter
# https://megogo.net/ua/search-extended?category_id=16&country_id=ua&main_tab=filters&sort=rating_imdb&video_genre_id=comedy

# class Scrape:
#     def __init__(self, url):
#         self.url = url
#
#     def soup_(self):
#         response = requests.get(url=self.url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         return soup

def find_top(video_genre_id = None, ua=False):
    try:
        country = '&country_id=ua' if ua == True else ''
        video_genre = f"&video_genre_id={video_genre_id}" if video_genre_id != None else ''
        url = f'https://megogo.net/en/search-extended?main_tab=filters{country}&sort=rating_imdb{video_genre}'
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text, 'html.parser')

        movies = [str(name).replace('\n','') for name in soup.find('div', class_="cards-content").find_all('h3')]
        movies = np.unique(np.array([re.search(">(.+)\\(", name).group(1)[1:-1].strip() if '(' in name
                  else re.search(">(.+)<", name).group(1)[1:-1].strip()
                  for name in movies]))
        return list(movies)
    except Exception as e:
        print(e)


# re.search("<h3.+>(.+)</h3>",str(name)).group(0)

