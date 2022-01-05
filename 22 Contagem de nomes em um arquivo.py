# Dado um arquivo .txt que contém uma lista de vários nomes, conte quantos de cada nome
# existem no arquivo e imprima os resultados na tela. Tenho um arquivo .txt para você,
# se quiser usá-lo! Extra:


counter_dict = {}
with open(nameslist.txt) as f:
	line = f.readline()
	while line:
		line = line.strip()
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print(counter_dict)

