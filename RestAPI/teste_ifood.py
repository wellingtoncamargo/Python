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
    for nota in soup.find_all('span','movie-rating-average'):
        if nota.string.strip():
            notas.add(nota.string.strip())

    return notas


def crawl(filmes):
    vistos = set([filmes])
    n_visto = set([filmes])

    while n_visto:
        nvi = n_visto.pop()

        content = requests.get(filmes).text

        title = nota_filme(content)
        #if title in title:
               # print()
        print(nvi,title)


        for link in nome_filme(content):
            if link not in vistos:
                vistos.add(link)
                n_visto.add(link)


try:
    crawl('https://filmow.com/listas/filmes-com-melhor-avaliacao-no-filmow-l3451/')
except KeyboardInterrupt:
    print()
    print('Programa finalizado')

#s = requests.get('http://www.adorocinema.com/filmes/criticas-filmes/').text
#print(nome_filme(s))