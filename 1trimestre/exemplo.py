preco_bruto = 789.90

d10 = preco_bruto * (10/100)
preco_final = preco_bruto - d10

d10 = preco_final * (10/100)
preco_final = preco_final - d10

d10 = preco_final * (10/100)
preco_final = preco_final - d10

print("Final: R$" , preco_final)
