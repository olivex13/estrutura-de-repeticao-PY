'''
3 - Faça um programa que leia e valide as seguintes informações:
        Nome: maior que 3 caracteres;
        Idade: entre 0 e 150;
        Salário: maior que zero;
        Sexo: 'f' ou 'm';
        Estado Civil: 's', 'c', 'v', 'd';
'''

print("----------VALIDANDO INFORMAÇÕES----------".center(120))
print('')

def validar_nome():
    nome = input('Digite seu nome: ')
    while True:
        if len(nome) > 3:
            return nome
        else:
            print('Digite um nome válido')

def validar_idade():
    idade = int(input('Digite sua idade: '))
    while True:
        if idade > 0 and idade < 150:
            return idade
        else:
            print('Digite uma idade válida: ')

        break
    return idade
        
def validar_salario():
    salario = float(input('Digite seu salário: '))
    while True:
        if salario > 0:
            return salario
            break
        else: 
            print('Salario invalido, digite novamente')

def validar_sexo():
    sexo = input('Digite seu sexo, F para feminino, M para masculino: ').lower()
    while True:
        if sexo == 'm' or sexo == 'f':
            return sexo
            break
        else: 
            ('Digite um sexo válido.')

def validar_estado_civil():
    estado_civil = input('''Digite seu estado civil:
                                [S] Solteiro
                                [C] Casado
                                [V] Viuvo
                                [D] Divorciado
                                 ==> ''').lower()
    while True:
        if estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
            return estado_civil
            break
        else:
            print('Digite um estado civil válido.')

idade = validar_idade()
salario =validar_salario()
sexo = validar_sexo()
estado_civil= validar_estado_civil()
nome = validar_nome()

print(f"""Nome: {nome};
        Idade: {idade}
        Salário: R$ {salario:.2f}
        Sexo: {sexo.upper()}
        Estado Civil: {estado_civil}""")
