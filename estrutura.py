#ex1
for i in range(1,6):
    print(i) 
i = 0
while i <= 5:
    print(i)
    i += 1
    
#ex2
nomes = ['ana', 'paulo', 'daniel', 'laura']
for i in nomes:
    print(i)   
i - 0
while i < len(nomes):
    print(nomes[i])
    i += 1

#ex3
lista = [10, 20, 30]
soma = 0
for valor in lista:
    soma += valor
print(soma)

#ex4
soma = 0
i = 0
while i < len(lista):
    soma += lista[i]
    i += 1
print(soma)

#ex5

for i in range(3):
    senha = input("Digite sua senha: ")
    if senha == '123':
        print(senha)
        break
    else:
        print("Acesso negado")
        
#ex6 infinito
while True:
    senha = input("Digite a senha: ")
    if senha == '123':
        print("Acesso permitido!")
        break
    else:
        print("Acesso negado")
        
#Exercicio
for i in range(5):
    senha = input("Digite a senha: ")
    if senha == '123':
        print("Acesso permitido!")
        break
    else:
        print("Acesso negado!")
        
while True:
    senha = input("Digite a senha: ")
    if senha == '123':
        print("Acesso liberado!")
        break
    else:
        print("Acesso negado!")
        
 ####################################       
        
for i in range(5):
    nome = input("Digite o nome: ")
    if nome == 'luiz':
        senha = input("Digite a senha: ")
        if senha == '123':
            print("Acesso permitido")
            break
    else:
        print(f"Acesso negado, vc só tem mais {5 - i} tentativas")
print("Bloqueado! Vc exedeu o limites de tentativas" )

#############################################################
     
for i in range(5):
    nome = input("Digite o nome do usuario: ")
    senha = input("Digite a senha: ")
    if nome == 'luiz' and senha == '123':
        print("Acesso liberado!")
        break
    else:
        print("Senha ou Nome incorreto.")
print("Off")

#########################################################

while True:
    nome = input("Digite o nome: ")
    senha = input("Digite a senha: ")
    if nome == 'luiz' and senha == '123':
        print("Acesso liberado!")
        break
    else:
        print("Negado!")

