faturamento = 1200 # tipo: int -> numero inteiro
custo = 750.0  # tipo: float -> número com casa decimal

novas_vendas = 100
faturamento = faturamento + novas_vendas

imposto = faturamento + 0.1
lucro = faturamento - custo - imposto

margem_lucro = lucro / faturamento


print("Faturamento foi de ", faturamento)
print("O custo foi de ", custo)
print("O lucro foi de ", lucro)
print("A margem de lucro foi de", round(margem_lucro,3))

mensagem = "O faturamento da loja foi de tanto" #
email = "emailqualquer@gmail.com" # tipo string -> texto

# Mod -> % resto da divisão
tempo_contrato = 170
tempo_anos = 170 / 12
print("Tempo em anos", int(tempo_anos))
tempo_meses = 170 % 12
print("Tempo em meses", tempo_meses)

for numero in range(1, 101):  # Conta de 1 a 100
    if numero % 3 == 0:  # Verifica se o número é divisível por 3
        print(numero)
