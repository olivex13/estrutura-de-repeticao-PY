''' 1 - Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido 
continue pedindo até que o usuário informe um valor válido.'''

print("----------Verificando notas----------".center(120))
print('')

while True:
    nota = float(input("Digite a nota (0 a 10): "))

    if 0 <= nota <= 10:
        print(f'A nota escolhida foi {nota}')
        break
    else:
        print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")

    