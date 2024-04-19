			

### var.py
def my_var():
    inteiro = 42
    texto = "42"
    citacao = "quarante-deux"
    decimal = 42.0
    booleano = True
    lista= [42]
    dicionario = {42: 42}
    tupla = (42,)
    grupo = set()
    
    print(texto , " tem o tipo ", type(texto))
    print(inteiro, " tem o tipo ", type(inteiro))
    print(citacao, "tem o tipo", type(citacao))
    print(decimal, "tem o tipo", type(decimal))
    print(booleano, "tem o tipo", type(booleano))
    print(lista, "tem o tipo", type(lista))
    print(dicionario, "tem o tipo", type(dicionario))
    print(tupla, "tem o tipo", type(tupla))
    print(grupo, "tem o tipo", type(grupo))

my_var()