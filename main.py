from service import conectar, arquive_service, troca_troca
from service.enviar import enviarTexto


def main():
    API_KEY = arquive_service.lerKey("./key.txt")
    escolha = input("1 - Criar Conexao\n2 - Conectar Conexao\n3 - Deletar Conexao\n4 - Mandar Mensagem\n5 - Troca Troca\n6 - Vazar\nOq c ke faze?\n")

    while escolha != "6":
        match escolha:
            case "1":
                nome = input("Qual o nome da conexão? ")
                numero = input("Qual o número da conexão? ")
                conexoes = conectar.criarConexao(nome, API_KEY, numero)

            case "2":
                nome = input("Qual o nome da conexão? ")
                conectar.conectarConexao(nome, API_KEY)

            case "3":
                nome = input("Qual o nome da conexão? ")
                conectar.deletarConexao(nome, API_KEY)

            case "4":
                nome = input("Qual o nome da conexão? ")
                numero = input("Qual o número do destinatário? ")
                texto = input("Qual o conteúdo da mensagem? ")
                enviarTexto(nome, numero, texto, API_KEY)

            case "5":
                    conexao0 = input("Qual o nome da primeira conexao? ")
                    conexao1 = input("Qual o nome da segunda conexao? ")

                    numero0 = input("Qual o primeiro numero? ")
                    numero1 = input("Qual o segundo numero? ")

                    disparos = input("Serao quantos disparos? ")
                    for i in range(int(disparos)):
                        troca_troca.troca(numero0, numero1, conexao0, conexao1, API_KEY)

            case _:
                print("Opção inválida! Tente novamente.")

        escolha = input("1 - Criar Conexao\n2 - Conectar Conexao\n3 - Deletar Conexao\n4 - Mandar Mensagem\n5 - Troca Troca\n6 - Vazar\nOq c ke faze?\n")


if __name__ == '__main__':
    main()