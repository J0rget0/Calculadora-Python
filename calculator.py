class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def soma(self):
        soma = self.numero1 + self.numero2
        print(f"O resultado da soma é: {soma}")

    def subtração(self):
        subtração = self.numero1 - self.numero2
        print(f'O resultado da subtração é: {subtração}')

    def multiplicação(self):
        multiplicação = self.numero1 * self.numero2
        print(f'O resultado da multiplicação é: {multiplicação}')

    def divisão(self):
      divisão = self.numero1 / self.numero2
      print(f'O resultado da divisão é: {divisão}')

    def porcentagem(self):
      porcentagem = self.numero1 * self.numero2 / 100
      print(f'{numero2}% de {numero1} é igual a: {porcentagem}')

operacao = int(input("""Escolha o dígito da operação que você deseja realizar:
1 - Soma (+)
2 - Subtração (-)
3 - Multiplicação (x)
4 - Divisão (/)
5 - Porcentagem (%)

"""))
if operacao > 5 or operacao < 1:
  print('Insira uma operação válida!!')

elif operacao == 5:
  numero1 = int(input('\nDigite o valor na qual você deseja saber a porcentagem: '))
  numero2 = int(input('Digite o valor da porcentagem a ser calculada: '))

elif operacao != 5:
  numero1 = int(input("\nDigite o primeiro valor: "))
  numero2 = int(input("Digite o segundo valor: "))

calculo = Calculadora(numero1, numero2)

if operacao == 1:
  calculo.soma()

elif operacao == 2:
  calculo.subtração()

elif operacao == 3:
  calculo.multiplicação()

elif operacao == 4:
  calculo.divisão()

elif operacao == 5:
  calculo.porcentagem()