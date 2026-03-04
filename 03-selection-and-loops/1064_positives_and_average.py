#Leia X valores -> o laço

positivo = 0
soma = 0
for numero in range(6):
    valor = float (input())
    if valor > 0:
        positivo = positivo + 1
        soma = soma + valor

media = soma/positivo

print(f"{positivo} valores positivos")
print(f"{media:.1f}")
