from webscraping import obter_carreira_do_jogador

def comparar_carreiras(jogador1, jogador2):
    carreira_jogador1 = obter_carreira_do_jogador(jogador1)
    carreira_jogador2 = obter_carreira_do_jogador(jogador2)

    if not carreira_jogador1 or not carreira_jogador2:
        print("Não foi possível obter informações de carreira para um ou ambos os jogadores.")
        return

    anos_e_times_comuns = {}

    for ano, time in carreira_jogador1.items():
        if ano in carreira_jogador2 and carreira_jogador2[ano] == time:
            anos_e_times_comuns[ano] = time

    if anos_e_times_comuns:
        print(f"Os jogadores {jogador1} e {jogador2} jogaram juntos nos seguintes anos e times:")
        for ano, time in anos_e_times_comuns.items():
            print(f"Ano: {ano}, Time: {time}")
    else:
        print(f"Os jogadores {jogador1} e {jogador2} não jogaram juntos em nenhum ano.")

if __name__ == "__main__":
    jogador1 = input("Digite o nome do primeiro jogador: ")
    jogador2 = input("Digite o nome do segundo jogador: ")

    comparar_carreiras(jogador1, jogador2)

    