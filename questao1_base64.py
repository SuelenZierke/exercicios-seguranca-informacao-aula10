import base64
import binascii

print("1 - Codificar texto para Base64")
print("2 - Decodificar Base64 para texto")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    mensagem = input("Digite uma mensagem: ")
    resultado = base64.b64encode(
        mensagem.encode("utf-8")
    ).decode("ascii")

    print("Mensagem em Base64:", resultado)

elif opcao == "2":
    mensagem = input("Digite uma mensagem em Base64: ")

    try:
        resultado = base64.b64decode(
            mensagem, validate=True
        ).decode("utf-8")

        print("Mensagem decodificada:", resultado)

    except (binascii.Error, ValueError):
        print("Erro: a entrada não é um Base64 válido.")

    except UnicodeDecodeError:
        print("Erro: o Base64 não representa um texto UTF-8.")

else:
    print("Opção inválida.")