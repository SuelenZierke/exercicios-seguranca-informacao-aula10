alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("1 - Cifrar")
print("2 - Decifrar")

opcao = input("Escolha uma opção: ")

if opcao not in ("1", "2"):
    print("Opção inválida.")

else:
    chave = input("Digite o alfabeto mapeado: ").strip().upper()

    if len(chave) != 26 or set(chave) != set(alfabeto):
        print("Erro: a chave deve conter as 26 letras A-Z sem repetição.")

    else:
        texto = input("Digite uma mensagem: ")
        resultado = ""

        if opcao == "1":
            origem = alfabeto
            destino = chave
        else:
            origem = chave
            destino = alfabeto

        for caractere in texto:
            if "A" <= caractere <= "Z":
                posicao = origem.index(caractere)
                resultado += destino[posicao]

            elif "a" <= caractere <= "z":
                posicao = origem.index(caractere.upper())
                resultado += destino[posicao].lower()

            else:
                resultado += caractere

        print("Resultado:", resultado)