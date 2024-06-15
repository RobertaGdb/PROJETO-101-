import random

response = "y"

while response.lower() == "y":
    # Gerar um número aleatório de 1 a 6 (simulando um dado)
    num = random.randint(1, 6)
    
    # USEI O CHAT SO NESSA PART OKAYY (TAVA COM PREGUIÇA DE DESENHAR OS DADOS)

    if num == 1:
        print("---------")
        print("|       |")
        print("|   0   |")
        print("|       |")
        print("---------")
    elif num == 2:
        print("---------")
        print("|       |")
        print("| 0   0 |")
        print("|       |")
        print("---------")
    elif num == 3:
        print("---------")
        print("|   0   |")
        print("|   0   |")
        print("|   0   |")
        print("---------")
    elif num == 4:
        print("---------")
        print("| 0   0 |")
        print("|       |")
        print("| 0   0 |")
        print("---------")
    elif num == 5:
        print("---------")
        print("| 0   0 |")
        print("|   0   |")
        print("| 0   0 |")
        print("---------")
    else: # num == 6
        print("---------")
        print("| 0   0 |")
        print("| 0   0 |")
        print("| 0   0 |")
        print("---------")
    
    # Solicitar ao usuário para jogar novamente
    response = input("Deseja jogar o dado novamente? (y/n): ")
