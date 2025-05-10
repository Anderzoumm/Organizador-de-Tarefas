#Crie um programa em Python para gerenciar uma lista de tarefas. O programa deve permitir ao usuário:
#Adicionar uma nova tarefa
#Remover uma tarefa concluída
#Exibir a lista de tarefas pendentes
#Desfazer a última ação (usando pilha para armazenar histórico)
#Sair do programa
import os
import time
lista = [ ]
opcoes = [1, 2, 3, 4, 5]
print ("GERENCIADOR DE TAREFAS")
print ("######################")
escolha = "#1- Adiconar tarefas \n#2- Remover tarefas \n#3- Exibir tarefas pendentes \n#4- Exibir tarefas concluidas \n#5- Sair"
while True:
    print (escolha)
    opc = int(input("Digite uma das opções acima: "))
    if opc == 5:
        print ("Encerrando programa...")
        break
    if opc == ValueError:
        print ('opcao invalida ')
        continue
    if opc not in opcoes:
        print ('opcao invalida ')
        continue
