'''2 - Faça um programa que leia um nome de usuário e a sua senha 
não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro 
e voltando a pedir as informações.'''

print("----------LOGIN SISTEMA PYTHON----------".center(120))
print('')


while True:
    nome = input('Digite o nome de usuário: ')
    senha = input('Digite a sua senha: ')

    if senha == nome:
        print("Erro, a senha não pode ser igual ao usuário, tente de novo.")
    else:
        print('Login realizado com sucesso.')
        break