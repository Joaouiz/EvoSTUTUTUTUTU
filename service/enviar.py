import requests

def enviarTexto(nome, numero, texto, API_KEY):
    url = f"http://localhost:8081/message/sendText/{nome}"

    payload = {
        "number": numero,
        "text": texto
    }
    headers = {
        "apikey": f"{API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response