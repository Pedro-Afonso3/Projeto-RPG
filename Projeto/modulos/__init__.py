from main import sorte,azar,hero1
from time import sleep
from classes import Personagem,Heroi,Boss


def mestref(fala):
    print(f'Mestre fala: {fala}')
    sleep(1)

def s(tempo):
    sleep(tempo)

def dial_inicial():

    print('Mestre entra na sala de jogos...')
    s(2)

    mestref('')

    nomeplayer1 = str(input('Bem vindo jogador, por favor me fale seu nome: ')).strip().upper()
    s(1)

    mestref(f' {nomeplayer1} se prepare para sua jornada')
    s(1)

    print('Escolha sua classe:')
    s(1)

    print('1 - Guerreiro\n 2 - Mago\n 3 - Tank')

def dial_batalha():
    mestref(' Vamos começar a jornada...')
    s(3)

    mestref(' Ops, parece que temos o primeiro oponente\n')
    s(1)

    print('### Um lobo gigante apareceu ###\n')
    s(1)
    mestref('Prepare-se para a batalha!')
    s(2)

def azar_sorte():
    total = 0

    total = sorte - azar

    if total == 0:
        hero1.sorte = 1

    if total < 0:
        hero1.azar = total
    elif total > 0:
        hero1.sorte = total

def status():
    if hero1.azar == 0:
        print(f' Os status do guerreiro são: \n\n Vida - {hero1.vida}\n Mana - {hero1.mana}\n Defesa - {hero1.defesa}\n Dano - {hero1.dano}\n Sorte - {hero1.sorte}\n')
    else:
        print(f' Os status do guerreiro são: \n\n Vida - {hero1.vida}\n Mana - {hero1.mana}\n Defesa - {hero1.defesa}\n Dano - {hero1.dano}\n Azar - {hero1.azar}\n')