nome = input()
salario = float(input())
vendas = float(input())

total = (15 / 100) * vendas 
salario = total + salario

print('TOTAL = R$ {:.2f}'.format(salario))