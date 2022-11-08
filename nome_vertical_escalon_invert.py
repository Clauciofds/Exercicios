# Interação com o usuário
print("NOME NA VERTICAL\n")
nome = input("DIGITE SEU NOME:")
print("")

# Recebe o tamanho do nome e imprime na vertical
tamanho_nome = len(nome)
contador = tamanho_nome

# Laço
while(contador > 0):
	print(nome[0:contador])
	contador = contador - 1