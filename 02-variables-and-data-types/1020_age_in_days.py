idade = int(input())
ano = idade // 365
resto = idade % 365
mes = resto // 30
dia = resto % 30
print(f"{ano} ano(s)\n{mes} mes(es)\n{dia} dia(s)")