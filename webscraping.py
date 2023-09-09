import requests
from bs4 import BeautifulSoup

def obter_carreira_do_jogador(nome_do_jogador):
    
    url = f"https://www.worldfootball.net/player_summary/{nome_do_jogador}/2/"

    response = requests.get(url)

    if response.status_code == 200:
        # Processar a resposta da API
        soup = BeautifulSoup(response.text, "html.parser")

        # Encontrar a tabela de carreira
        tabela = soup.find("table", class_="standard_tabelle")

        if tabela:
            anos_e_times = {}

            # Iterar pelas linhas da tabela (excluindo o cabeçalho)
            linhas = tabela.find_all("tr")  # Ignorar a primeira linha (cabeçalho)
            for linha in linhas:
                colunas = linha.find_all("td")
                if len(colunas) >= 3:
                    temporada = colunas[2].text.strip()
                    time = colunas[3].text.strip()
                    anos_e_times[temporada] = time
                    

            return anos_e_times

    print(f"Informações de carreira não encontradas para {nome_do_jogador}.")