line_menu = "="
print(line_menu * 30)
print(f"{line_menu * 5}BEM VINDO AO BANCO PY{line_menu * 4}")
print(line_menu * 30)

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[v] Verificar Saldo
[q] Sair

=> """

saldo = 0
limite_valor_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
numero_operacoes = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("\nPor favor insira o valor do depósito: \n=> "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: R${deposito:.2f}\n"
            print(f"Depósito no valor de R${deposito:.2f} realizado com sucesso!\n")
            numero_operacoes += 1

        else:
            print("Valor inválido!")

    elif opcao == "s":
        saque = float(input("Valor do saque: \n=> "))

        if saque > limite_valor_saque:
            print("O valor informado é maior que o limite de saque permitido para esse tipo de conta. Por favor, tente novamente.\n")
        
        elif saque <= 0:
            print("O valor informado não é considerado válido para essa operação! Por favor, tente novamente.\n")

        elif numero_saques >= LIMITE_SAQUES:
            print("Você atingiu o limite de saques diários para sua conta, por favor tente novamente amanhã!\n")

        elif saque > saldo:
            print("Saldo insuficiente! Por favor consulte seu saldo e tente novamente!\n")

        else:
            saldo = saldo - saque
            print(f"\nSaque de R${saque:.2f} realizado com sucesso!\n")
            extrato += f"Saque: R${saque:.2f}\n"
            numero_saques += 1
            numero_operacoes += 1        
    
    elif opcao == "e":
        if numero_operacoes > 0:
            print(f"Extrato Bancário:\nSaldo: R${saldo}\n{extrato}")

        else:
            print(f"Extrato Bancário: \nSaldo: R${saldo}\n Nenhuma operação foi realizada nessa conta até o momento.")
                
    elif opcao == "v":
        print(f"O saldo disponível em sua conta é de R${saldo:.2f}\n")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor seleciona a opção desejada.")