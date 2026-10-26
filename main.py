from pathlib import Path
from funcoes import carregar_dados, df_para_registros, limpar_categoria, padronizar_canal


# Descobrir onde está o main.py
pasta_projeto = Path(__file__).resolve().parent

# Localizar o CSV dentro da pasta dados
caminho_csv = pasta_projeto / "dados" / "halloween_vendas.csv"

# Chamar a função e enviar o caminho
dados = carregar_dados(caminho_csv)
registros = df_para_registros(dados)


# Mostrar os nomes das colunas
print("\n=== COLUNAS ===")
print(dados.columns.tolist())

# Mostrar quantidade de linhas e colunas
print("\n=== TAMANHO ===")
print(dados.shape)

# Mostrar os primeiros registros do DataFrame
print("\n=== PRIMEIROS REGISTROS ===")
print(dados.head())



# ==== Apos transformar o DATAFRAME em registros ====

print("\n=== TOTAL DE REGISTROS ===")
print(len(registros))

print("\n=== PRIMEIRO REGISTRO ===")
print(registros[0])

print("\n=== CATEGORIA DO SEGUNDO REGISTRO ===")
print(repr(registros[1]["categoria"]))


#Testando a função de limpeza de categorias

print("\n=== TESTE DE LIMPEZA DE CATEGORIAS ===")

print(limpar_categoria(" FANTASIA!!! "))
print(limpar_categoria(" Acessorio "))
print(limpar_categoria(""))


# Aplicar a limpeza em todos os registros

categorias_vazias = 0 #Cria um contador para categorias vazias
categorias_alteradas = 0 #Cria um contador para categorias alteradas no conteúdo
categorias_so_maiusculas = 0 #Cria um contador para categorias alteradas somente na caixa
canais_padronizados = 0 #Cria um contador para canais padronizados

for registro in registros:
    categoria_original = registro["categoria"]

    categoria_limpa, estava_vazia = limpar_categoria(categoria_original)

    registro["categoria_limpa"] = categoria_limpa

    if estava_vazia:
        categorias_vazias += 1

    elif categoria_original.lower() != categoria_limpa:
        categorias_alteradas += 1

    elif categoria_original != categoria_limpa:
        categorias_so_maiusculas += 1

 # Padronização dos canais

    canal_original = registro["canal_venda"]

    canal_padrao = padronizar_canal(canal_original)

    registro["canal_padrao"] = canal_padrao

    if canal_padrao is not None and canal_original != canal_padrao:
        canais_padronizados += 1


print("\n=== RESULTADO DA LIMPEZA ===")
print("Categorias vazias:", categorias_vazias)
print("Categorias alteradas no conteúdo:", categorias_alteradas)
print("Categorias alteradas somente na caixa:", categorias_so_maiusculas)


#teste para padronizar os canais de venda
print("\n=== TESTE DE PADRONIZAÇÃO DOS CANAIS ===")

print(padronizar_canal(" web "))
print(padronizar_canal(" MERCADO "))
print(padronizar_canal(" LOJA FÍSICA "))
print(padronizar_canal("tv"))

print("\n=== RESULTADO DOS CANAIS ===")

print("Canais padronizados:", canais_padronizados)

print("\n=== EXEMPLOS DE CANAIS ===")

for registro in registros[:5]:
    print("Original:", repr(registro["canal_venda"]))
    print("Padronizado:", repr(registro["canal_padrao"]))
    print("---")


