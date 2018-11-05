# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def nome_filme(content):

    soup = BeautifulSoup(content, 'lxml')
    nomes = set()
    for tag in soup.find_all('h3', text=True):
        if tag.string.strip():
            nomes.add(tag.string.strip())

    return nomes


def nota_filme(content):

    soup = BeautifulSoup(content, 'lxml')
    notas = set()
    for tag in soup.find('span','movie-rating-average', text=True):
        if tag.string.strip():
            notas.add(tag.string.strip())

    return notas


def crawl(filmes):
    v = set([filmes])
    n_v = set([filmes])
    content = requests.get(filmes, timeout=2).text
    while n_v:
        n_ = n_v.pop()

        for title in nota_filme(content):
            if title in title:
                print()
                print(n_,title)

        for link in nome_filme(content):
            if link not in v:
                v.add(link)
                n_v.add(link)


try:
    crawl('https://filmow.com/listas/filmes-com-melhor-avaliacao-no-filmow-l3451/')
except KeyboardInterrupt:
    print()
    print('Programa finalizado')

#s = requests.get('https://filmow.com/listas/filmes-com-melhor-avaliacao-no-filmow-l3451/').text
#print(nota_filme(s))