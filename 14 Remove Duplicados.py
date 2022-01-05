# Escreva uma função que receba uma lista e retorne uma nova lista
# que contenha # todos os elementos da primeira lista menos as duplicatas.
# este usa um loop for

def dedupe_v1(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
      y.sort()
  return y

#this one uses sets
def dedupe_v2(x):
    return list(set(x))

a = [1,2,3,4,3,2,1,6,6,6]
print(a, '\n')
a.sort()
print(a, '\n')
print(dedupe_v1(a), '\n')
print(dedupe_v2(a))

