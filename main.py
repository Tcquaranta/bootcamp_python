#Numeros inteiros
#1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
'''
print("digite dois inteiros a serem somados:")
num1 = int(input())
num2 = int(input())aaaa
print("soma = ",num1 +num2)
'''
#2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

'''
num1 = float(input("Digite um numero:"))
print("resto da divisão por 5",str(num1%5))
'''

#3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
'''
print("digite dois inteiros a serem multiplicados:")
num1 = float(input())
num2 = float(input())
print("Multiplicação = ",num1*num2)
'''
#4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
'''
print("digite dois inteiros a serem dividos:")
num1 = int(input())
num2 = int(input())
print("Divisão = ",num1/num2)

'''

#5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
'''
print("digite dois inteiros a numero:")
num1 = float(input())
print("Quadrado = ",num1**2)
'''
#Numeros de pontos flutuantes

#6. Escreva um programa que receba dois números flutuantes e realize sua adição.
'''
print("digite dois numeros float a serem adicionados:")
num1 = float(input())
num2 = float(input())
print("Adição = ",num1+num2)
'''

#7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
'''
print("digite dois numeros:")
num1 = float(input())
num2 = float(input())
print("Média = ",(num1+num2)/2)
'''
#8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
'''
print("digite dois numeros:")
num1 = float(input())
num2 = float(input())
print("Potência = ",(num1**num2))
'''

#9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
'''
print("digite a temperatura em Celsius:")
num1 = float(input())
print("temperatura em fahrenheit = ",(num1*1.8+32))
'''

#10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
'''
print("digite o raio")
num1 = float(input())
print("Área do circula = ",(3.14159*num1**2))
'''
#Strings
#11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
'''
text = str(input("Digite um texto: ")).upper()

print(text)
'''
#12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
'''
text = str(input("Digite o nome do usuário: ")).lower()

print(text)
'''
#13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
'''
text = str(input("Digite um texto: "))
x = text.strip()
print("x",text,"x",x,"x")
'''
#14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
'''
text = str(input('Digite uma data no formato "dd/mm/aaaa": '))
dia = text.split("/")
# dia, mes, ano = data.split("/")
print("dia: "  ,dia[0]," mes: ",dia[1]," ano: ",dia[2])
'''

#15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
'''
text1 = str(input('Digite uma String": '))
text2 = str(input('Digite uma String": '))
text3 = text1+text2
print(text3)
'''

#Booleanos (bool)

#16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
'''
int1 = bool(input("digite um valor booleano "))
int2 = bool(input("digite um valor booleano "))
print(int1 and int2)
'''
#17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
'''
int1 = bool(input("digite um valor booleano "))
int2 = bool(input("digite um valor booleano "))
print(int1 or int2)
'''
#18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
'''
int1 = bool(input("digite um valor booleano "))
int2 = not int1
print(int2)
'''

#19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
'''
int1 = int(input("digite um valor"))
int2 = int(input("digite um valor"))
c = False
if(int1 == int2):
    c = True
print(c)
'''


#20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

'''
int1 = int(input("digite um valor"))
int2 = int(input("digite um valor"))
c = False
if(int1 != int2):
    c = True
print(c)
'''

# Exemplo que causa TypeError
# try:
#     resultado = len(5)
# except TypeError as e:
#     print(e)  # Imprime a mensagem de erro

# Type check

# numero = "kkk"
# numero = 10
# if isinstance(numero, int):
#     print("A variável é um inteiro.")
# else:
#     print("A variável não é um inteiro.")

# Exemplo de Type Conversion

# numero_inteiro = 5
# numero_flutuante = 2.5
# # Converte o inteiro para flutuante e realiza a soma
# soma = float(numero_inteiro) + numero_flutuante
# soma = (numero_inteiro) + int(numero_flutuante)
# print(soma)  # Resultado: 7.5

# Exemplo de try-except

# try:
#     # Código que pode gerar uma exceção
#     resultado = 10 / 0
# except ZeroDivisionError:
#     # Código que executa se a exceção ZeroDivisionError for levantada
#     print("Divisão por zero não é permitida.")

# #The try block will generate a NameError, because x is not defined:

# try:
#   print(x)

# except NameError:
#   print("Variable x is not defined")

# except:
#   print("Something else went wrong")

# else:
#   print("Nothing went wrong") 

# finally:
#   print("The 'try except' is finished") 


# numero = 10
# if numero < 0:
#     raise ValueError("Impossível calcular a raiz quadrada de um número negativo!")
    

# try:
#     resultado = calcular_raiz_quadrada(-10)
# except ValueError as e:
#     print(e)

# Exercício 21: Conversor de Temperatura

# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. 
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
# '''

# try:
#     Celsius = float(input("digite a temperatura em Celsius:"))
#     Fahrenheit = Celsius*1.8+32
    
#     print(f"{Celsius}°C é igual a {Fahrenheit}°F.")
# except ValueError:
#     print("Por favor, digite um número válido para a temperatura.")

# Exercício 22: Verificador de Palíndromo

# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

# a = "kaiak"
# b = a[::-1]
# # a = 5

# if isinstance(a, str):
#     print("A variável é uma string.")
#     if(a==b):
#         print("É um polindrono")
#     else:
#         print("Não é um polindrono")
# else:
#     print("A variável não é uma string.")


# entrada = input("Digite uma palavra ou frase: ")
# if isinstance(entrada, str):
#     formatado = entrada.replace(" ", "").lower()
#     if formatado == formatado[::-1]:
#         print("É um palíndromo.")
#     else:
#         print("Não é um palíndromo.")
# else:
#     print("Entrada inválida. Por favor, digite uma palavra ou frase.")



# Exercício 23: Calculadora Simples

# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. 
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.



# try:
#     # Código que pode gerar uma exceção
#     num1 = float(input("digite um numero:"))
#     num2 = float(input("digite um numero:"))
#     op = str(input("digite o operador (+, -, *, /):"))
#     if(op == "+"):
#         res = num1 + num2;
#     elif(op == "-"):
#         res = num1 - num2;
#     elif(op == "*"):
#         res = num1 * num2;
#     elif(op == "/"):
#         res = num1 / num2;
#     else:
#         print("operador incorreto")

#     print(res)
# except ZeroDivisionError:
#     # Código que executa se a exceção ZeroDivisionError for levantada
#     print("Divisão por zero não é permitida.")
# except ValueError:
#     print("Erro: Entrada inválida. Certifique-se de inserir números.")
# except NameError:
#     print("Erro: Entrada inválida. Certifique-se de que o operador é valido.")


# Exercício 24: Classificador de Números

# Escreva um programa que solicite ao usuário para digitar um número. 
# Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". 
# Adicionalmente, identifique se o número é "par" ou "ímpar".

# try:
#     num1 = float(input("digite um numero:"))
#     if(num1>0):
#         print("Positivo")
#     elif(num1==0):
#         print("zero")
#     else:
#         print("Negativo")
#     if(num1 %2 == 0):
#         print("Par")
#     else:
#         print("Impar")
# except ValueError:
#     print("Erro: Entrada inválida. Certifique-se de inserir números.")

# Exercício 25: Conversão de Tipo com Validação

# Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
# O programa deve converter a string de entrada em uma lista de números inteiros. 
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
# Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. 
# Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

# try:

#     text = str(input("Digite numeros separados por virgura: "))
#     lista_str = text.split(",")
#     lista_int = []
#     for num in lista_str:
#         lista_int.append(int(num.strip()))
#     print(lista_str)
#     print(lista_int)
# except ValueError:
#     print("Erro: Entrada inválida. Certifique-se de inserir números.")
 


 #         AULA 03

# Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

# try:
#     quantidade = int(input("digite a quantidade: "))
#     preço = int(input("digite a quantidade: "))
#     if quantidade<= 0:
#         raise ValueError("O nome não pode estar negativo ou zerado")
#     elif preço <= 0:
#         raise ValueError("O nome não pode estar negativo ou zerado")
#     else:
#         print("Dados validadados")

# except ValueError as e:
#     print(e) 


# Exercício 2: Classificação de Dados de Sensor

# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. 
# Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

#     Temperatura < 18°C é 'Baixa'
#     Temperatura >= 18°C e <= 26°C é 'Normal'
#     Temperatura > 26°C é 'Alta'


# temp = -100
# if temp<18:
#     print("baixa")
# elif temp>=18 and temp<=26:
#     print("normal")
# else:
#     print("alta")

# Exercício 3: Filtragem de Logs por Severidade

# Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. 
# Dado um registro de log em formato de dicionário como log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# if log['level'] == 'ERROR':
#     print(log['message'])

# Exercício 4: Validação de Dados de Entrada

# Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. 
# Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# idade = 20
# email = "thiago@gmail.com"

# if not 18 <= idade <= 65:
#     print("idade incorreta")
# elif "@" not in email or "." not in email:
#     print("não é um email valido")

# Exercício 5: Detecção de Anomalias em Dados de Transações

# Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. 
# Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.

# transacao = {'valor': 10000, 'hora': 10}

# if transacao['valor'] > 10000 or not 9 <= transacao['hora'] <= 18:
#     print("transação invalida")
# else:
#     print("transação normal")
 

#  6. Contagem de Palavras em Textos

# Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.


# texto = "a raposa a a a a  a marrom salta sobre o cachorro marrom preguiçoso"
# Lista = texto.split()
# contagem_palavras = {}
# for i in Lista:
#         if i in contagem_palavras:
#             contagem_palavras[i] +=1
#         else:
#             contagem_palavras[i] = 1
        
# print(contagem_palavras)

# 7. Normalização de Dados
# Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.


# numeros = [10, 20, 30, 40, 50]
# minimo = min(numeros)
# maximo = max(numeros)
# normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

# print(normalizados)

# 9. Extração de Subconjuntos de Dados

# Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.

# numeros = range(1, 11)
# pares = [x for x in numeros if x % 2 == 0]

# print(pares)

# 10. Agregação de Dados por Categoria

# Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800}
# ]
# total_por_categoria = {}
# for venda in vendas:
#     categoria = venda["categoria"]
#     valor = venda["valor"]
#     if categoria in total_por_categoria:
#         total_por_categoria[categoria] += valor
#     else:
#         total_por_categoria[categoria] = valor

# print(total_por_categoria)   

# WHILE

# 11. Leitura de Dados até Flag
# Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

# dados =[]
# # dados = {}
# entrada = ""
# i =0
# while entrada.lower() != "sair":
#     entrada = input("digite um valor de entrada o sair para terminar")
#     if entrada.lower()!= "sair":
#         dados.append(entrada)
#         # dados[i] = entrada
#         # i+=1
# print (dados)


# 12. Validação de Entrada
# Objetivo: Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

# int1 = int(input("digite um valor entre 1 e 10 "))

# while( int1 < 1 or int1 >10):
#     print("Número fora do intervalo!")
#     int1 = int(input("digite um valor entre 1 e 10 "))
    
# print("numero valido")

# 13. Consumo de API Simulado
# Objetivo: Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

# pag_a = 1
# pag_t = 5

# while (pag_a <= pag_t):
#     print(f"Processando página {pag_a} de {pag_t}")
#     pag_a+=1

# print("todas as paginas foram processadas")


# 14. Tentativas de Conexão
# Objetivo: Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

# while tentativa <= tentativas_maximas:
#     print(f"Tentativa {tentativa} de {tentativas_maximas}")
#     # Simulação de uma tentativa de conexão
#     # Aqui iria o código para tentar conectar
#     if True:  # Suponha que a conexão foi bem-sucedida
#         print("Conexão bem-sucedida!")
#         break
#     tentativa += 1
# else:
#     print("Falha ao conectar após várias tentativas.")


# 15. Processamento de Dados com Condição de Parada
# Objetivo: Processar itens de uma lista até encontrar um valor específico que indica a parada.

itens = [1, 2, 3, 5, 6, 7, "parar", 4, 5]

i =0
while i< len(itens):
    if itens[i] == "parar":
        print("Parada encontrada, encerrando o processamento.")
        break
    # Processa o item
    print(f"Processando item: {itens[i]}")
    i += 1