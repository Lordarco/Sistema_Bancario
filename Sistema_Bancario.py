import os

def bank():
    saldo = 1500.58
    limite = 500
    n_saques = 3
    extrato = 'Extrato: \n\n'
    option = 0

    while(option != 4):
        print('-------------------------------------')
        print("1 - Deposito")
        print("2 - Saque")
        print("3 - Extrato")
        print("4 - Sair")
        option = float(input("Escolha um número para realizar a ação: "))

        if(option == 1):
            valor = deposito()
            while valor == 0:
                valor = deposito()
            saldo += valor
            extrato += 'Foi depositado R$' + str(valor) + '\n'
            print(extrato)
            print(f'Saldo total: {saldo}\n\n')
            print('-------------------------------------')
        elif(option == 2):
            if n_saques == 0:
                os.system('cls')
                print('Limite de saque diario excedido!')
            else:
                valor = saque()
                if valor == 0:
                    valor = saque()
                    
                n_saques -= 1
                saldo -= valor
                extrato += 'Foi sacado R$' + str(valor) + '\n'
                print(extrato)
                print(f'Saldo total: {saldo}\n\n')
                print('-------------------------------------')
        elif(option == 3):
            if extrato == 'Extrato: \n\n':
                os.system('cls')
                print("Não há movimentações nesta conta!\n\n")
            else:
                print(extrato)
                print(f'Saldo total: {saldo}\n\n')
                print('---------------------------')
        elif(option == 4):
            print("Muito obrigado, volte sempre!")
        else:
            os.system('cls')
            print("Opção Invalida, escolha uma das opções a seguir: ")

    

    


#Deposito
def deposito():
    valor = float(input("Informe o saldo a ser depositado: "))
    if valor > 0:
        return valor
    else:
        os.system('cls')
        print("Não é possivel realizar deposito de saldo negativo.")
        return 0
#Saque
def saque():
    valor = float(input("Informe o saldo a ser Sacado: "))
    if valor > 500:
        os.system('cls')
        print("Não é possivel realizar saque de um saldo maior que R$ 500.00")
        return 0
    else:
        return valor
#Extrato




bank()