import os
from os import getcwd
import pyperclip

arq = input('Selecione o arquivo: ')
os.system(f'java -DDOMAINS_EXTRACT_ACCESS_TOKEN=/digital/identity-access-management/v1 -Denvironment.name=LO -DHOST_SCHEMA=http -DHOST_NAME=localhost -DHOST_PORT=8080 -DAPI_VERSION=/digital-commerce/acquirers/security-management/v1 '
          f' -DFEATURE_SOURCE={arq} -jar {getcwd()}\experian-cucumber-runner-1.0.0.0.jar')

search = 'Authorization:'
with open(f'{getcwd()}/null\execution\execution.json','r') as f:

    texto = f.readlines()
    for i in texto:
        if search in i:
            t = i.rsplit(search)
            a = t[1].replace(']','')
            b = a.replace(' Bearer', 'Bearer')
            pyperclip.copy(b)
