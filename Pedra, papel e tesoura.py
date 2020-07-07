from random import randint
from time import sleep
print("Vamos Brincar de Pedra, Papel ou Tesoura?")
jogador = int(input('''Escolha:
[1]Pedra
[2]Papel
[3]Tesoura
Digite sua escolha aqui: 
'''))
print("Processando....")
sleep(2)
maquina = randint(1, 3)
if maquina != jogador:
    if maquina == 1 and jogador == 2:
        print("Você venceu.")
    elif maquina == 2 and jogador == 1:
        print("Máquina venceu!")
    elif maquina == 2 and jogador == 3:
        print("Você venceu!")
    elif  maquina == 1 and jogador == 3:
        print("Máquina venceu!")
    elif maquina == 3 and jogador == 1:
        print(" Você venceu!")
    elif maquina == 3 and jogador == 2:
        print("Máquina venceu!")
elif maquina == jogador:
    print("Empate.")
else:
    print("Digito Inválido.") 
print("Sua escolha: {}. Máquina: {}".format(jogador, maquina))
ficha = str(input("Deseja jogar novamente?[S/N]: ")).upper()
if ficha == "S":
    c = 0
    while c < 1:
        jogador = int(input('''Escolha:
        [1]Pedra
        [2]Papel
        [3]Tesoura
        Digite sua escolha aqui: '''))
        maquina = randint(1, 3)
        if maquina != jogador:
            if maquina == 1 and jogador == 2:
                print("Você venceu.")
            elif maquina == 2 and jogador == 1:
                print("Máquina venceu!")
            elif maquina == 2 and jogador == 3:
                print("Você venceu!")
            elif  maquina == 1 and jogador == 3:
                print("Máquina venceu!")
            elif maquina == 3 and jogador == 1:
                print(" Você venceu!")
            elif maquina == 3 and jogador == 2:
                print("Máquina venceu!")
        elif maquina == jogador:
            print("Empate.")
        print("Sua escolha: {}. Máquina: {}".format(jogador, maquina))
        novamente = str(input("Deseja jogar novamente?[S/N]: ")).upper()
        if novamente == "S":
                c += 0
        elif novamente == "N":
                c += 1
    print("Finalizando....")
    sleep(3)
    print("Fim.")
            

elif ficha == "N":
    print("Fim")


         

    


