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
    while True:
        nome = input('Digite seu nome: ')
        if len(nome) > 3:
            return nome
        else:
            print('Digite um nome válido')

def validar_idade():
       while True:
        idade = int(input('Digite sua idade: '))
        if idade > 0 and idade < 150:
            return idade
        else:
            print('Digite uma idade válida: ')        
def validar_salario():
    
    while True:
        salario = float(input('Digite seu salário: '))
        if salario > 0:
            return salario
          
        else: 
            print('Salario invalido, digite novamente')

def validar_sexo():
    while True:
        sexo = input('Digite seu sexo, F para feminino, M para masculino: ').lower()
        if sexo == 'm' or sexo == 'f':
            return sexo
        else: 
            print('Digite um sexo válido.')

def validar_estado_civil():
    while True:
        estado_civil = input('''Digite seu estado civil:
                                [S] Solteiro
                                [C] Casado
                                [V] Viuvo
                                [D] Divorciado
                                 ==> ''').lower()
    
        if estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
            return estado_civil
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
