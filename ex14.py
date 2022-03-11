#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" 
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
#Caso contrário, ele será classificado como "Inocente".

print("Olá! Responda as 5 perguntas que avaliarei a participação de uma pessoa no crime.")
perguntas = ["Telefonou para a vítima? ", "Esteve no local do crime? ", "Mora perto da vítima? ", "Devia para a vítima? ", "Já trabalhou com a vítima? "]
respostas = []
respostasPositivas = 0
while True:
    for p in range(0, len(perguntas)):
        respostas.append(input(perguntas[p]))

    for r in range(0, len(respostas)):
        if respostas[r] == "sim":
            respostasPositivas += 1

    if respostasPositivas == 2:
        print("Essa pessoa é suspeita! ")
    elif respostasPositivas >=3 and respostasPositivas <=4:
        print("Essa pessoa é cúmplice! ")
    elif respostasPositivas == 5:
        print("Essa pessoa é culpada! ")
    else:
        print("Essa pessoa é inocente! ")

    desejaContinuar = input("Analisar alguém?")
    if desejaContinuar == "não":
        break