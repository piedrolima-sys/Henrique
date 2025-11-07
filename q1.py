num = 101
while True:
    if num % 7 == 0 and num % 3 == 0:
        print(num)
        break
    num += 1


# Lista de notas
notas = [8.5, 4.0, 10.0, 7.5, 6.0, 9.0]

# Variáveis para soma e contagem
soma = 0
contagem_aprovados = 0

# Loop for para percorrer a lista
for nota in notas:
    soma += nota
    if nota >= 7.0:
        contagem_aprovados += 1

# Cálculo da média
media = soma / len(notas)

# Exibição dos resultados
print(f"Média das notas: {media:.2f}")
print(f"Quantidade de notas maiores ou iguais a 7.0: {contagem_aprovados}")

# Listas originais
lista_A = [1, 2, 3, 4, 5]
lista_B = [4, 5, 6, 7, 8]

# Cria a lista de elementos comuns (interseção)
comuns = list(set(lista_A) & set(lista_B))

# Imprime o resultado
print("Elementos comuns às duas listas:", comuns)

estoque = [
    {"nome": "Teclado", "preco": 150.00, "quantidade": 5},
    {"nome": "Mouse", "preco": 80.00, "quantidade": 12},
    {"nome": "Monitor", "preco": 700.00, "quantidade": 3},
    {"nome": "Headset", "preco": 250.00, "quantidade": 8}
]

for produto in estoque:
    if produto["quantidade"] < 10:
        print(produto["nome"])

 
sku = "PRD-004-A-v2"

# Remover todos os hífens e converter para maiúsculas
sku_limpo = sku.replace("-", "").upper()

# Imprimir o resultado
print(sku_limpo)