import requests

def enviarTexto(nome, numero, texto, API_KEY):
    url = f"http://localhost:8080/message/sendText/{nome}"

    payload = {
        "number": f"{numero}",
        "textMessage": {"text": f"{texto}"}
    }
    headers = {
        "apikey": f"{API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)