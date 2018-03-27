#1-Faça um Programa que peça dois números e imprima o maior deles.
num1 = input("Digite um numero:")
num1 = int(num1)

num2 = input("Digite um numero:")
num2 = int(num2)

if num1 > num2 :
    print("O primeiro numero é maior.")
elif num2 > num1:
    print("O segundo numero é maior.")
else:
    print("Os numeros são iguais.")
#2-Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
a = input("digite o valor:")
a = int(a)

if a < 5:
    print("O valor é negativo.")
else:
    print("O valor é positivo.")

#3-Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = input("Digite m para Masculino e f para feminino:")

if sexo == "m":
    print("M masculino.")
elif sexo == "f":
    print("F feminino.")
else:
    print("Sexo invalido")

#4-Faça um Programa que verifique se uma letra digitada é vogal ou consoante
letra = input("Digite uma letra:")

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("A letra é uma vogal.")
else:
    print("A letra é uma consoante.")

#5- Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar
n1 = input('Digite sua nota:')
n1 = int(n1)
n2 = input('Digite sua 2° nota:')
n2 = int(n2)

nota = (n1 + n2) / 2

if nota >= 7 and nota < 10:
    print ("Você foi Aprovado!")
elif nota >= 10:
    print ("Você foi Aprovado com Distinção!")
else:
    print ("Infelizmente você foi reprovado!")


#6-Faça um Programa que leia três números e mostre o maior deles.
num1 = input("Digite um numero:")
num1 = int(num1)

num2 = input("Digite um numero:")
num2 = int(num2)

num3 = input("Digite um numero:")
num3 = int(num3)

if num1 > num2:
    print("O primeiro é maior.")
elif num2 > num3:
    print("O segundo é maior.")
else:
    print("O terceiro é maior.")

#7-Faça um Programa que leia três números e mostre o maior e o menor deles.
num1 = input("Digite um numero:")
num1 = int(num1)

num2 = input("Digite um numero:")
num2 = int(num2)

num3 = input("Digite um numero:")
num3 = int(num3)

if num1 > num2 > num3:
    print("O primeiro é maior.")
elif num1 < num2 < num3:
    print("O primeiro é menor.")
if num2 > num1 > num3:
    print("O segundo é maior.")
elif num2 < num1 < num3:
    print("O segundo é menor")
if num3 > num2 > num1:
    print("O terceiro é maior")
elif num3 < num2 < num1:
    print("O terceiro é menor")

#8-Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.
prod1 = input("Preco do produto")
prod1 = int(prod1)

prod2 = input("Preco do produto")
prod2 = int(prod2)

prod3 = input("Preco do produto")
prod3 = int(prod3)

if prod1 < prod2 :
    print("Primeiro produto mais barato.")
elif prod2 < prod1:
    print("O segundo é mais barato.")
elif prod3 <= prod2 :
    print("O terceiro é mais barato.")
#10-Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = input('Digite o 1° numero:')
n1 = int(n1)
n2 = input('Digite o 2° numero:')
n2 = int(n2)
n3 = input('Digite o 3° numero:')
n3 = int(n3)

if n1 > n2 and n3:
    print("n1")
elif n2 > n3 and n1:
    print("n2")
if n3 > n1 and n2:
    print("n3")

#agora o numero do meio
if n1 > n3 and n2:
	 print("n1")
 elif n2 > n1 and n3:
	  print("n2")
   elif n3 > n2 and n1:
    print("n3")
elif n2 < n1 and n3:
    print("n2")


if n1 < n2 and n3:
    print("n1")
elif n2 < n3 and n1:
    print("n2")
elif n3 < n1 and n2:
    print("n3")
