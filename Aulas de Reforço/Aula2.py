faturamento = 1200
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento
print(f"Faturamento da empresa: {faturamento}, Custo {custo}, Lucro: {lucro}")

email_cliente = "iury@gmail.com"

# maiuscula
email_cliente = email_cliente.upper()
print(email_cliente)

# minuscula
email_cliente = email_cliente.lower()
print(email_cliente)

# @
print(email_cliente.find("@")) # -1 quando não encontrar

# taqmanho do texto
print(len(email_cliente))

# Pegar um caracter
print(email_cliente[4]) # Pegar o caacter escolhido
print(email_cliente[:4]) # Pegar até o caracter escolhido
print(email_cliente[4:]) # Pegar depois do caracter escolhido
print(email_cliente[1:4]) # Pegar determinados caracter

# Trocar um texto
print(email_cliente.replace("@gmail.com", "@hotmail.com"))

nome = "iury oliveira bonadiman"

# Transformando a primeira letra em maíusculo
print(nome.capitalize())

# Transformando a primeira letra de cada palavra em maiusculo
print(nome.title())

#casos especiais
margem_lucro = round(margem_lucro, 2) # (Variavel, Qtd de casas decimais)
print(f"Faturamento da empresa: R$ {faturamento:.2f}, Custo R$ {custo:.2f}, Lucro: R$ {lucro:.2f}, Margem de lucro: {margem_lucro:.0%}")