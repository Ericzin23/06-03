try:
    numero = int(input("Digite um número inteiro: "))
    if numero == 0:
        print("Não é possível dividir por zero.")
    else:
        resultado = 10 / numero
        print("O resultado da divisão é:", resultado)
except ValueError:
    print("Por favor, digite um número inteiro válido.")