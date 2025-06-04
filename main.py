import random

# Função para escolher uma palavra aleatória
def escolher_palavra():
    palavras = ["python", "javascript", "desenvolvimento", "computador", "programacao"]
    return random.choice(palavras)

# Função para exibir o estado da palavra
def exibir_palavra(palavra, letras_corretas):
    return ' '.join([letra if letra in letras_corretas else '_' for letra in palavra])

# Função principal do jogo
def jogar():
    print("Bem-vindo ao jogo da Adedonha (Forca)!")
    
    palavra = escolher_palavra()
    letras_corretas = []
    letras_erradas = []
    tentativas = 6
    
    # Loop do jogo
    while tentativas > 0:
        print(f"\nPalavra: {exibir_palavra(palavra, letras_corretas)}")
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        
        # Solicitar uma letra ao jogador
        letra = input("Digite uma letra: ").lower()
        
        # Verificar se o jogador já tentou essa letra
        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        # Verificar se a letra está na palavra
        if letra in palavra:
            letras_corretas.append(letra)
            print("Boa! A letra está na palavra.")
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print(f"A letra {letra} não está na palavra.")
        
        # Verificar se o jogador adivinhou a palavra
        if all(letra in letras_corretas for letra in palavra):
            print(f"\nParabéns, você adivinhou a palavra: {palavra}!")
            break
    else:
        print(f"\nVocê perdeu! A palavra era: {palavra}")

# Iniciar o jogo
if __name__ == "__main__":
    jogar()
