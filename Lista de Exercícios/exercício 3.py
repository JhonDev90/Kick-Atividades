"""Faça um programa no qual o usuário precisa cadastrar as informações de uma produto: código, nome, quantidade e preço.
No final o programa deve mostrar as informações cadastradas e exibir o valor total da compras"""

código = int(input("Digite o código do produto: "))
nome = (input("Digite o nome do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))
preço = float(input("Digite o preço: "))

print("\nCódigo:", código)
print("Nome:", nome)
print("Quantidade:", quantidade)
print("Peço:", preço)
print("Total: R$",quantidade * preço)