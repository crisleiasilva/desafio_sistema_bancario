print("=" * 14)
print("\033[34mBanco Py\033[m")
print("=" * 14)
menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Infome o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Falha na operação! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Falhou! \033[31mSaldo Insuficiente\033[m")

        elif excedeu_limite:
            print("Operação Falhou! \033[31m O valor do saque ultrapassa o limite\033[m")

        elif excedeu_saques:
            print("Operação Falhou! \033[31mNúmero máximo de saques execedido\033[m")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! Valor informado é inválido")

    elif opcao == "e":
        print("\n==========\033[36mEXTRATO\033[m==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n\033[34mSaldo: R$ {saldo:.2f}\033[m")

    elif opcao == "q":
        break

    else:
        print("Operação Inválida! Por favor selecione novamente a operação desejada.")

