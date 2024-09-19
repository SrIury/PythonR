# inputs
# pelo input pegamos os dados com o usuário

# email = input("Digite seu e-mail: ")
# nome = input("Qual o seu nome? ")

# print(nome, email)

# print(f"{nome}, verifique seu email: {email} que enviamos um link de confirmação!")

# # Todo input é importado como um texto, você precisa converter ele caso deseje utilizar números
# faturamento = float(input("Escreva o faturamento: "))

# imposto = faturamento * 0.1
# print(imposto)

# # Listas
# vendas = [100, 500, 300, 5, 900]

# # soma
# total_vendas = sum(vendas)
# print(total_vendas)

# # tamanho da lista
# qtd_vendas = len(vendas)
# print(qtd_vendas)

# # Valor Min e Max
# max_Vendas = max(vendas)
# min_Vendas = min(vendas)

# print(f"O valor máximo da lista é: {max_Vendas}, e o menor valor da lista é: {min_Vendas}")

# # pegar posição
# lista_produtos = ["iphone", "airpod", "ipad", "macbook"]

# produto_procurado = input("Pesquise pelo nome do produto: ")
# produto_procurado = produto_procurado.lower()

# print(produto_procurado in lista_produtos)

# adicionar um item

# lista_produtos.append("apple watch")
# print(lista_produtos)

# # Remover um item da lista
# lista_produtos.remove("apple watch") # .pop remove um item mas pela posição do item
# print(lista_produtos)

# # Editar um item da lista
# preco = [200, 5800, 700]
# preco[0] = 600
# preco[0] = preco[0] * 1.5

# print(preco)

# contar quantas vezes o item se repete
lista_produtos = ["iphone", "airpod", "ipad", "macbook", "iphone"]
print(lista_produtos.count("iphone"))

# ordenar uma lista
vendas = [100, 500, 300, 5, 900]
vendas.sort()
vendas.sort(reverse=True)
print(vendas)
