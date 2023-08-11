
def inputes():
    while True:
        try:
            x = int(input("1: "))
            y = int(input("2: "))
            return x, y
        except:
            print("Os elementos devem ser números inteiros")
            continue

def dividir(a, b):
    d = a / b
    print(f"O valor da divisão é {d}")

x, y = inputes()

if y != 0:
    dividir(x, y)
else:
    print("Não é possível dividir por 0")
