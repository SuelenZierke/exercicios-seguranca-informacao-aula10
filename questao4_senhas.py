import hashlib
import hmac
import json
from getpass import getpass
from pathlib import Path

arquivo = Path(__file__).with_name("usuarios.json")

if arquivo.exists():
    usuarios = json.loads(arquivo.read_text(encoding="utf-8"))
else:
    usuarios = {}

print("1 - Cadastrar")
print("2 - Autenticar")

opcao = input("Escolha uma opção: ")

if opcao in ("1", "2"):
    usuario = input("Digite o nome de usuário: ").strip()
    senha = getpass("Digite a senha: ")

    hash_senha = hashlib.sha256(
        senha.encode("utf-8")
    ).hexdigest()

    if opcao == "1":
        if not usuario or not senha:
            print("Usuário e senha não podem ser vazios.")

        elif usuario in usuarios:
            print("Esse usuário já está cadastrado.")

        else:
            usuarios[usuario] = hash_senha

            arquivo.write_text(
                json.dumps(usuarios, indent=4, ensure_ascii=False),
                encoding="utf-8"
            )

            print("Cadastro realizado!")

    else:
        hash_salvo = usuarios.get(usuario)

        if hash_salvo is not None and hmac.compare_digest(
            hash_salvo, hash_senha
        ):
            print("Acesso permitido!")
        else:
            print("Usuário ou senha incorretos.")

else:
    print("Opção inválida.")