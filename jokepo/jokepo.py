import mecanica
import time

while True:
    mecanica.iniciar()
    jogada = mecanica.sua_jogada()
    jogada_computador = mecanica.bot()

    print('==='*7)
    print(f'Você escolheu: {jogada}')
    print('==='*7)
    time.sleep(2)

    mecanica.jokepo()
    print('==='*7)
    print(f'O bot escolheu: {jogada_computador}')
    
    print('==='*7)
    mecanica.resultado(jogada_computador,jogada)
    print('==='*7)
    
    r = input('Tente de novamente! (s/n): ')
    print('==='*7)
    if r != 's':
        break


    



