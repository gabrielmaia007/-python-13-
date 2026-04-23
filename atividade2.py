while True:
    try:
        numero = int(input("Manda um número positivo aí 😄: "))

        if numero < 0:
            print("Eita 😅... negativo não vale! Tenta um positivo 👍")
        else:
            print(f"Aí sim! Número {numero} recebido com sucesso 🎉")
            break

    except:
        print("Hmm 🤔 isso não parece um número... tenta de novo só com números 😉")