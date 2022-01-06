x=2
y=3
z=5

def soma(x, y, z):
    return x+y+z
    a = soma
    a = (1, 2, 3)
    print(soma)

#Ou podemos escrever assim tmb

f = (lambda x, y, z: x + y +z )
f(1, 2, 3)
print(f)