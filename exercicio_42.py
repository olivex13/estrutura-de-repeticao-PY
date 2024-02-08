'''
42 - Faça um programa que leia uma quantidade indeterminada de números positivos 
e conte quantos deles estão nos seguintes intervalos: 
[0-25], [26-50], [51-75] e [76-100]. 

A entrada de dados deverá terminar quando for lido um número negativo.

'''

intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0

# Loop para entrada de dados
while True:
    # Solicita a entrada do usuário
    numero = float(input("Digite um número positivo (ou um negativo para encerrar): "))
    
    # Verifica se o número é negativo para encerrar o programa
    if numero < 0:
        break
    
    # Classifica o número nos intervalos adequados
    if 0 <= numero <= 25:
        intervalo_0_25 += 1
    elif 26 <= numero <= 50:
        intervalo_26_50 += 1
    elif 51 <= numero <= 75:
        intervalo_51_75 += 1
    elif 76 <= numero <= 100:
        intervalo_76_100 += 1
    else:
        print("Número fora dos intervalos especificados.")

# Exibe os resultados
print("\nResultados:")
print(f"Números no intervalo [0-25]: {intervalo_0_25}")
print(f"Números no intervalo [26-50]: {intervalo_26_50}")
print(f"Números no intervalo [51-75]: {intervalo_51_75}")
print(f"Números no intervalo [76-100]: {intervalo_76_100}")