def while1():
    x=50
    while x<=100:
        print(x)
        x = x + 1
#while1()

def while2():
    x=1
    while x<=100:
        print(x)
        x = x + 1
#while2()
def contagem_regressiva():
    x = 10
    while x >=1:
        print(x)
        x = x - 1
    print("fogo")
#contagem_regressiva()
def whilw_while():
    fim=int(input("digite o ultimo numero a imprimir:"))
    x = 0
    while x <= fim:
        if x % 2 == 1:
            print(x)
        x = x + 1
whilw_while()