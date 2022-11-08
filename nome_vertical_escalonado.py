# Interação com o usuário
print("NOME NA VERTICAL\n")
nome = input("DIGITE SEU NOME:")
print("")


# Recebe o tamanho do nome e imprime na vertical 
tamanho_nome = len(nome)
contador = 0

# Laço
for t in nome:
	s=nome[0:contador+1]
	print(s)
	contador = contador + 1