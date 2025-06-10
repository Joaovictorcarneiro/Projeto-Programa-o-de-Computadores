# Jogo Adedonha (Forca) - Versão Procedural - Projeto Prático
# Autores: João Victor Carneiro Cavalcante e Tobias De Souza Feitoza Cardia
# Data de atulização: 09/06/2025
# Versão: 1.0
# Requisitos: Python 3.x, sem bibliotecas externas, sem uso de POO ou frameworks

import random
import time

# Função para escolher a categoria
def escolher_categoria():
    categorias = {
        "Frutas": ["banana", "laranja", "uva", "morango", "abacaxi"],
        "Animais": ["elefante", "girafa", "cachorro", "gato", "tigre"],
        "Profissoes": ["professor", "bombeiro", "engenheiro", "medico", "advogado"],
        "Paises": ["brasil", "canada", "argentina", "japao", "australia"],
        "Super Heróis": ["superman", "batman", "spiderman", "hulk", "thor" ,"jeofton"]
    }
    while True:
        try:
            print("\nCategorias disponíveis:")
            for i, cat in enumerate(categorias.keys(), start=1):
                print(f"{i}. {cat}")
            escolha = int(input("Escolha uma categoria (1-5): "))
            if escolha not in range(1, 6):
                raise ValueError
            categoria = list(categorias.keys())[escolha - 1]
            palavra = random.choice(categorias[categoria])
            return categoria, palavra
        except ValueError:
            print("Entrada inválida. Digite um número entre 1 e 5.")

# Função para exibir a palavra com as letras corretas e as ocultas
def exibir_palavra(palavra, letras_corretas):
    return ' '.join([letra if letra in letras_corretas else '_' for letra in palavra])

# Função para desenhar o estado da forca
def desenhar_forca(tentativas_restantes):
    fases = [
        """
          -----
          |   |
              |
              |
              |
              |
        """,
        """
          -----
          |   |
          O   |
              |
              |
              |
        """,
        """
          -----
          |   |
          O   |
          |   |
              |
              |
        """,
        """
          -----
          |   |
          O   |
         /|   |
              |
              |
        """,
        """
          -----
          |   |
          O   |
         /|\\  |
              |
              |
        """,
        """
          -----
          |   |
          O   |
         /|\\  |
         /    |
              |
        """,
        """
          -----
          |   |
          O   |
         /|\\  |
         / \\  |
        """
    ]
    print(fases[6 - tentativas_restantes])

# Função para escolher a dificuldade
def escolher_dificuldade():
    while True:
        try:
            print("\nEscolha a dificuldade:")
            print("1. Fácil (10 tentativas)")
            print("2. Médio (6 tentativas)")
            print("3. Difícil (3 tentativas)")
            op = int(input("Digite sua escolha: "))
            if op not in [1, 2, 3]:
                raise ValueError
            return {1: 10, 2: 6, 3: 3}[op]
        except ValueError:
            print("Escolha inválida. Digite 1, 2 ou 3.")

# Função para fornecer dicas
def fornecer_dica(palavra, letras_corretas):
    letras_faltando = [letra for letra in palavra if letra not in letras_corretas]
    if letras_faltando:
        dica = random.choice(letras_faltando)
        print(f"Dica: A letra '{dica}' está na palavra!")
        return dica
    else:
        print("Você já acertou todas as letras!")
        return None

# Função principal para jogar uma rodada
def jogar_rodada():
    categoria, palavra = escolher_categoria()
    tentativas = escolher_dificuldade()
    letras_corretas = []
    letras_erradas = []
    dicas_usadas = 0

    print(f"\nCategoria: {categoria}")
    inicio_rodada = time.time()  # Marca o tempo de início da rodada

    while tentativas > 0:
        print(f"\nPalavra: {exibir_palavra(palavra, letras_corretas)}")
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        desenhar_forca(tentativas)  # Desenha a forca com base nas tentativas restantes

        escolha = input("Digite uma letra ou 'dica' para pedir uma dica: ").lower()

        # Verifica se o jogador pediu uma dica
        if escolha == 'dica':
            if dicas_usadas < 1:  # Apenas uma dica por rodada
                dica = fornecer_dica(palavra, letras_corretas)
                if dica:
                    letras_corretas.append(dica)  # Adiciona a letra dada pela dica
                    dicas_usadas += 1
            else:
                print("Você já usou sua dica!")
            continue

        # Verifica se a entrada é válida
        if not escolha.isalpha() or len(escolha) != 1:
            print("Digite apenas uma letra válida!")
            continue

        if escolha in letras_corretas or escolha in letras_erradas:
            print("Você já tentou essa letra.")
            continue

        # Se a letra estiver na palavra, marca como correta
        if escolha in palavra:
            letras_corretas.append(escolha)
            print("Boa! Letra correta.")
        else:
            letras_erradas.append(escolha)
            tentativas -= 1
            print("Letra incorreta!")

        # Verifica se o jogador acertou a palavra
        if all(l in letras_corretas for l in palavra):
            fim_rodada = time.time()  # Marca o tempo de término da rodada
            tempo_rodada = round(fim_rodada - inicio_rodada, 2)  # Calcula o tempo da rodada
            print(f"\nParabéns! Você acertou a palavra: {palavra}")
            print(f"Tempo de conclusão: {tempo_rodada} segundos.")
            return True, tempo_rodada

    print(f"\nFim de jogo. A palavra era: {palavra}")
    return False, 0

# Função para iniciar o jogo
def iniciar_jogo():
    pontos = 0
    tempo_total = 0
    while True:
        ganhou, tempo_rodada = jogar_rodada()
        if ganhou:
            pontos += 1
            tempo_total += tempo_rodada

        print(f"Pontos atuais: {pontos}")
        print(f"Tempo total de jogo: {round(tempo_total, 2)} segundos")
        again = input("Deseja jogar novamente? (s/n): ").lower()
        while again not in ['s', 'n']:
            again = input("Entrada inválida. Digite 's' para sim ou 'n' para não: ").lower()
        if again != 's':
            break
    print(f"\nFim de jogo. Total de pontos: {pontos}. Tempo total de jogo: {round(tempo_total, 2)} segundos. Obrigado por jogar!")

# Início do programa
if __name__ == "__main__":
    print("\n====== JOGO DA ADEDONHA (FORCA) ======")
    time.sleep(1)
    iniciar_jogo()


