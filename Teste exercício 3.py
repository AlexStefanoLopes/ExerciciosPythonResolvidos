a = [1, 1, 2, 3, 5,6, 8, 13, 21, 34, 55, 89]
l = []
for n in a:
    if n < 4: l.append(n)
print(l,end="")
l = []

inp = int(input("Please give me a number\n"))
for n in a:
    if n < inp: l.append(n)
print(l,end="")