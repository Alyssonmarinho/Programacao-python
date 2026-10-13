ncasos = int(input())

for i in range(ncasos):
    cord = (input())
    x, y = cord.split(" ")
    x = int(x)
    y = int(y)

    if x % 2 == 0:
        x = x + 1
    soma = 0
    for i in range(y):
        soma = soma + x
        x = x + 2
    print(soma)


# Também pode ser feito como

# valores = input().split()
# n = int(valores[0])
# resultados = []
# idx = 1

# for i in range(n):
#     x = int(valores[idx])
#     y = int(valores[idx + 1])
#     idx += 2

#     if x % 2 == 0:
#         x = x + 1
#     soma = 0
#     for j in range(y):
#         soma = soma + x
#         x = x + 2
#     resultados.append(str(soma))

# print(" ".join(resultados))

#esse segundo é mais complicado e preciso estuda-lo melhor