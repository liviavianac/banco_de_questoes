from database import Database
from questao import Questao

def main():
    db = Database()  # Inicializa a conexão com o banco de dados
    questoes = [Questao(*q) for q in db.buscar_questoes()]  # Busca e cria as questões

    for questao in questoes:
        acertou = False
        while not acertou:
            resposta = input(f"{questao.pergunta} ")  # Pergunta ao usuário
            if questao.verificar_resposta(resposta):
                print("Correto! Próxima questão...\n")
                acertou = True
            else:
                print("Errado! Tente novamente.\n")

    print("Parabéns, você concluiu todas as questões!")
    db.fechar_conexao()  # Fecha a conexão ao final

if __name__ == "__main__":
    main()