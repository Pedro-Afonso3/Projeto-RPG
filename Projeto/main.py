from classes import Heroi,Boss
import random
from time import sleep
import sys

list = [1,2,3]

def mestref(fala):
    print(f'Mestre fala: {fala}')
    sleep(1)

def s(tempo):
    sleep(tempo)

def dial_inicial():
    global nomeplayer1
    print('Mestre entra na sala de jogos...')
    s(2)

    mestref('') 
    nomeplayer1 = str(input('Bem vindo jogador, por favor me fale seu nome: ')).strip().upper()
    while True:
        if nomeplayer1.isalpha():
            break
        else:
            print('Nome invalido')
            s(2)
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

    statusboss()
    s(4)

    printar()
 
    mestref('Prepare-se para a batalha!')
    s(2)

def mov_batalha():
    print('Escolha o seu movimento:')
    print('1 - Ataque normal \n 2 - Habilidade \n 3 - Fugir')
    
def azar_sorte():
    total = 0
    totalb = 0

    total = sorte - azar
    totalb = sorte - azar

    if total == 0:
        hero1.sorte = 1

    if total < 0:
        hero1.azar = total
    elif total > 0:
        hero1.sorte = total
     ########## Boss
    if totalb == 0:
        boss.sorte = 1
   
    if totalb < 0:
        boss.azar = totalb
    elif totalb > 0:
        boss.sorte = totalb

def status():
    if hero1.azar == 0:
        print(f' Os status do personagem são: \n\n Vida - {hero1.vida}\n Mana - {hero1.mana}\n Defesa - {hero1.defesa}\n Dano - {hero1.dano}\n Sorte - {hero1.sorte}\n')
        s(5)
    else:
        print(f' Os status do personagem são: \n\n Vida - {hero1.vida}\n Mana - {hero1.mana}\n Defesa - {hero1.defesa}\n Dano - {hero1.dano}\n Azar - {hero1.azar}\n')
        s(5)

def statusboss():
    if boss.azar == 0:
        print(f' Os status do personagem são: \n\n Vida - {boss.vida}\n Mana - {boss.mana}\n Defesa - {boss.defesa}\n Dano - {boss.dano}\n Sorte - {boss.sorte}\n')
        s(5)
    else:
        print(f' Os status do personagem são: \n\n Vida - {boss.vida}\n Mana - {boss.mana}\n Defesa - {boss.defesa}\n Dano - {boss.dano}\n Azar - {boss.azar}\n')
        s(5)

def rolar_dadoh():
    global random_dadoh
    total = hero1.sorte + hero1.azar
    if total == -5:
        dado = [1,1,2,2,3,3,4,4,5,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        random_dadoh = random.choice(dado)
        #pos_dadoh = dado.index(pos_dadoh)
        #random_dadoh = random_dadoh[pos_dadoh]     
    elif total == -4:
        dado = [1,1,2,2,3,3,4,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        random_dadoh = random.choice(dado)
        #pos_dadoh = dado.index(pos_dadoh)
        #random_dadoh = random_dadoh[pos_dadoh]    
    elif total == -3:
        dado = [1,1,2,2,3,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        random_dadoh = random.choice(dado)
        #pos_dadoh = dado.index(pos_dadoh)
        #random_dadoh = random_dadoh[pos_dadoh]     
    elif total == -2:
        dado = [1,1,2,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        random_dadoh = random.choice(dado)
        #pos_dadoh = dado.index(pos_dadoh)
        #random_dadoh = random_dadoh[pos_dadoh]    
    elif total == -1:
        dado = [1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        random_dadoh = random.choice(dado)
        #pos_dadoh = dado.index(pos_dadoh)
        #random_dadoh = random_dadoh[pos_dadoh]    
    elif total == 1:
        dado = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,16,17,18,19,20]
        random_dadoh = random.choice(dado)
        #pos_dadoh = dado.index(pos_dadoh)
        #random_dadoh = random_dadoh[pos_dadoh]    
    elif total == 2:
        dado = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,16,17,17,18,19,20]
        random_dadoh = random.choice(dado)
        #pos_dadoh = dado.index(pos_dadoh)
        #random_dadoh = random_dadoh[pos_dadoh]     
    elif total == 3:
        dado = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,16,17,17,18,18,19,20]
        random_dadoh = random.choice(dado)
        #pos_dadoh = dado.index(pos_dadoh)
        #random_dadoh = random_dadoh[pos_dadoh]     
    elif total == 4:
        dado = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,16,17,17,18,18,19,19,20]
        random_dadoh = random.choice(dado)
        #pos_dadoh = dado.index(pos_dadoh)
        #random_dadoh = random_dadoh[pos_dadoh]     
    elif total == 5:
        dado = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,16,17,17,18,18,19,19,20,20]
        random_dadoh = random.choice(dado)
        #pos_dadoh = dado.index(pos_dadoh)
        #random_dadoh = random_dadoh[pos_dadoh]     
          
def rolar_dadob():
    global random_dadob  
    totalb = boss.sorte + boss.azar
    if totalb == -5:
        dadob = [1,1,2,2,3,3,4,4,5,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        random_dadob = random.choice(dadob)
    elif totalb == -4:
        dadob = [1,1,2,2,3,3,4,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        random_dadob = random.choice(dadob)
    elif totalb == -3:
        dadob = [1,1,2,2,3,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        random_dadob = random.choice(dadob)
    elif totalb == -2:
        dadob = [1,1,2,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        random_dadob = random.choice(dadob)
    elif totalb == -1:
        dadob = [1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        random_dadob = random.choice(dadob)
    elif totalb == 1:
        dadob = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,16,17,18,19,20]
        random_dadob = random.choice(dadob)
    elif totalb == 2:
        dadob = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,16,17,17,18,19,20]
        random_dadob = random.choice(dadob)
    elif totalb == 3:
        dadob = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,16,17,17,18,18,19,20]
        random_dadob = random.choice(dadob)
    elif totalb == 4:
        dadob = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,16,17,17,18,18,19,19,20]
        random_dadob = random.choice(dadob)
    elif totalb == 5:
        dadob = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,16,17,17,18,18,19,19,20,20]
        random_dadob = random.choice(dadob)

def batalha_hero(herodano):
    s(2)
    if random_dadoh <= 1:
        print('Seu ataque falhou!')
        s(1)
    elif random_dadoh <= 10:
        dano1 = herodano / 2
        if random_dadob <= 1:
            boss.vida = boss.vida - (dano1 * 2)
            print(f'Seu Ataque da {dano1 * 2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob <= 10:
            boss.defesa = boss.defesa / 2
            if boss.defesa < dano1:
                boss.vida = boss.vida - (dano1 - boss.defesa)
                dano2 = dano1 - boss.defesa
                print(f'Seu Ataque da {dano2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob <= 19:
            if boss.defesa < dano1:
                boss.vida = boss.vida - (dano1 - boss.defesa)
                dano2 = dano1 - boss.defesa
                print(f'Seu Ataque da {dano2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob == 20:
            boss.defesa = boss.defesa * 2
            if boss.defesa < dano1:
                boss.vida = boss.vida - (dano1 - boss.defesa)
                dano2 = dano1 - boss.defesa
                print(f'Seu Ataque da {dano2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
    elif random_dadoh <= 19:
        dano1 = herodano 
        if random_dadob == 1:
            boss.vida = boss.vida - (dano1 * 2)
            print(f'Seu Ataque da {dano1 * 2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob <= 10:
            boss.defesa = boss.defesa / 2
            if boss.defesa < dano1:
                boss.vida = boss.vida - (dano1 - boss.defesa) 
                dano2 = dano1 - boss.defesa
                print(f'Seu Ataque da {dano2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob <= 19:
            if boss.defesa < dano1:
                boss.vida = boss.vida - (dano1 - boss.defesa)
                dano2 = dano1 - boss.defesa
                print(f'Seu Ataque da {dano2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob == 20:
            boss.defesa = boss.defesa * 2
            if boss.defesa < dano1:
                boss.vida = boss.vida - (dano1 - boss.defesa)
                dano2 = dano1 - boss.defesa
                print(f'Seu Ataque da {dano2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
    elif random_dadoh == 20:
        dano1 = herodano * 2
        if random_dadob == 1:
            boss.vida = boss.vida - (dano1 * 2)
            print(f'Seu Ataque da {dano1 * 2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob <= 10:
            boss.defesa = boss.defesa / 2
            if boss.defesa < dano1:
                boss.vida = boss.vida - (dano1 - boss.defesa) 
                dano2 = dano1 - boss.defesa
                print(f'Seu Ataque da {dano2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob <= 19:
            if boss.defesa < dano1:
                boss.vida = boss.vida - (dano1 - boss.defesa)
                dano2 = dano1 - boss.defesa
                print(f'Seu Ataque da {dano2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob == 20:
            boss.defesa = boss.defesa * 2
            if boss.defesa < dano1:
                boss.vida = boss.vida - (dano1 - boss.defesa)
                dano2 = dano1 - boss.defesa
                print(f'Seu Ataque da {dano2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)

def batalha_boss():
    if random_dadob <= 1:
        print('O ataque do lobo falhou!')
        s(1)
    elif random_dadob <= 10:
        danob = boss.dano / 2

        if random_dadoh <= 1:
            hero1.vida = hero1.vida - (danob * 2)
            print(f'O Ataque do lobo da {danob * 2} de dano')
            print(f'Seu personagem esta com {hero1.vida} de vida')
            s(1)

        elif random_dadoh <= 10:
            hero1.defesa = hero1.defesa / 2
            if hero1.defesa < danob:
                hero1.vida = hero1.vida - (danob - hero1.defesa)
                danob2 = danob - hero1.defesa
                print(f'O Ataque o lobo da {danob2} de dano')
            print(f'Seu personagem esta com {hero1.vida} de vida')
            s(1)

        elif random_dadoh <= 19:
            if hero1.defesa < danob:
                hero1.vida = hero1.vida - (danob - hero1.defesa)
                danob2 = danob - hero1.defesa
                print(f'O Ataque o lobo da {danob2} de dano')
            print(f'Seu personagem esta com {hero1.vida} de vida')
            s(1)

        elif random_dadoh == 20:
            hero1.defesa = hero1.defesa * 2
            if hero1.defesa < danob:
                hero1.vida = hero1.vida - (danob - hero1.defesa)
                danob2 = danob - hero1.defesa
                print(f'O Ataque o lobo da {danob2} de dano')
            print(f'Seu personagem esta com {hero1.vida} de vida')
            s(1)


    elif random_dadob <= 19:
        danob = boss.dano

        if random_dadoh <= 1:
            hero1.vida = hero1.vida - (danob * 2)
            print(f'Seu personagem esta com {hero1.vida} de vida')
            s(1)

        elif random_dadoh <= 10:
            hero1.defesa = hero1.defesa / 2
            if hero1.defesa < danob:
                hero1.vida = hero1.vida - (danob - hero1.defesa)
                danob2 = danob - hero1.defesa
                print(f'O Ataque o lobo da {danob2} de dano')
            print(f'O seu Personagem esta com {hero1.vida} de vida')
            s(1)

        elif random_dadoh <= 19:
            if hero1.defesa < danob:
                hero1.vida = hero1.vida - (danob - hero1.defesa)
                danob2 = danob - hero1.defesa
                print(f'O Ataque o lobo da {danob2} de dano')
            print(f'O seu Personagem esta com {hero1.vida} de vida')
            s(1)

        elif random_dadoh == 20:
            hero1.defesa = hero1.defesa * 2
            if hero1.defesa < danob:
                hero1.vida = hero1.vida - (danob - hero1.defesa)
                danob2 = danob - hero1.defesa
                print(f'O Ataque o lobo da {danob2} de dano')
            print(f'O seu Personagem esta com {hero1.vida} de vida')
            s(1)

    elif random_dadob == 20:
        danob = boss.dano * 2

        if random_dadoh <= 1:
            hero1.vida = hero1.vida - (danob * 2)
            print(f'Seu personagem esta com {hero1.vida} de vida')
            s(1)

        elif random_dadoh <= 10:
            hero1.defesa = hero1.defesa / 2
            if hero1.defesa < danob:
                hero1.vida = hero1.vida - (danob - hero1.defesa)
                danob2 = danob - hero1.defesa
                print(f'O Ataque o lobo da {danob2} de dano')
            print(f'O seu Personagem esta com {hero1.vida} de vida')
            s(1)

        elif random_dadoh <= 19:
            if hero1.defesa < danob:
                hero1.vida = hero1.vida - (danob - hero1.defesa)
                danob2 = danob - hero1.defesa
                print(f'O Ataque o lobo da {danob2} de dano')
            print(f'O seu Personagem esta com {hero1.vida} de vida')
            s(1)

        elif random_dadoh == 20:
            hero1.defesa = hero1.defesa * 2
            if hero1.defesa < danob:
                hero1.vida = hero1.vida - (danob - hero1.defesa)
                danob2 = danob - hero1.defesa
                print(f'O Ataque o lobo da {danob2} de dano')
            print(f'O seu Personagem esta com {hero1.vida} de vida')
            s(1)

def escolha_habilidade1():
    print(f'1 - Avanço / CD: {cont1} \n 2 - Giro / CD: {cont2} \n 3 - Execução / CD: {cont3}')

def escolha_habilidade2():
    print(f'1 - Bola de fogo / CD:{cont1} \n 2 - Choque do trovão / CD: {cont2} \n 3 - Meteoro de diamante / CD: {cont3}')

def escolha_habilidade3():
    print(f'1 - Golpe de escudo / CD: {cont1} \n 2 - Armadura de espinhos / CD: {cont2} \n 3 - Buff de Armadura / CD: {cont3}')

def printar():
    print('-='*40)

def caso2():
    global cont1,cont2,cont3

    if hero1.mana == 80:
        g1 = guerreiro.dano + 10
        g2 = guerreiro.dano + 6
        g3 = guerreiro.dano + 20

        escolha_habilidade1()
        printar()
    
        while True:
            y = input('Digite o numero correspondente a Habilidade:')
            print('Ou pressione 6 para voltar ao menu anterior')

            while True:
                if y.isdigit():
                    break
                else:
                    print('A opção digitada NÂO é um número!')
                    y = input('Digite o numero correspondente a Habilidade:')
                    s(1)

            y1 = int(y)

            while True:
                if y1 > 0 and y1 < 4:
                    break      
                else:
                    print('Opção Inválida!')
                    s(2)
                    y1 = input('Digite o numero correspondente a Habilidade:')
                    s(1)
          
            match y1:
                case 1:
                    if cont1 == 0:
                        batalha_hero(g1)
                        cont1 = 2
                        break
                    else:
                        print(f'A habilidade em cooldown por {cont1} rodada')

                case 2:
                    if cont2 == 0:
                        batalha_hero(g2)
                        cont2 = 3
                        break
                    else:
                        print(f'A habilidade em cooldown por {cont2} rodada')
                case 3:
                    if cont3 == 0:
                        batalha_hero(g3)
                        cont3 = 4
                        break
                    else:
                        print(f'A habilidade em cooldown por {cont3} rodada')
                case 9:
                    batalhatotal()
            
                

    if hero1.mana == 100:
        m1 = mago.dano +14
        m2 = mago.dano + 8
        m3 = mago.dano + 22
        escolha_habilidade2()
        printar()
  
        while True:
            y = input('Digite o numero correspondente a Habilidade:')
            print('Ou pressione 6 para voltar ao menu anterior')

            while True:
                if y.isdigit():
                    break
                else:
                    print('A opção digitada NÂO é um número!')
                    y = input('Digite o numero correspondente a Habilidade:')
                    s(1)

            y1 = int(y)

            while True:
                if y1 > 0 and y1 < 4:
                    break      
                else:
                    print('Opção Inválida!')
                    s(2)
                    y1 = input('Digite o numero correspondente a Habilidade:')
                    s(1)
            
            match y1:
                case 1:
                    if cont1 == 0:
                        batalha_hero(m1)
                        cont1 = 2
                        break
                    else:
                        print(f'A habilidade em cooldown por {cont1} rodada')

                case 2:
                    if cont2 == 0:
                        batalha_hero(m2)
                        cont2 = 3
                        break
                    else:
                        print(f'A habilidade em cooldown por {cont2} rodada')
                case 3:
                    if cont3 == 0:
                        batalha_hero(m3)
                        cont3 = 4
                        break
                    else:
                        print(f'A habilidade em cooldown por {cont3} rodada')
                case 6:
                    batalhatotal()

    if hero1.mana == 50:
        t1 = tank.defesa + 6
        t2 = tank.defesa - 8

        escolha_habilidade3()
        printar()

        if cont3 == 1:
            tank.defesa = tank.defesa - 20
       
        while True:
            y = input('Digite o numero correspondente a Habilidade:')
            print('Ou pressione 6 para voltar ao menu anterior')

            while True:
                if y.isdigit():
                    break
                else:
                    print('A opção digitada NÂO é um número!')
                    y = input('Digite o numero correspondente a Habilidade:')
                    s(1)

            y1 = int(y)

            while True:
                if y1 > 0 and y1 < 4:
                    break      
                else:
                    print('Opção Inválida!')
                    s(2)
                    y1 = input('Digite o numero correspondente a Habilidade:')
                    s(1)
               
            match y1:
                case 1:
                    if cont1 == 0:
                        golpe_escudo(t1)
                        cont1 = 2
                        break
                    else:
                        print(f'A habilidade em cooldown por {cont1} rodada')

                case 2:
                    if cont2 == 0:
                        armadura_espinhos(t2)
                        cont2 = 3
                        break
                    else:
                        print(f'A habilidade em cooldown por {cont2} rodada')
                case 3:
                    if cont3 == 0:
                        buff_de_armor()
                        cont3 = 6
                        break
                    else:
                        print(f'A habilidade em cooldown por {cont3} rodada')
                case 6:
                    batalhatotal()
                                       
def golpe_escudo(defesatank):
    s(2)
    if random_dadoh <= 1:
        print('Seu ataque falhou!')
        s(1)
    elif random_dadoh <= 10:
        dano1 = defesatank / 2
        if random_dadob <= 1:
            boss.vida = boss.vida - (dano1 * 2)
            print(f'Seu Ataque da {dano1 * 2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob <= 10:
            boss.defesa = boss.defesa / 2
            if boss.defesa < dano1:
                boss.vida = boss.vida - (dano1 - boss.defesa)
                dano2 = dano1 - boss.defesa
                print(f'Seu Ataque da {dano2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob <= 19:
            if boss.defesa < dano1:
                boss.vida = boss.vida - (dano1 - boss.defesa)
                dano2 = dano1 - boss.defesa
                print(f'Seu Ataque da {dano2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob == 20:
            boss.defesa = boss.defesa * 2
            if boss.defesa < dano1:
                boss.vida = boss.vida - (dano1 - boss.defesa)
                dano2 = dano1 - boss.defesa
                print(f'Seu Ataque da {dano2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
    elif random_dadoh <= 19:
        dano1 = defesatank 
        if random_dadob == 1:
            boss.vida = boss.vida - (dano1 * 2)
            print(f'Seu Ataque da {dano1 * 2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob <= 10:
            boss.defesa = boss.defesa / 2
            if boss.defesa < dano1:
                boss.vida = boss.vida - (dano1 - boss.defesa) 
                dano2 = dano1 - boss.defesa
                print(f'Seu Ataque da {dano2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob <= 19:
            if boss.defesa < dano1:
                boss.vida = boss.vida - (dano1 - boss.defesa)
                dano2 = dano1 - boss.defesa
                print(f'Seu Ataque da {dano2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob == 20:
            boss.defesa = boss.defesa * 2
            if boss.defesa < dano1:
                boss.vida = boss.vida - (dano1 - boss.defesa)
                dano2 = dano1 - boss.defesa
                print(f'Seu Ataque da {dano2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
    elif random_dadoh == 20:
        dano1 = defesatank * 2
        if random_dadob == 1:
            boss.vida = boss.vida - (dano1 * 2)
            print(f'Seu Ataque da {dano1 * 2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob <= 10:
            boss.defesa = boss.defesa / 2
            if boss.defesa < dano1:
                boss.vida = boss.vida - (dano1 - boss.defesa) 
                dano2 = dano1 - boss.defesa
                print(f'Seu Ataque da {dano2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob <= 19:
            if boss.defesa < dano1:
                boss.vida = boss.vida - (dano1 - boss.defesa)
                dano2 = dano1 - boss.defesa
                print(f'Seu Ataque da {dano2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob == 20:
            boss.defesa = boss.defesa * 2
            if boss.defesa < dano1:
                boss.vida = boss.vida - (dano1 - boss.defesa)
                dano2 = dano1 - boss.defesa
                print(f'Seu Ataque da {dano2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)

def dados_perso():
    global sorte,azar,guerreiro,mago,tank,boss
    sorte = random.randint(1,5)
    azar = random.randint(1,5)

    guerreiro = Heroi(250,80,18,14)
    mago = Heroi(160,100,10,28)
    tank = Heroi(310,50,28,12)

    boss = Boss(500,300,20,20)

def batalhatotal():
    global cont1,cont2,cont3

    while True:
        printar()
        mov_batalha()
        printar()

        if cont1 > 0:
            cont1 -= 1
        if cont2 > 0:
            cont2 -= 1
        if cont3 > 0:
            cont3 -= 1
    
        mov = input('Digite o numero correspondente a sua ação:')
        printar()

        while True:
            if mov not in list:
                print('Digite um número correspondente a classe!')
                mov = input('Digite o numero correspondente a sua ação:')
                s(1)
            else:
                break

        while True:
                if mov.isdigit():
                    break
                else:
                    print('Digite um némero válido!')
                    mov = input('Digite o numero correspondente a sua ação:')
                    s(1)

        rolar_dadoh()
        rolar_dadob()

        #print(f'Você tirou {rolar_dadoh()} no dado')

        match mov:
            case 1:
                #random_dado -> numero do dado
                if hero1.mana == 80:
                    batalha_hero(guerreiro.dano)
                if hero1.mana == 100:
                    batalha_hero(mago.dano)
                if hero1.mana == 50:
                    batalha_hero(tank.dano)
                    #tank 
                
            case 2:
                caso2()
                
            case 3:
                mestref('Escolheu o caminho mais fácil...')
                s(2)
                print('Você fugiu com sucesso!!!')
                sys.exit()  
                
        printar()
        #print(f'O oponente tirou {rolar_dadob()} no dado')
        batalha_boss()

        if boss.vida <= 1:
            mestref(f'A vida do boss foi zerada, PARABENS {nomeplayer1}')
            break
        
        if  hero1.vida <= 1:
            mestref('A sua vida foi zerada, GAME OVER!!!')
            break

def armadura_espinhos(defesatank):
    s(2)
    if random_dadoh <= 1:
        print('Seu ataque falhou!')
        s(1)
    elif random_dadoh <= 10:
        defesa = defesatank + (boss.dano / 2)
        if random_dadob <= 1:
            boss.vida = boss.vida - (defesa * 2)
            print(f'Voce causa {defesa * 2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob <= 10:
            boss.defesa = boss.defesa / 2
            if boss.defesa < defesa:
                boss.vida = boss.vida - (defesa - boss.defesa)
                defesa2 = defesa - boss.defesa
                print(f'Voce causa {defesa2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob <= 19:
            if boss.defesa < defesa:
                boss.vida = boss.vida - (defesa - boss.defesa)
                defesa2 = defesa - boss.defesa
                print(f'Voce causa {defesa2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob == 20:
            boss.defesa = boss.defesa * 2
            if boss.defesa < defesa:
                boss.vida = boss.vida - (defesa - boss.defesa)
                defesa2 = defesa - boss.defesa
                print(f'Voce causa {defesa2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
    elif random_dadoh <= 19:
        defesa = defesatank 
        if random_dadob == 1:
            boss.vida = boss.vida - (defesa * 2)
            print(f'Voce causa {defesa * 2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob <= 10:
            boss.defesa = boss.defesa / 2
            if boss.defesa < defesa:
                boss.vida = boss.vida - (defesa - boss.defesa) 
                defesa2 = defesa - boss.defesa
                print(f'Voce causa {defesa2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob <= 19:
            if boss.defesa < defesa:
                boss.vida = boss.vida - (defesa - boss.defesa)
                defesa2 = defesa - boss.defesa
                print(f'Voce causa {defesa2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob == 20:
            boss.defesa = boss.defesa * 2
            if boss.defesa < defesa:
                boss.vida = boss.vida - (defesa - boss.defesa)
                defesa2 = defesa - boss.defesa
                print(f'Voce causa {defesa2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
    elif random_dadoh == 20:
        defesa = defesatank * 2
        if random_dadob == 1:
            boss.vida = boss.vida - (defesa * 2)
            print(f'Voce causa {defesa * 2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob <= 10:
            boss.defesa = boss.defesa / 2
            if boss.defesa < defesa:
                boss.vida = boss.vida - (defesa - boss.defesa) 
                defesa2 = defesa - boss.defesa
                print(f'Voce causa {defesa2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob <= 19:
            if boss.defesa < defesa:
                boss.vida = boss.vida - (defesa - boss.defesa)
                defesa2 = defesa - boss.defesa
                print(f'Voce causa {defesa2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
        elif random_dadob == 20:
            boss.defesa = boss.defesa * 2
            if boss.defesa < defesa:
                boss.vida = boss.vida - (defesa - boss.defesa)
                defesa2 = defesa - boss.defesa
                print(f'Voce causa {defesa2} de dano')
            print(f'O boss esta com {boss.vida} de vida')
            s(1)
    
def buff_de_armor():
    s(1)
    hero1.defesa = hero1.defesa + 20
    print('A sua defesa foi aumentada em 20')
    print(f'Defesa tank: {hero1.defesa}')

dial_inicial()

x = input('Digite o numero correspondente a classe:')

while True:
    if x.isdigit():
        int(x)
        break
    else:
        print('Digite um número válido!')
        x = input('Digite o numero correspondente a classe:')
        s(1)

x1 = int(x)

while True:
    if x1 > 0 and x1 < 4:
        break      
    else:
        print('Digite um número correspondente a classe!')
        s(2)
        x1 = input('Digite o numero correspondente a classe:')
        s(1)
            
dados_perso()

printar()

match x1:
    case 1:
        print('Voce escolheu o guerreiro. Dano, vida e defesas medianas')
        hero1 = guerreiro
        azar_sorte()
        status()
        
    case 2:
        print('Voce escolheu o Mago. Dano alto, porem vida e defesas baixas')
        hero1 = mago
        azar_sorte()
        status()
        
    case 3:
        print('Voce escolheu o Tank. Vida e defesas altas, porem baixo dano')
        hero1 = tank
        azar_sorte()
        status()
        
printar()

dial_batalha()

batalhatotal()