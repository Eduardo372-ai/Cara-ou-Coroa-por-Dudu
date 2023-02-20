import random

def cara_ou_coroa():
    opcoes = ["cara", "coroa"]
    escolha_usuario = input("Escolha cara ou coroa: ").lower()
    while escolha_usuario not in opcoes:
        escolha_usuario = input("Escolha cara ou coroa: ").lower()
    escolha_computador = random.choice(opcoes)
    print(f"Você escolheu {escolha_usuario}.")
    print(f"O computador escolheu {escolha_computador}.")
    if escolha_usuario == escolha_computador:
        print("Parabéns, você ganhou!")
    else:
        print("Que pena, você perdeu!")

cara_ou_coroa()
