import csv
import pandas as pd
import re #Biblioteca de expressões regulares

from datetime import datetime

def carregar_dados(caminho_arquivo):
    dados = pd.read_csv(caminho_arquivo, sep=",", encoding="utf-8-sig", dtype=str, keep_default_na=False) 

    return dados #retornar os dados carregados

# ==== Transformar o DATAFRAME em registros ====

def df_para_registros(df): #criando função para converter o DataFrame em uma lista de dicionários
    registros = df.to_dict(orient="records") #transformando em tabela
    return registros #devolve os registros

# ==== Função para limpar a categoria ====

def limpar_categoria(texto):
    limpo = texto.strip().lower()
    limpo = re.sub(r"[^a-z ]", "", limpo) #nega os caracteres que nao estão no intervalo de a-z e espaços
    limpo = re.sub(r"\s+", " ", limpo).strip() 

    if limpo == "":
        return "sem categoria", True

    return limpo, False

#Padronizando os canais de venda, para que fiquem consistentes e padronizados, evitando erros de digitação ou variações na escrita. 

CANAIS_VALIDOS = {"mercado": "Mercado", "loja física": "Loja física", "web": "Web"}

def padronizar_canal(texto):
    return CANAIS_VALIDOS.get(texto.strip().lower())

