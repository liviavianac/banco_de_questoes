class Questao:
    def __init__(self, id, pergunta, resposta_correta):
        self.id = id
        self.pergunta = pergunta
        self.resposta_correta = resposta_correta

    def verificar_resposta(self, resposta):
        # Verifica se a resposta está correta
        return resposta.strip().lower() == self.resposta_correta.strip().lower()