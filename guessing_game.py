# 🎮 Python Number Guessing Game
# Author: Jon
# Description: Simple game to practice logic and user input in Python

import random

recorde = None

print("🎮 Bem-vindo ao jogo de adivinhação!")
print("Versão atualizada!!!!!!!!!!!")

while True:
    print("\nEscolha a dificuldade:")
    print("1 - Fácil (1 a 10 | 5 tentativas)")
    print("2 - Médio (1 a 50 | 7 tentativas)")
    print("3 - Difícil (1 a 100 | 10 tentativas)")

    escolha = input("Digite 1, 2 ou 3: ")

    if escolha == "1":
        limite = 10
        max_tentativas = 5
    elif escolha == "2":
        limite = 50
        max_tentativas = 7
    elif escolha == "3":
        limite = 100
        max_tentativas = 10
    else:
        print("Opção inválida! Indo no fácil 😅")
        limite = 10
        max_tentativas = 5

    numero_secreto = random.randint(1, limite)
    tentativas = 0

    print(f"\n🎯 Adivinhe o número entre 1 e {limite}")
    print(f"💣 Você tem {max_tentativas} tentativas!")

    while tentativas < max_tentativas:
        try:
            tentativa = int(input("\nSeu palpite: "))
            tentativas += 1
        except:
            print("⚠️ Digite um número válido!")
            continue

        diferenca = abs(tentativa - numero_secreto)

        if tentativa < numero_secreto:
            print("📉 Muito baixo!")
        elif tentativa > numero_secreto:
            print("📈 Muito alto!")
        else:
            print(f"\n🎉 ACERTOU em {tentativas} tentativas!")

            if recorde is None or tentativas < recorde:
                recorde = tentativas
                print("🏆 NOVO RECORDE!")

            break

        if diferenca <= 2:
            print("🔥 Tá MUITO perto!")
        elif diferenca <= 5:
            print("😯 Tá perto...")

        print(f"📊 Tentativas restantes: {max_tentativas - tentativas}")

    else:
        print(f"\n💀 Você perdeu! O número era {numero_secreto}")

    if recorde:
        print(f"🏆 Recorde atual: {recorde} tentativas")

    jogar_novamente = input("\nQuer jogar de novo? (s/n): ").lower()
    if jogar_novamente != "s":
        print("👋 Valeu por jogar!")
        break
