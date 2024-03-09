def verificar_maiusculas(string):
    if not string.isupper():
        raise ValueError("minúsculas.")
    else:
        print("maiúsculas.")

try:
    entrada = input("Digite uma string: ")
    verificar_maiusculas(entrada)
except ValueError as ve:
    print("Erro:", ve)