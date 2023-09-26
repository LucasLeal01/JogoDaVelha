import os

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):

    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or \
           all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador or \
       tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogadas = 0

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        exibir_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual}, é sua vez!")

        linha = int(input("Digite o número da linha (0, 1 ou 2): "))
        coluna = int(input("Digite o número da coluna (0, 1 ou 2): "))

        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2 or tabuleiro[linha][coluna] != " ":
            print("Jogada inválida. Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador_atual
        jogadas += 1

        if verificar_vitoria(tabuleiro, jogador_atual):
            os.system("cls" if os.name == "nt" else "clear")
            exibir_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            break
        elif jogadas == 9:
            os.system("cls" if os.name == "nt" else "clear")
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

    return jogador_atual

def salvar_placar(vencedor):
    try:
        with open("placar.txt", "a") as arquivo:
            arquivo.write(f"Vencedor: {vencedor}\n")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o placar: {e}")

def exibir_placar():
    try:
        with open("placar.txt", "r") as arquivo:
            placar = arquivo.read()
            print("Placar:")
            print(placar)
    except FileNotFoundError:
        print("O arquivo de placar ainda não existe.")

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("Bem-vindo ao Jogo da Velha!")
        opcao = input("Escolha uma opção:\n1. Jogar\n2. Exibir Placar\n3. Sair\n")

        if opcao == "1":
            vencedor = jogar_jogo_da_velha()
            salvar_placar(vencedor)
        elif opcao == "2":
            exibir_placar()
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()