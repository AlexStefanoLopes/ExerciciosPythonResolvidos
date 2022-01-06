class Calculadora:
    def __int__(self,a, b):
        self.a = a
        self.b = b

    def soma(self, a, b):
        resultado = self.a + self.b
        self.impressao(resultado)

    def subtracao(self):
        return self.a - self.b

    def impressao(self, a):
        print(a)

a = int(input("Player a: "))
b = int(input("Player b: "))
soma = Calculadora(5, 5)
print(soma.a)
#
# pessoa1 = Pai('Alcimar', 95)
#
# filha1 = Filha('Mirela', 13, 'Loira')
#
# print(filha1.nome)
# print(filha1.peso)
# print(filha1.cabelo)
# print(pessoa1.nome, pessoa1.peso)