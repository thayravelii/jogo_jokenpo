import random
from time import sleep
from emoji import emojize

dicionario = {'R': 'ROCK', 'P': 'PAPER', 'S': 'SCISSORS'}
lista = ['R', 'P', 'S']
score_maquina = 0
score_jogador = 0
jogar = 'C'
maquina = dicionario[lista[random.randint(0, 2)]].upper().strip()[0]

while jogar == 'C':
    print('='*40)
    print(emojize('''Para começar, escolha sua jogada:
        [R]ROCK :fist:
        [P]PAPER :hand:
        [S]SCISSORS :v:''', use_aliases= True))
    print('='*40)
    jogador = input('Qual é a sua jogada?').upper().strip()[0]
    print('='*40)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ...')
    sleep(1)
    print('='*40)
    print('A jogada do seu adversario foi: {}'.format(dicionario[maquina]))
    print('Sua jogada:{}'.format(dicionario[jogador]))

    if jogador == "R":
        if maquina == "R":
            print('EMPATE!')
            print('===============Placar===============')
            print('Jogador:{}'.format(score_jogador))
            print('Máquina:{}'.format(score_maquina))
            print('='*36)
        elif maquina == "P":
            print('VOCÊ GANHOU!')
            score_jogador = score_jogador + 1
            print('===============Placar===============')
            print('Jogador:{}'.format(score_jogador))
            print('Máquina:{}'.format(score_maquina))
            print('='*36)
        elif maquina == "S":
            print('VOCÊ PERDEU!')
            score_maquina = score_maquina + 1
            print('===============Placar===============')
            print('Jogador:{}'.format(score_jogador))
            print('Máquina:{}'.format(score_maquina))
            print('='*36)

    elif jogador == "P":
        if maquina == "R":
            print('VOCÊ GANHOU!')
            score_jogador = score_jogador + 1
            print('===============Placar===============')
            print('Jogador:{}'.format(score_jogador))
            print('Máquina:{}'.format(score_maquina))
            print('='*36)
        elif maquina == "P":
            print("EMPATE!")
            print('===============Placar===============')
            print('Jogador:{}'.format(score_jogador))
            print('Máquina:{}'.format(score_maquina))
            print('='*36)
        elif maquina == "S":
            print('VOCÊ PERDEU!')
            score_maquina = score_maquina + 1
            print('===============Placar===============')
            print('Jogador:{}'.format(score_jogador))
            print('Máquina:{}'.format(score_maquina))
            print('='*36)
    elif jogador == "S":
        if maquina == "R":
            print("VOCÊ PERDEU!")
            score_maquina = score_maquina + 1
            print('===============Placar===============')
            print("Jogador:{}".format(score_jogador))
            print("Máquina:{}".format(score_maquina))
            print('='*36)
        elif maquina == "P":
            print("VOCÊ GANHOU!")
            score_jogador = score_jogador + 1
            print('===============Placar===============')
            print("Jogador:{}".format(score_jogador))
            print("Máquina:{}".format(score_maquina))
            print('='*36)
        elif maquina == "S":
            print("EMPATE!")
            print('===============Placar===============')
            print("Jogador:{}".format(score_jogador))
            print("Máquina:{}".format(score_maquina))
            print('='*36)

    print('===============FIM DA RODADA===============')
    jogar = input('''
    [C] CONTINUE
    [S] STOP
    DESEJA CONTINUAR JOGANDO?''').upper().strip()[0]
    print('='*30)
    
    if jogar == "S":
        print('FIM DE JOGO!!!')
        print('===============PLACAR FINAL===============')
        print('Jogador:{}'.format(score_jogador))
        print('Maquina:{}'.format(score_maquina))
        print('='*40)