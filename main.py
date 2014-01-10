#!/usr/bin/env python


import requests
from bs4 import BeautifulSoup


def main():
    resp = download_imdb_top_page()
    parse_page(resp)


def download_imdb_top_page():
    url = 'http://www.imdb.com/chart/top'
    return requests.get(url)


def parse_page(resp):
    soup = BeautifulSoup(resp.text)
    table = soup.find('table', {'class': 'chart'})

    movies = []
    for tr in table.find_all('tr'):
        td = tr.find('td', {'class': 'titleColumn'})
        if td is not None:
            a = td.find('a')
            movie = a.string
            movies.append(movie)
    return movies


if __name__ == '__main__':
    main()