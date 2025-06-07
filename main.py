# Jogo Adedonha (Forca) - Versão Procedural - Projeto Prático
# Autores: João Victor Carneiro Cavalcante e Tobias De Souza Feitoza Cardia
# Data de atulização: 07/06/2025
# Versão: 1.0
# Requisitos: Python 3.x, sem bibliotecas externas, sem uso de POO ou frameworks

import random
import time

def escolher_categoria():
    categorias = {
        "Frutas": ["banana", "laranja", "uva", "morango", "abacaxi"],
        "Animais": ["elefante", "girafa", "cachorro", "gato", "tigre"],
        "Profissoes": ["professor", "bombeiro", "engenheiro", "medico", "advogado"],
        "Paises": ["brasil", "canada", "argentina", "japao", "australia"]
    }
    while True:
        try:
            print("\nCategorias disponíveis:")
            for i, cat in enumerate(categorias.keys(), start=1):
                print(f"{i}. {cat}")
            escolha = int(input("Escolha uma categoria (1-4): "))
            if escolha not in range(1, 5):
                raise ValueError
            categoria = list(categorias.keys())[escolha - 1]
            palavra = random.choice(categorias[categoria])
            return categoria, palavra
        except ValueError:
            print("Entrada inválida. Digite um número entre 1 e 4.")

def exibir_palavra(palavra, letras_corretas):
    return ' '.join([letra if letra in letras_corretas else '_' for letra in palavra])

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

def jogar_rodada():
    categoria, palavra = escolher_categoria()
    tentativas = escolher_dificuldade()
    letras_corretas = []
    letras_erradas = []

    print(f"\nCategoria: {categoria}")

    while tentativas > 0:
        print(f"\nPalavra: {exibir_palavra(palavra, letras_corretas)}")
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")

        letra = input("Digite uma letra: ").lower()

        if not letra.isalpha() or len(letra) != 1:
            print("Digite apenas uma letra válida!")
            continue

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra.")
            continue

        if letra in palavra:
            letras_corretas.append(letra)
            print("Boa! Letra correta.")
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print("Letra incorreta!")

        if all(l in letras_corretas for l in palavra):
            print(f"\nParabéns! Você acertou a palavra: {palavra}\n")
            return True

    print(f"\nFim de jogo. A palavra era: {palavra}\n")
    return False

def iniciar_jogo():
    pontos = 0
    while True:
        ganhou = jogar_rodada()
        if ganhou:
            pontos += 1
        print(f"Pontos atuais: {pontos}")
        again = input("Deseja jogar novamente? (s/n): ").lower()
        while again not in ['s', 'n']:
            again = input("Entrada inválida. Digite 's' para sim ou 'n' para não: ").lower()
        if again != 's':
            break
    print(f"\nFim de jogo. Total de pontos: {pontos}. Obrigado por jogar!")

# Início do programa
if __name__ == "__main__":
    print("\n====== JOGO DA ADEDONHA (FORCA) ======")
    print("Autores: João Victor Carneiro e [Nome do Colega]")
    time.sleep(1)
    iniciar_jogo()
