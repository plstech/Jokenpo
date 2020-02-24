#!/usr/bin/env python3

import os
import random

escolha = int(input('\n                    '+'\033[1;31m'+'  ✌ '+'\033[1;36m'+'[-   jokenpô  じゃんけんぽん      -]'+'✌  '+'\n'+'\033[1;97m'+'\n1-Jogar'+'\n2-Sair'+'\033[1;36m'+'\n\nEscolha: '))

def main(): # Começo
    maquina = random.choice(["Pedra", "Papel", "Tesoura"]) # Maquina escolhe aleatoriamente entre os 3


    if escolha == 1:  # Se a escolha for igual a 1 Inicia o game
            os.system('clear')
            x = str(input('************************************************\nOBS:Colocar da forma que está escrito abaixo.\n************************************************\n\n\033[1;36m'+'----------------------------------------'+"\nPedra, Papel ou Tesoura?\n"+'----------------------------------------'+'\033[1;31m'+'\n\nEscolha: '))


    elif escolha == 2: # Se a escolha for igual a 2, limpa a tela e fecha.
        os.system('clear')
        exit(0)
#
# Papel
#
    if x == 'Papel' and maquina == 'Pedra':
            os.system('clear')
            print('\033[1;97m'+'----------------------------------------')
            print('\033[1;36m'+'Papel embrulha Pedra, Você ganhou!')
            print('\033[1;97m'+'----------------------------------------')
            os.system('sleep 3')
            main()


    elif x == 'Papel' and maquina == 'Tesoura':
        os.system('clear')
        print('\033[1;97m'+'----------------------------------------')
        print('\033[1;31m'+'Tesoura corta Papel, Você perdeu.')
        print('\033[1;97m'+'----------------------------------------')
        os.system('sleep 3')
        main()


    elif x == 'Papel' and maquina == 'Papel':
        os.system('clear')
        print('\033[1;97m'+'----------------------------------------')
        print('\033[1;33m'+'Os dois colocaram Papel, Deu empate.')
        print('\033[1;97m'+'----------------------------------------')
        os.system('sleep 3')
        main()


#
# Tesoura
#
    if x == 'Tesoura' and maquina == 'Papel':
            os.system('clear')
            print('\033[1;97m'+'----------------------------------------')
            print('\033[1;36m'+'Tesoura corta Papel, Você ganhou!')
            print('\033[1;97m'+'----------------------------------------')
            os.system('sleep 3')
            main()


    elif x == 'Tesoura' and maquina == 'Pedra':
        os.system('clear')
        print('\033[1;97m'+'----------------------------------------')
        print('\033[1;31m'+'Pedra quebra Tesoura, Você perdeu.')
        print('\033[1;97m'+'----------------------------------------')
        os.system('sleep 3')
        main()


    elif x == 'Tesoura' and maquina == 'Tesoura':
        os.system('clear')
        print('\033[1;97m'+'----------------------------------------')
        print('\033[1;33m'+'Os dois colocaram Tesoura, Deu empate.')
        print('\033[1;97m'+'----------------------------------------')
        os.system('sleep 3')
        main()
#
# Pedra
#

    if x == 'Pedra' and maquina == 'Tesoura':
            os.system('clear')
            print('\033[1;97m'+'----------------------------------------')
            print('\033[1;36m'+'Pedra quebra Tesoura, Você ganhou!')
            print('\033[1;97m'+'----------------------------------------')
            os.system('sleep 3')
            main()


    elif x == 'Pedra' and maquina == 'Papel':
        os.system('clear')
        print('\033[1;97m'+'----------------------------------------')
        print('\033[1;31m'+'Papel embrulha Pedra, Você perdeu.')
        print('\033[1;97m'+'----------------------------------------')
        os.system('sleep 3')
        main()


    elif x == 'Pedra' and maquina == 'Pedra':
        os.system('clear')
        print('\033[1;97m'+'----------------------------------------')
        print('\033[1;33m'+'Os dois colocaram Pedra, Deu empate.')
        print('\033[1;97m'+'----------------------------------------')
        os.system('sleep 3')
        main()
main()
