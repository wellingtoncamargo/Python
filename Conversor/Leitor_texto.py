# -*- coding: utf-8 -*-

import pyperclip


search = 'Authorization:'
arq = input("Selecione o arquivo: ")

with open(arq,'r') as f:
    texto = f.readlines()
    for i in texto:
        if search in i:
            t = i.rsplit(search)
            a = t[1].replace(']','')
            b = a.replace(' Bearer', 'Bearer')
            pyperclip.copy(b)


