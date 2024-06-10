# CALCULADORA
def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por zero."
    

# INTERFACE DO USUÁRIO
def menu():
    print("Selecione a operação:")
    print("1- Adição")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")
    print("5- Sair.")

while True:
    menu()
    escolha = input("Digite sua escolha de 1 a 5: ")
    
    if escolha in ['1', '2', '3', '4']:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f'Resultado: {n1} + {n2} = {somar(n1, n2)}')
        elif escolha == '2':
            print(f'Resultado: {n1} - {n2} = {subtrair(n1, n2)}')
        elif escolha == '3':
            print(f'Resultado: {n1} * {n2} = {multiplicar(n1, n2)}')
        elif escolha == '4':
            print(f'Resultado: {n1} / {n2} = {dividir(n1, n2)}')
    elif escolha == '5':
        print('Saindo..')
        break
    else:
        print('Opção inválida! Tente novamente.')
