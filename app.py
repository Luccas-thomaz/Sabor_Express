import os

def exibir_nome_do_programa():
    print("""
██████████████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
""")
def exibir_opcoes():
        print('1. Cadastrar restaurante')
        print('2. Listar restaurante')
        print('3. Ativar restaurante')
        print('4. Sair\n')
def escolher_opcoes():

    opcao_escolhida = int(input('Escolha uma Opção: \n'))  # Pede a entrada dentro da função
    match opcao_escolhida:
        case 1:
            print('Opção 1: Cadastrar restaurante')
        case 2: 
            print('Opção 2: Listar restaurante')
        case 3: 
            print('Opção 3: Ativar restaurante')
        case 4: 
            opcao_4()
        case _:
            opcao_invalida()


def opcao_4():
    os.system('cls')
    print('Saindo...')
def opcao_invalida():
    os.system('cls')
    print("""𝙤𝙥𝙘̧𝙖̃𝙤 𝙞𝙣𝙫𝙖́𝙡𝙞𝙙𝙖\n""")
    main()



  





def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()


if __name__ == '__main__':
    main()