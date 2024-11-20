print("Loja do Victor\n")

valor=float(input("Qual é o preço do produto? \n"))
print("Selecione uma forma de pagamento")
print("""
Digite 1: Para pagar a vista no dinheiro. 
Digite 2: Para pagar a vista no cartão.
Digite 3: Em 2x no cartão
Digite 4: Em 3x no cartão ou mais \n""")
forma=int(input("Selecione a forma de pagamento: \n"))

if forma == 1:
    print("Voce selecionou a vista no dinheiro\n")
    desconto =(valor *(10/100))
    print("Valor a vista no dinheiro: R${:.2f}.".format(
        valor -desconto)
    )
elif forma == 2:
    print("Voce selecionou a vista no cartão.")
    desconto = (valor * (5/100))
elif forma == 3:
    print("Voce selecionou em 2x no cartão.")
    print("Pagamento em 2x de R${:.2f}.".format((valor /2)))
elif forma == 4:  # Em até 3x ou mais: 20% de juros
    print("Você selecionou em 3x ou mais no cartão.")
    desconto = (valor * (20 / 100))
    parcelas = int(input("Em quantas vezes você deseja parcelar? \n"))
    if parcelas < 3:
        print("A quantidade mínima de parcelas é de 3x no cartão.")
    else:
        print("Pagamento, com juros de 20%, em {}x de R$ {:.2f}.".format(
            parcelas, (valor + (desconto)) / parcelas))
else:
    print("Por favor, selecione uma alternativa válida. Tente novamente.")
