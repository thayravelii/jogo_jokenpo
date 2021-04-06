import random
from time import sleep
from emoji import emojize

dicionario = {'R': 'ROCK', 'P': 'PAPER', 'S': 'SCISSORS'}
lista = ['R', 'P', 'S']
score_maquina = 0
score_jogador = 0
continuar = 'C'
escolha_maquina = dicionario[lista[random.randint(0, 2)]].upper().strip()[0]


def showResult(result, score):
    if result == 0:
        print('EMPATE!')
    elif result == 1:
        print('GANHOU!')
        score = score + 1
    elif result == 2:
        print('PERDEU!')
        score = score + 1
    return score

def showPlacar():
    print('===============Placar===============')
    print('Jogador:{}'.format(score_jogador))
    print('Máquina:{}'.format(score_maquina))
    print('='*36)
  

while continuar == 'C':
    print('='*40)
    print(emojize('''Para começar, escolha sua jogada:
        [R]ROCK :fist:
        [P]PAPER :hand:
        [S]SCISSORS :v:''', use_aliases=True))
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
    print('A jogada do seu adversario foi: {}'.format(
        dicionario[escolha_maquina]))
    print('Sua jogada:{}'.format(dicionario[jogador]))
#PEDRA
    if jogador == "R":
        if escolha_maquina == "R":   
            showResult(0, 0)
            showPlacar()
        elif escolha_maquina == "P":

            score_maquina = showResult(2, score_maquina)
            showPlacar()

        elif escolha_maquina == "S":
            
            score_jogador = showResult(1, score_jogador)
            showPlacar()
#PAPEL
    elif jogador == "P":
        if escolha_maquina == "R":

            score_jogador = showResult(1, score_jogador)
            showPlacar()

        elif escolha_maquina == "P":
            showResult(0, 0)    
            showPlacar()

        elif escolha_maquina == "S":
            score_maquina = showResult(2, score_maquina)
            showPlacar()
#TESOURA
    elif jogador == "S":
        if escolha_maquina == "R":

            score_maquina = showResult(2, score_maquina)
            showPlacar()

        elif escolha_maquina == "P":
            score_jogador = showResult(1, score_jogador)
            showPlacar()

        elif escolha_maquina == "S":
            showResult(0, 0)
            showPlacar()
    

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
