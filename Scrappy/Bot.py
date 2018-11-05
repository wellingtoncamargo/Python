# -*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import wikipedia
import os

bot = ChatBot('Teste', read_only=True)
wikipedia.set_lang('pt')
bot.set_trainer(ListTrainer)

for arq in os.listdir('arq'):
    chats = ('Ola','Tudo bem?','Sim e voce?','Como vai seu dia?')
    bot.train(chats)

while True:
    resq = input('Você: ')
    # l = wikipedia.search(resq)
    resp = bot.get_response(resq)

    # if l:
    #     for i in l:
    #         print(wikipedia.summary(i, sentences=1))

    print('Bot: '+ str(resp))
