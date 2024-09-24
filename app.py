import os  # Importa o módulo os para executar comandos do sistema operacional

# Lista de restaurantes com informações iniciais (nome, categoria e estado)
restaurantes = [
    {'nome': 'chico', 'categoria': 'brasileira', 'ativo': False},
    {'nome': 'cardoso lanches', 'categoria': 'italiana', 'ativo': True},
    {'nome': 'serolanches', 'categoria': 'brasileira', 'ativo': False}
]

def exibir_nome_do_programa():
    # Exibe o nome do programa com um formato artístico
    print("""
██████████████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
""")

def exibir_opcoes():
    # Exibe as opções disponíveis no menu
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def escolher_opcoes():
    # Função para escolher uma opção do menu
    try:
        opcao_escolhida = int(input('Escolha uma Opção: \n'))  # Pede a entrada do usuário
        match opcao_escolhida:  # Usa o match para verificar a opção escolhida
            case 1:
                opcao_1()  # Chama a função para cadastrar restaurante
            case 2: 
                opcao_2()  # Chama a função para listar restaurantes
            case 3: 
                opcao_3()  # Chama a função para alternar o estado do restaurante
            case 4: 
                opcao_4()  # Chama a função para sair do programa
            case _:  # Caso a opção não seja válida
                opcao_invalida()
    except ValueError:  # Captura erro caso a entrada não seja um número
        opcao_invalida()  

def voltar_ao_menu():
    # Função para voltar ao menu principal após uma ação
    input('\nAperte qualquer tecla para voltar para o menu principal ')
    os.system('cls')  # Limpa a tela do terminal
    main()  # Retorna para a função main

def exibir_titulo(texto):
    # Função para exibir um título com bordas
    linha = '*' * (len(texto))  # Cria uma linha de asteriscos do mesmo comprimento que o texto
    os.system('cls')  # Limpa a tela do terminal
    print(linha)  # Exibe a linha superior
    print(texto)  # Exibe o texto do título
    print(linha)  # Exibe a linha inferior
    print()  # Espaço adicional

def categorias():
    # Exibe as categorias disponíveis para o restaurante
    print('Qual a categoria do restaurante?\n')
    print('1. Brasileira')
    print('2. Lanches')
    print('3. Pizzaria')
    print('4. Japonesa')
    print('5. Italiana')
    print('6. Doces e Sobremesas')

def opcao_1():
    # Função para cadastrar um novo restaurante
    exibir_titulo('Cadastro de restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante: ')  # Pede o nome do restaurante
    categorias()  # Exibe as categorias
    categoria_escolhida = int(input('Escolha uma Opção: \n'))  # Pede a escolha da categoria

    # Determina a categoria com base na escolha do usuário
    if categoria_escolhida == 1:
       categoria_do_restaurante = "Brasileira"
    elif categoria_escolhida == 2:
        categoria_do_restaurante = 'Lanches'
    elif categoria_escolhida == 3:
        categoria_do_restaurante = 'Pizzaria'
    elif categoria_escolhida == 4:
        categoria_do_restaurante = 'Japonesa'
    elif categoria_escolhida == 5:
        categoria_do_restaurante = 'Italiana'
    elif categoria_escolhida == 6:
        categoria_do_restaurante = 'Doces e Sobremesas'
    else:
        opcao_invalida()  # Se a opção não é válida, chama a função de opção inválida

    os.system('cls')  # Limpa a tela
    # Cria um dicionário com os dados do novo restaurante
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
    restaurantes.append(dados_do_restaurante)  # Adiciona o restaurante à lista
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso na categoria {categoria_do_restaurante}!\n')
    voltar_ao_menu()  # Volta ao menu principal

def opcao_2():
    # Função para listar todos os restaurantes cadastrados
    exibir_titulo('lista de restaurantes')
    # Ordena a lista de restaurantes pelo nome
    restaurantes.sort(key=lambda restaurante: restaurante['nome'].lower())
    tabela = '-' * 60  # Linha para separar os dados na lista
    # Exibe os cabeçalhos da tabela
    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    print(tabela)  # Exibe a linha da tabela
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        # Verifica se o restaurante está ativado ou desativado
        ativo_restaurante = 'Ativado' if restaurante['ativo'] else 'Destivado'
        # Exibe os dados do restaurante
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}')
        print(tabela)  # Exibe a linha da tabela após cada restaurante
    voltar_ao_menu()  # Volta ao menu principal

def opcao_3():
    # Função para alternar o estado (ativo/desativado) de um restaurante
    exibir_titulo('Alternar estado do restaurante')
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")  # Pede o nome do restaurante
    restaurante_encontrado = False  # Variável para verificar se o restaurante foi encontrado
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:  # Se o restaurante for encontrado
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']  # Alterna o estado
            # Mensagem de confirmação
            mensagem = f'o restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'o restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:  # Se o restaurante não for encontrado
        print('o restaurante não foi encontrado')
    voltar_ao_menu()  # Volta ao menu principal

def opcao_4():
    # Função para sair do programa
    exibir_titulo('Saindo...')

def opcao_invalida():
    # Função para exibir uma mensagem de opção inválida
    exibir_titulo("""𝙤𝙥𝙘̧𝙖̃𝙤 𝙞𝙣𝙫𝙖́𝙡𝙞𝙙𝙖\n""")
    voltar_ao_menu()  # Volta ao menu principal

def main():
    # Função principal que inicia o programa
    exibir_nome_do_programa()  # Exibe o nome do programa
    exibir_opcoes()  # Exibe as opções do menu
    escolher_opcoes()  # Permite que o usuário escolha uma opção

# Início do programa
if __name__ == '__main__':
    main()  # Chama a função main para iniciar o programa