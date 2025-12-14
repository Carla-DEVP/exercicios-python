# Programa para calcular o preço total de uma compra
preco = float(input("Digite o preço unitário: "))
quantidade = int(input("Digite a quantidade: "))

total = preco * quantidade

print(f"O total a pagar é: R$ {total:.2f}")
