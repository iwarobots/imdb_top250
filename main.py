#!/usr/bin/env python


import requests
from bs4 import BeautifulSoup


def str2(navigable_string, src_encoding=None, dst_encoding=None):
    if src_encoding is None:
        src_encoding = 'utf-8'
    if dst_encoding is None:
        dst_encoding = 'utf-8'
    return navigable_string.encode(src_encoding).decode(dst_encoding)


def download_imdb_top_250_page():
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
            movie = str2(a.string)
            movies.append(movie)
    return movies


def print_movies(movies):
    for movie in movies:
        print(movie)


def main():
    resp = download_imdb_top_250_page()
    movies = parse_page(resp)
    print_movies(movies)


if __name__ == '__main__':
    main()