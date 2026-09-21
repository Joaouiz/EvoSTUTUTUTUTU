import requests

from models.filho import Conexao
from service import arquive_service


def criarConexao(nome, API_KEY,numero):

    url = "http://localhost:8080/instance/create"

    payload = {
        "instanceName": f"{nome}",
        "integration": "WHATSAPP-BAILEYS",
        "number": f"{numero}"
    }
    headers = {
        "apikey": f"{API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)

    filhos = [Conexao(nome, numero)] #lista dos caras

    return filhos

def conectarConexao(nome, API_KEY):

    url = f"http://localhost:8080/instance/connect/{nome}"

    headers = {"apikey": f"{API_KEY}"}

    response = requests.get(url, headers=headers)

    dados = response.json()
    qrCode = dados["base64"]
    arquive_service.print_qrCode(qrCode)

    escolha = input("Já leu o QR Code?\n1 - SIM /// 2 - NÃO\n")
    if escolha == "1":
        return
    elif escolha == "2":
        print("Se fodeu kkkkk")
        return


def deletarConexao(nome, API_KEY):

    url = f"http://localhost:8080/instance/delete/{nome}"

    headers = {"apikey": f"{API_KEY}"}

    response = requests.delete(url, headers=headers)

    print(response.text)

