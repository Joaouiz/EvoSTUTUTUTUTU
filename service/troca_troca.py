import random
import time

import requests

from service import enviar


def troca(numero0, numero1, conexao0, conexao1, API_KEY):
    musicas = ["AiSeEuTePego", "Don'tStopMeNow", "EpisodeX", "Evidências", "FullMoonFullLife", "Maniac", "Nightmare", "NoOneThere", "TheWinnerTakesItAll", "TrainingSeason"]

    with open(f"./letrasMusicas/{random.choice(musicas)}.txt", "r", encoding="utf-8") as arquivo:
        mensagens = [linha.strip() for linha in arquivo if linha.strip()]

        print("Iniciando troca troca...\n")

    for mensagem in mensagens:
        tempo = random.randint(1, 5)
        print("Mensagem sera enviada em " + str(tempo) + " segundos")
        time.sleep(tempo)

        try:
            response = enviar.enviarTexto(conexao0, numero1, mensagem, API_KEY)
            if response.ok:
                print("Mensagem enviada!\n")

                conexao0, conexao1 = conexao1, conexao0
                numero0, numero1 = numero1, numero0
            else:
                print(f"Erro da API: {response.status_code}")
                print(response.text)
                print("Encerrando disparos...\n\n")
                return
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão com a API: {e}")
            print("Encerrando disparos...\n\n")

            return