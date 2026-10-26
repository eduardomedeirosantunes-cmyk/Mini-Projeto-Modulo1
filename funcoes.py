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

# Função para validar a quantidade de produtos vendidos, garantindo que seja um número inteiro positivo.
def validar_quantidade(texto):
    try:
        return int(texto) > 0
    except ValueError:
        return False


def validar_preco(texto):
    if texto.strip() == "":
        return False

    try:
        return float(texto) >= 0

    except ValueError:
        return False


# Formato de data utilizado para validação.
FORMATO_DATA = "%Y-%m-%d %H:%M:%S"

def converter_data(texto):
    try:
        return datetime.strptime(texto, FORMATO_DATA)

    except (ValueError, TypeError):
        return None


# Transformando data no padrao Brasileiro

def formatar_data_br(data):
    return data.strftime("%d/%m/%Y")

# Função para validar a data de venda, garantindo que seja uma data válida e no formato correto.
def investigar_entrega(registros):
    cancelados = 0
    outros = 0
    exemplos = []

    for registro in registros:
        if registro["data_entrega"].strip() == "":
            if registro["status_pedido"] == "Cancelado":
                cancelados += 1
            else:
                outros += 1
                exemplos.append((
                    registro["pedido_id"],
                    registro["status_pedido"],
                    registro["data_venda"]
                ))

    resultado = {
        "sem_entrega_cancelado": cancelados,
        "sem_entrega_outros": outros,
        "hipotese_verdadeira": outros == 0,
        "exemplos": exemplos
    }

    return resultado

# Função para contar os pedidos por canal de venda, retornando a contagem de cada canal e o número de registros com canais desconhecidos.

def contar_pedidos_por_canal(registros):
    contagem = {
        "Web": 0,
        "Loja física": 0,
        "Mercado": 0
    }

    desconhecidos = 0

    for registro in registros:
        canal = registro["canal_padrao"]

        if canal in contagem:
            contagem[canal] += 1
        else:
            desconhecidos += 1

    return contagem, desconhecidos

#Contar os pedidos por periodo

def contar_pedidos_por_periodo(registros):
    contagem = {}
    datas_excluidas = 0

    for registro in registros:
        data = registro["data_venda_dt"]

        if data is None:
            datas_excluidas += 1

        else:
            periodo = data.strftime("%Y-%m")

            if periodo not in contagem:
                contagem[periodo] = 0

            contagem[periodo] += 1

    return contagem, datas_excluidas