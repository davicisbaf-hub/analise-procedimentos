from dotenv import load_dotenv
import os 
import pandas as pd

load_dotenv()
def carregarMensagem():
    arquivo = os.getenv("arquivo")
    tabela = pd.read_excel(arquivo)

    def carregarColuna():
        lista = []
        for column in tabela.columns:
            if "Unnamed" not in str(column):
                lista.append(column)
        return lista

    dados = {
        "mucinipios carregados": carregarColuna()
    }

    df = pd.DataFrame(dados)
    df.to_markdown("./relatorio-criado-municipio/carregados")