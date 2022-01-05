# Dados dois arquivos .txt que contêm listas de números, encontre os números que estão
# sobrepostos. Um arquivo .txt tem uma lista de todos os números primos abaixo de 1000,
# e o outro arquivo .txt tem uma lista de números felizes até 1000. (Se você se esqueceu,
# os números primos são números que não podem ser divididos por nenhum outro número. E sim,
# os números felizes são reais na matemática - você pode procurar na Wikipedia. A explicação
# é mais fácil com um exemplo, que eu irá descrever abaixo.)

# primeslist = []
# with open('primenumbers.txt') as primesfile:
#     line = primesfile.readline()
#     while line:
#         primeslist.append(int(line))
#         line = primesfile.readline()
#
# happieslist = []
# with open('happynumbers.txt') as happiesfile:
#     line = happiesfile.readline()
#     while line:
#         happieslist.append(int(line))
#         line = happiesfile.readline()
#
# overlaplist = []
# for elem in primeslist:
#     if elem in happieslist:
#         overlaplist.append(elem)
#
# print(overlaplist)

def filetolistofints(filename):
	list_to_return = []
	with open(filename) as f:
		line = f.readline()
		while line:
			list_to_return.append(int(line))
			line = f.readline()
	return list_to_return

primeslist = filetolistofints('primenumbers.txt')
happieslist = filetolistofints('happynumbers.txt')

overlaplist = [elem for elem in primeslist if elem in happieslist]
print(overlaplist)