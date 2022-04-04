

print('\n' + '='*51 + '\n')
print('Seja bem vindo ao jogo da velha!')
print('Você está pronto para jogar?')
print('Se estiver, digite o comando "SIM" para prosseguir.')
print('\n' + '=' * 51 + '\n')
resp = input()
print()

while resp != 'SIM':
    print('Comando digitado incorretamente! Digite de novo.')
    resp = input()
    if resp == 'SIM':
        break

print('Vamos para o programa entao!\n')



tabela = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
def imprimir_tabela():
    print('=:'*25 + '=\n')
    print('                      1     2     3')
    print('                 A   ', tabela[0][0], ' | ', tabela[0][1], ' | ', tabela[0][2])
    print('                    -----|-----|-----')
    print('                 B   ', tabela[1][0], ' | ', tabela[1][1], ' | ', tabela[1][2])
    print('                    -----|-----|-----')
    print('                 C   ', tabela[2][0], ' | ', tabela[2][1], ' | ', tabela[2][2], '\n')


    

def converte_entrada_em_posicao():

    if jogador == 1:
        entrada = str(input('Vez do Jogador 1! Digite a posicao: '))
    elif jogador == 2:
        entrada = str(input('Vez do Jogador 2! Digite a posicao: '))
    
    posicao_linha = []
    for caractere in entrada:
        posicao_linha.append(caractere)

    posicao_coluna = int(posicao_linha[0]) - 1

    if posicao_linha[1] == 'A':
        posicao_linha[1] = 0
    elif posicao_linha[1] == 'B':
        posicao_linha[1] = 1
    elif posicao_linha[1] == 'C':
        posicao_linha[1] = 2

    if tabela[posicao_linha[1]][posicao_coluna] in 'XO':
        print ('\nEssa posicao ja possui uma jogada! Escolha outra posicao.\n')
        converte_entrada_em_posicao()
            
    elif jogador == 1:
        tabela[posicao_linha[1]][posicao_coluna] = 'O'
    elif jogador == 2:
        tabela[posicao_linha[1]][posicao_coluna] = 'X'


b = []

game_end = 0
while game_end == 0:

    
    
    imprimir_tabela()
    print('')
    jogador = 1
    converte_entrada_em_posicao()
    print('')
    imprimir_tabela()
    print('')

    if tabela[0][2] == 'O' and tabela[1][2] == 'O' and tabela[2][2] == 'O':
        game_end = 1
        print('\nO jogo acabou! O Jogador 1 venceu.')

    elif tabela[0][1] == 'O' and tabela[1][1] == 'O' and tabela[2][1] == 'O':
        game_end = 1
        print('\nO jogo acabou! O Jogador 1 venceu.')

    elif tabela[0][0] == 'O' and tabela[1][0] == 'O' and tabela[2][0] == 'O':
        game_end = 1
        print('\nO jogo acabou! O Jogador 1 venceu.')

    elif tabela[0][0] == 'O' and tabela[0][1] == 'O' and tabela[0][2] == 'O':
        game_end = 1
        print('\nO jogo acabou! O Jogador 1 venceu.')

    elif tabela[1][0] == 'O' and tabela[1][1] == 'O' and tabela[1][2] == 'O':
        game_end = 1
        print('\nO jogo acabou! O Jogador 1 venceu.')

    elif tabela[2][0] == 'O' and tabela[2][1] == 'O' and tabela[2][2] == 'O':
        game_end = 1
        print('\nO jogo acabou! O Jogador 1 venceu.')

    elif tabela[0][0] == 'O' and tabela[1][1] == 'O' and tabela[2][2] == 'O':
        game_end = 1
        print('\nO jogo acabou! O Jogador 1 venceu.')

    elif tabela[0][2] == 'O' and tabela[1][1] == 'O' and tabela[2][0] == 'O':
        game_end = 1
        print('\nO jogo acabou! O Jogador 1 venceu.')

    else:
        c = []
        for linha in tabela:
            for coluna in linha:
                if coluna in 'XO':
                    c.append(coluna)
        if len(c) == 9:
            game_end = 1
            print('\nO JOGO DEU VELHA! NENHUM DOS JOGADORES VENCEU.')
            break
        
        jogador = 2
        print('')
        converte_entrada_em_posicao()
        print('')

        if tabela[0][2] == 'X' and tabela[1][2] == 'X' and tabela[2][2] == 'X':
            game_end = 1
            imprimir_tabela()
            print('\nO jogo acabou! O Jogador 2 venceu.')

        elif tabela[0][1] == 'X' and tabela[1][1] == 'X' and tabela[2][1] == 'X':
            game_end = 1
            imprimir_tabela()
            print('\nO jogo acabou! O Jogador 2 venceu.')

        elif tabela[0][0] == 'X' and tabela[1][0] == 'X' and tabela[2][0] == 'X':
            game_end = 1
            imprimir_tabela()
            print('\nO jogo acabou! O Jogador 2 venceu.')

        elif tabela[0][0] == 'X' and tabela[0][1] == 'X' and tabela[0][2] == 'X':
            game_end = 1
            imprimir_tabela()
            print('\nO jogo acabou! O Jogador 2 venceu.')

        elif tabela[1][0] == 'X' and tabela[1][1] == 'X' and tabela[1][2] == 'X':
            game_end = 1
            imprimir_tabela()
            print('\nO jogo acabou! O Jogador 2 venceu.')

        elif tabela[2][0] == 'X' and tabela[2][1] == 'X' and tabela[2][2] == 'X':
            game_end = 1
            imprimir_tabela()
            print('\nO jogo acabou! O Jogador 2 venceu.')

        elif tabela[0][0] == 'X' and tabela[1][1] == 'X' and tabela[2][2] == 'X':
            game_end = 1
            imprimir_tabela()
            print('\nO jogo acabou! O Jogador 2 venceu.')

        elif tabela[0][2] == 'X' and tabela[1][1] == 'X' and tabela[2][0] == 'X':
            game_end = 1
            imprimir_tabela()
            print('\nO jogo acabou! O Jogador 2 venceu.')
