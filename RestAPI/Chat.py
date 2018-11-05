# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot2 = ChatBot('Senior')

conv2 = ['oi',
         'ola',
         'ola, tudo bem?',
         'sim e voce',
         'qual o seu nome?',
         'meu nome é Chat, e o seu?',
         'Você dorme com as portas do seu armário aberta ou fechada?',
         'Você leva embora os shampoos e condicionadores dos hotéis?',
         'Você dorme com seu edredom dobrado pra dentro ou pra fora?',
         'Você já roubou uma placa de rua?',
         'Você gosta de usar post-it?',
         'Você corta cupons, mas depois nunca usa?',
         'Você prefere ser atacado por um urso ou um enxame de abelhas?',
         'Você tem sardas?',
         'Você sempre sorri para fotos?',
         'Qual é a sua maior neura?',
         'Você já contou seus passos enquanto você andava?',
         'Você já fez xixi na floresta?',
         'E quanto fazer coco na floresta?',
         'Você dança, mesmo se não tiver música?',
         'Você mastiga suas canetas e lápis?',
         'Com quantas pessoas você já dormiu essa semana?',
         'Qual é o tamanho da sua cama?',
         'Qual é a música da semana?',
         'O que você acha de homens que usam rosa?',
         'Você ainda assiste desenhos animados?',
         'Qual é o filme que você menos gosta?',
         'Onde você enterraria um tesouro escondido, se você teve algum?',
         'O que você bebe com o jantar?',
         'No que você mergulha um nugget de frango?',
         'Qual é a sua comida favorita?',
         'Quais filmes você poderia assistir várias vezes e continuar amando?',
         'Última pessoa que você beijou/beijou você?',
         'Alguma vez você já foi escoteiro(a)?',
         'Você posararia nua em uma revista?',
         'Quando foi a última vez que você escreveu uma carta para alguém no papel?',
         'Você pode trocar o óleo de um carro?',
         'Já obteve uma multa?',
         'Alguma vez ficou sem gasolina?',
         'Tipo favorito de sanduíche?',
         'A melhor coisa para comer no café da manhã?',
         'Qual é a sua hora de dormir?',
         'Você é preguiçoso?',
         'Quando você era criança, o que você vestia para o Dia das Bruxas?',
         'Qual é o seu signo astrológico chinês?',
         'Quantos idiomas você fala?',
         'Você tem alguma assinatura de revista?',
         'Quais são melhores, Lego ou Logs Lincoln?',
         'Você é teimoso(a)?',
         'Quem é melhor … Faustão ou Silvio Santos?',
         'Já assistiu alguma novela?',
         'Você tem medo de altura?',
         'Você canta no carro?',
         'Você canta no chuveiro?',
         'Você dança no carro?',
         'Alguma vez usou uma arma?',
         'A última vez que você teve um retrato tirado por um fotógrafo?',
         'Você acha que os musicais são legais?',
         'Natal é estressante?',
         'Nunca comeu um Pierogi?',
         'Tipo favorito de torta?',
         'O que você queria ser quando era criança?',
         'Você acredita em fantasmas?',
         'Já teve um sentimento de Deja-vu?',
         'Toma uma vitamina diária?',
         'Usa chinelos?',
         'Usa um roupão de banho?',
         'O que você usa para a cama?',
         'Primeiro show?',
         'Wal-Mart, Target e Kmart?',
         'Nike ou Adidas?',
         'Cheetos ou Fritos?',
         'Os amendoins ou sementes de girassol?',
         'Já ouviu falar do grupo de Tres Bien?',
         'Já teve aulas de dança?',
         'Existe uma profissão que você imagine fazer no seu futuro?',
         'Você consegue enrolar sua língua?',
         'Já ganhou um concurso de soletração?',
         'Você já chorou porque você estava feliz?',
         'Possui algum disco de vinil?',
         'E uma vitrola?',
         'Você utiliza incenso regularmente?',
         'Já se apaixonou?',
         'Quem você gostaria de ver em um show?',
         'Qual foi o último show que você viu?',
         'chá quente ou chá frio?',
         'Chá ou café?',
         'Açúcar ou adoçante?',
         'Você sabe nadar bem?',
         'Você consegue prender a respiração sem segurar seu nariz?',
         'Você é paciente?',
         'DJ ou banda, em um casamento?',
         'Já ganhou um concurso?',
         'Já fez alguma cirurgia plástica?',
         'Quais são as melhores azeitonas, pretas ou verdes?',
         'Você faz tricô ou crochê?',
         'O melhor lugar para uma lareira?',
         'Você já viajou pra fora do seu país?',
         'Que lugares pretende conhecer?',
         'Qual era a sua matéria preferida no Ensino Médio?',
         'Você esperneia até conseguir as coisas do seu jeito?',
         'Você tem filhos?',
         'Você quer ter filhos?',
         'Qual é sua cor favorita?',
         'Você sente falta de alguma coisa da sua infância?',





         ]

bot2.set_trainer(ListTrainer)
bot2.train(conv2)

while True:
    quest = input('Voce: ')
    resp = bot2.get_response(quest)

    if float(resp.confidence) > 0.5:
        print('Chat: ', resp)
    else:
        print('Chat: Desculpe, não entendi')