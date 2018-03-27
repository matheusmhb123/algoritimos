n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

maior = n1
menor = n1

if maior < n2:
	maior = n2

if maior < n3:
	maior = n3

if menor > n2:
	menor = n2

if menor > n3:
	menor = n3

print ('Maior:  %d ' %maior)
print ('Menor:  %d ' %menor)


letra = input('Digite uma letra (em minusculo) : ')

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print ('A letra é uma vogal')
else:
    print ('A letra é uma consoante')

nota1 = input('Digite sua nota:')
nota1 = int(n1)
nota2 = input('Digite sua 2° nota:')
nota2 = int(n2)

nota = (n1 + n2) / 2

if nota >= 7 and nota < 10:
    print ("Você foi Aprovado!")
elif nota >= 10:
    print ("Você foi Aprovado com Distinção!")
else:
    print ("Infelizmente você foi reprovado!")




n1 = input('Digite o 1° numero: ')
n2 = input('Digite o 2° numero: ')
n3 = input('Digite o 3° numero: ')

if n1 > n2 and n1 >n3:
    print("n1")
elif n2 > n3 and n2 > n1:
    print("n2")
elif n3 > n1 and n3 > n2:
    print("n3")

#agora o numero do meio
if n1 > n3 and n1 < n2:
	 print("n1")
  elif n2 > n1 and n2 < n3
	  print("n2")
   elif n3 > n2 and n3 > n1:
    print("n3")
elif n2 < n1 and n2 > n3:
    print("n2")


if n1 < n2 and n1 < n3:
    print("n1")
elif n2 < n3 and n2 < n1:
    print("n2")
elif n3 < n1 and n3 < n2:
    print("n3")
