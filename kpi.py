#Exercicios aula 01


'''
exercicio 1

#print("Digite o seu nome, ")
nome = input("Digite seu nome: ")
print(len(nome))
print(len(input("Digite o seu nome: ")))
'''

##desafio 1


nome = input("Digite seu nome: ")
Salario = int(input("Digite seu Salario: "))
Bonus = float(input("Digite seu bonux: "))
kpi = 1000 + Salario*Bonus

print("Olá ", nome, " , o seu valor bônus foi de ",str(kpi))
