try:
    palavra1 = input("Digite a primeira palavra: ")
    palavra2 = input("Digite a segunda palavra: ")
    if len(palavra1) != len(palavra2):
        raise ValueError("As palavras têm tamanhos diferentes.")
    else:
        print("As palavras têm o mesmo tamanho.")
except ValueError as e:
    print("Erro:", e)