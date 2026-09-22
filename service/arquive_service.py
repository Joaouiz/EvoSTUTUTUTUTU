import json
from dataclasses import asdict
import base64
import io
from PIL import Image

def registrarConexoes(caminho, lista):
    with open(caminho, "a") as arquivo:
        json.dump([asdict(c) for c in lista], arquivo, indent=4, ensure_ascii=False, default=str)

def print_qrCode(string_base64: str): #Essa buceta nao funciona
    """
    Decodifica uma string Base64 (PNG) de um QR Code e renderiza no terminal.

    :param string_base64: A string completa (com ou sem 'data:image/png;base64,')
    :param tamanho: Resolução de redimensionamento (largura/altura em pixels).
                    O padrão 45 funciona bem na maioria dos terminais.
    """
    tamanho = 80
    try:
        # 1. Remove o prefixo data:image/... se existir
        if "base64," in string_base64:
            string_base64 = string_base64.split("base64,")[-1]

        # 2. Converte de volta para imagem binária
        dados_binarios = base64.b64decode(string_base64)
        img = Image.open(io.BytesIO(dados_binarios)).convert("1")  # Modo 1-bit (Preto e Branco)

        # 3. Redimensiona mantendo a proporção quadrada
        img = img.resize((tamanho, tamanho), Image.Resampling.NEAREST)

        # 4. Renderiza os blocos no terminal
        # Nota: Usamos dois blocos "██" por pixel preto porque os caracteres do
        # terminal costumam ser duas vezes mais altos do que largos.
        for y in range(img.height):
            linha = "".join("██" if img.getpixel((x, y)) == 0 else "  " for x in range(img.width))
            print(linha)

    except Exception as e:
        print(f"Erro ao processar o QR Code: {e}")

def lerKey(caminho):
    with open(caminho, "r") as arquivo:
        key = arquivo.read()
    return key
