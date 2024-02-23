#####    Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal    #####                  
#####    e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome    ##### 
#####    e informando o valor do salário em comparação com o bônus recebido.                                           #####    

constante_bonus = 1000


# 1) Solicita ao usuário que digite seu nome
nome_ussuario = input("Digite seu nome: ")


# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario_usuario = float(input("Digite o valor do seu salario: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus_usuario = float(input("Digite a porcentagem do bonus recebido: "))


# 4) Calcule o valor do bônus final
kpi = constante_bonus + salario_usuario * bonus_usuario


# 5) Imprima cálculo do KPI para o usuário
print(kpi)

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"Olá {nome_ussuario}, o seu bonus foi de {kpi}")


# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
