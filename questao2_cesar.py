print("1 - Cifrar")
print("2 - Decifrar")

opcao = input("Escolha uma opção: ")

if opcao in ("1", "2"):
    texto = input("Digite uma mensagem: ")

    try:
        chave = int(input("Digite o deslocamento: "))
        resultado = ""

        for caractere in texto:
            if "A" <= caractere <= "Z":
                base = ord("A")
            elif "a" <= caractere <= "z":
                base = ord("a")
            else:
                resultado += caractere
                continue

            posicao = ord(caractere) - base

            if opcao == "1":
                nova_posicao = (posicao + chave) % 26
            else:
                nova_posicao = (posicao - chave) % 26

            resultado += chr(base + nova_posicao)

        print("Resultado:", resultado)

    except ValueError:
        print("Erro: o deslocamento deve ser um número inteiro.")

else:
    print("Opção inválida.")