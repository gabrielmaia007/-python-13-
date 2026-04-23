while True:
    entrada = input("Digite um número aí 😎: ")

    try:
        numero = int(entrada)
        print(f"Boa! Você digitou o número {numero} 🎉")
        break
    except:
        print("Ops 😅... isso não é número não! Tenta de novo só com números 👍")