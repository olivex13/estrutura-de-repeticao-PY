'''
32 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
-              Fatorial de: 5
        5! =  5 . 4 . 3 . 2 . 1 = 120
'''

print("Calculo de fatorial".center(60))
print('=' * 60)
def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

def exibir_fatorial_formatado(numero):
    fatorial = calcular_fatorial(numero)
    
    print(f"\n- Fatorial de: {numero}")
    print(f"{numero}! = ", end="")

    for i in range(numero, 0, -1):
        print(f"{i}", end="")
        if i > 1:
            print(" . ", end="")
        else:
            print(f" = {fatorial}")

numero_usuario = int(input("Digite um número inteiro para calcular o fatorial: "))

exibir_fatorial_formatado(numero_usuario)
