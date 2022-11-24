import random
import time



def bot():
    lista = ['Pedra','Papel','Tesoura']
    valor = random.choice(lista)
    return valor

def resultado(jogada_computador,jogada):
    #global cont_bot 
    #global cont_jogador 
    if jogada_computador == jogada:
        print ('Impate')

    elif (jogada_computador == 'Pedra' and jogada == 'Tesoura') or (jogada_computador == 'Papel' and jogada == 'Pedra') or (jogada_computador == 'Tesoura' and jogada == 'Papel'):
        print ('Você perdeu!!!')
        #cont_bot+=1

    elif (jogada_computador == 'Pedra' and jogada == 'Papel') or (jogada_computador == 'Tesoura' and jogada == 'Pedra') or (jogada_computador == 'Papel' and jogada == 'Tesoura'):
        print( 'Você ganhou!!')
        #cont_jogador+=1

    '''if jogada not in ('0','1','2'):
        print ('jogada invalida ')'''
    
    #return cont_bot, cont_jogador

def placar():
    print(f'| PLACAR: Jogador1 X Bot |')
    print(f'|          {cont_jogador}  X  {cont_bot}      |')

    
def iniciar():
    print('----------------------------------------')
    print('=='*4,'Pedra, Papel e Tesoura','=='*4)
    print('----------------------------------------')
    name = input('Informer seu nome: ').capitalize()
    print(f'Blz, {name}. Vamos lá!')
    print('----------------------------------------')

def sua_jogada():
    while True:
        jogadas = [
                    ("Pedra",0),
                    ("Papel",1),
                    ("Tesoura",2),
                ]
        resp = int(input('Faça sua jogada -> \n[0] - Pedra \n[1] - Papel  \n[2] - Tesoura\n'))
        if resp not in (0,1,2):
            print('----------------------------------------')
            print ('jogada invalida ')
            print('----------------------------------------')
            print('Escolha um das alternativas!')
            print('----------------------------------------')
        else:
            break
    jogada = jogadas[resp][0]
    return jogada 

def jokepo():
    fala = ['JO','KE','POO']
    for i in range(0,len(fala)):
        print(f'{fala[i]}...')
        time.sleep(1)


#==========================================