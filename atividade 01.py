class minhaexcecao(Exception):
    pass


try:
    nun=int(input("numero"))
    if nun % 2 ==0:
        print("par")
    else:
        raise minhaexcecao("impar")
except minhaexcecao as e:
    print (e)


    