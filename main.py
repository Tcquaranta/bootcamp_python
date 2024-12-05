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

try:

    text = str(input("Digite numeros separados por virgura: "))
    lista_str = text.split(",")
    lista_int = []
    for num in lista_str:
        lista_int.append(int(num.strip()))
    print(lista_str)
    print(lista_int)
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")
 