vendedor = input()
salario = float(input())
totalVendas = float(input())
comissao = totalVendas * 0.15
salarioTotal = salario + comissao
print(f"TOTAL = R$ {salarioTotal:.2f}")