from Pessoa import Pessoa

def CriarPessoa():
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    cpf = str(input('Digite o cpf: '))
    telefone = int(input('Digite o telefone: '))

    return Pessoa(nome, idade, cpf, telefone)

def ExcluirPessoa():
    excluir = int(input('\nQual contato dejesa excluir da agenda? (DIGITE O ID): '))
    listaPessoas.pop(excluir - 1)

def ListarPessoas():
    for cont, pessoa in enumerate (listaPessoas):
                print(f'Contato ID: {cont + 1} | {pessoa}')

listaPessoas = []

while True:
    print("""
=============================
|   ------ Agenda -------   |                  
|   [1] Adicionar Contato   |
|   [2] Excluir Contato     |
|   [3] Mostrar Contatos    |
|   [4] Sair da Agenda      |
|   ---------------------   |
==============================""")

    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        pessoa = CriarPessoa()
        listaPessoas.append(pessoa)
        print('=' * 30)
        print('\n- Contato adicionado com sucesso! -')

    if opcao == 2:
        if not listaPessoas:
            print('=' * 30)
            print('\n- A agenda ainda está vazia! -')

        else:
            for cont, pessoa in enumerate (listaPessoas):
                print(f'Contato ID: {cont + 1} | {pessoa}')

            ExcluirPessoa()
            print('\n- Contato excluído com sucesso! -')

    if opcao == 3:
        if not listaPessoas:
            print('=' * 30)
            print('\n- A agenda ainda está vazia! -')
        else:
            print('\n')
            ListarPessoas()

    if opcao == 4:
         break
    
print('\n- Programa finalizado, volte sempre! -')
