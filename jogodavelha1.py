from random import randint
from time import sleep

def escolhajogador():
    posicao = int(input('Digite a posicao de 1 a 9: '))
    while True:
        if p[posicao] == 'X' or p[posicao] == 'Z':
            posicao = int(input('Posição já preenchida. Digite a posicao de 1 a 9: '))
        else:
            p[posicao] = 'X'
            break

def escolhapc():
    posicao = randint(1, 9)
    while True:    
        if p[posicao] == 'X' or p[posicao] == 'Z':
            posicao = randint(1, 9)
        else:
            p[posicao] = 'Z'
            break
        
def tabuleiro():
    print(f'''
    1|2|3          {p[1]} | {p[2]} | {p[3]}
    4|5|6          {p[4]} | {p[5]} | {p[6]}
    7|8|9          {p[7]} | {p[8]} | {p[9]}
''')

def conferevencedor():
    jogadores = [['X','jogador'], ['Z','pc']]
    pvencedor = [[1,2,3], [1,4,7], [1,5,9], [4,5,6], [7,8,9], [7,5,3], [2,5,8], [3,6,9]]
    for t, c in jogadores:
        for c1 in pvencedor:
            if p[c1[0]] == t and p[c1[1]] == t and p[c1[2]] == t:
                print(f'{c} GANHOU!')
                global jogando
                jogando = False

p = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0]
jogadas = 0
jogando = True

tabuleiro()

while jogando:
    
    escolhajogador()
    jogadas +=1
    if jogadas >= 9:
        print('Empate!')
        break
    
    tabuleiro()
    conferevencedor()
    if jogando == False:
        break
   
    escolhapc()
    print('pensando...')
    jogadas += 1
    if jogadas >= 9:
        print('Empate!')
        break
    sleep(1)
    tabuleiro()
    conferevencedor()
    if jogando == False:
        break
