# -*- coding: utf-8 -*-

import speech_recognition as sr
import wikipedia
import pyttsx3
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot2 = ChatBot('Senior')
tts = pyttsx3.init('sapi5')
r = sr.Recognizer()
pchaves = ['defina', 'definição', 'procure por', 'o que é', 'como é', 'quem é']
conv2 = ['oi',
         'ola',
         'ola, tudo bem?',
         'sim e voce',
         'qual o seu nome?',
         'meu nome é Chat, e o seu?']
wikipedia.set_lang('pt')


def speak(text):
    tts.say(text)
    tts.runAndWait()


def answer(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except:
        return 'Desculpe, não consegui encontrar'


def evaluate(query):
    for pchave in pchaves:
        if query.startswith(pchave):
            return query.replace(pchave, '')
    else:
        return None


with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s, duration=1)

    bot2.set_trainer(ListTrainer)
    bot2.train(conv2)
    print('Chat: Olá o que quer saber?')
    while True:
        audio = r.listen(s)

        speech = r.recognize_google(audio, language='pt')
        print('Eu:',speech)
        res = evaluate(speech)

        if res is not None:
            ans = answer(speech)
            print('Chat:',ans)
            speak(ans)
            print()

        elif True:
            resp = bot2.get_response(speech)
            print(resp)
            speak(resp)
        else:
            print('Chat: Desculpe, não entendi!')
            #speak('Desculpe, não entendi!')