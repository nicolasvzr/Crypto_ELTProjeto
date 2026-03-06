import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
import time
import os

# Pega a URL do banco das variáveis do Docker
db_url = os.getenv('DATABASE_URL')
engine = create_engine(db_url)

def extrair_dados():
    print("Iniciando extração da CoinGecko...")
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1
    }
    response = requests.get(url, params=params)
    return response.json()



def transformar_dados(dados_brutos):
    print("Transformando dados com Pandas...")
    df = pd.DataFrame(dados_brutos)
    
    # Selecionamos as colunas originais
    colunas = ['id', 'symbol', 'name', 'current_price', 'market_cap', 'last_updated']
    df = df[colunas]
    
    # ADICIONAMOS AQUI: Uma nova coluna com o momento exato da carga
    df['data_carga'] = datetime.now() 
    
    return df

def carregar_dados(df):
    print("Salvando no Postgres...")
    # Usar 'with' garante que a conexão feche e salve os dados no final
    with engine.begin() as connection:
        df.to_sql('precos_cripto', connection, if_exists='replace', index=False)
    print("Sucesso! Dados salvos.")

if __name__ == "__main__":
    # Aguarda o banco subir totalmente
    time.sleep(15) 
    
    try:
        dados = extrair_dados()
        df_limpo = transformar_dados(dados)
        carregar_dados(df_limpo)
    except Exception as e:
        print(f"Erro no pipeline: {e}")