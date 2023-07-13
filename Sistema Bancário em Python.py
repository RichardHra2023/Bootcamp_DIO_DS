"""
Objetivo do desafio: 

Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

"""

menu = """
*****************   MENU   *******************
[d] Depositar   [s] Sacar 
[e] Extrato     [t] Transferencia
[q] Sair        [i] Informações das operações

**********************************************

"""
saldo = 0
extrato = ""
qtd_depositos = 0

limite_saque = 500
numero_saques = 0
LIMITES_SAQUES = 2

limite_transferencia = 600
numero_transferencia = 0
LIMITES_TRANSFERENCIA = 2

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do seu depósito: "))

        if valor > 0:
            saldo = saldo + valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            qtd_depositos = qtd_depositos + 1
            print(f"Valor de R$ {valor:.2f} depositado com sucesso !")

        else:
            print("Operação invalida! Por favor digite um valor positivo.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_saque

        excedeu_saques = numero_saques > LIMITES_SAQUES

        if excedeu_saldo:
            print("Operação inválida! Você nao tem saldo suficiente")

        elif excedeu_limite:
            print(f"Operação inválida! O valor do saque excede o limite de R$ {limite_saque}")

        elif excedeu_saques:
            print(f"Operação inválida! Você ultrapassou o numero maximo de saques que é {LIMITES_SAQUES+1} por dia")

        elif valor > 0:
            saldo = saldo - valor
            extrato += f"Saque R$ {valor:.2f}\n" 
            numero_saques = numero_saques + 1
            print(f"Valor de R$ {valor:.2f} sacado com sucesso!")

        else:
            print("Operação inválida! O valor informado é inválido.")

    elif opcao == "t":
        valor = float(input("Informe o valor da transação: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_transferencia

        excedeu_transferencia = numero_transferencia > LIMITES_TRANSFERENCIA

        if excedeu_saldo:
            print("Operação inválida! Você nao tem saldo suficiente")

        elif excedeu_limite:
            print(f"Operação inválida! O valor da transferencia excede o limite de R$ {limite_transferencia}")

        elif excedeu_transferencia:
            print(f"Operação inválida! Você ultrapassou o numero maximo de transferencias que é {LIMITES_TRANSFERENCIA+1} por dia")

        elif valor > 0:
            saldo = saldo - valor
            extrato += f"Transferencia R$ {valor:.2f}\n" 
            numero_transferencia = numero_transferencia + 1
            print(f"Valor de R$ {valor:.2f} transferido com sucesso")

        else:
            print("Operação inválida! O valor informado é inválido.")
    
    elif opcao == "e":
        print("\n**************** EXTRATO *************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("**************************************")

    
    elif opcao == "i":
        print("\n******************** INFORMAÇÕES ******************")
        if (qtd_depositos == 0) and (numero_saques == 0) and (numero_transferencia == 0):
            print("Não foram realizadas movimentações.")
        else:
            print(f"Quantidades de depositos realizados hoje: {qtd_depositos}")
            print(f"Quantidades de saques realizados hoje: {numero_saques}")
            print(f"Quantidades de transferencias realizados hoje: {numero_transferencia}")


    elif opcao == "q":
        break

    else:
        print("Operação inválida! Por favor selecione novamente a operação desejada.")


        
    
