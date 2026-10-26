from pathlib import Path
from funcoes import carregar_dados, df_para_registros, limpar_categoria, padronizar_canal,validar_quantidade
from funcoes import validar_preco, converter_data, formatar_data_br, investigar_entrega, contar_pedidos_por_canal
from funcoes import contar_pedidos_por_periodo


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

quantidades_invalidas = 0 #Cria um contador para quantidades inválidas
precos_invalidos = 0 #Cria um contador para preços inválidos.
pedidos_com_problema = set() #Cria um conjunto vazio para armazenar os identificadores dos pedidos que possuem problemas numéricos.

datas_invalidas = 0 #Cria um contador para datas inválidas.

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

 # Verificar a quantidade do pedido

    quantidade_original = registro["quantidade"]

    quantidade_valida = validar_quantidade(quantidade_original)

    registro["quantidade_valida"] = quantidade_valida

    if not quantidade_valida:
        quantidades_invalidas += 1
        pedidos_com_problema.add(registro["pedido_id"])

 # Verificar o preço do pedido

    preco_original = registro["preco_unitario"]

    preco_valido = validar_preco(preco_original)

    registro["preco_valido"] = preco_valido

    if not preco_valido:
        precos_invalidos += 1
        pedidos_com_problema.add(registro["pedido_id"])

 # Verificar a data do pedido

    data_original = registro["data_venda"]

    data_convertida = converter_data(data_original)

    registro["data_venda_dt"] = data_convertida

    if data_convertida is None:
        datas_invalidas += 1

    else:
        registro["ano"] = data_convertida.year
        registro["mes"] = data_convertida.month
        registro["dia"] = data_convertida.day
        registro["hora"] = data_convertida.hour
        registro["data_br"] = formatar_data_br(data_convertida)


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


print("\n=== TESTE DE VALIDAÇÃO DE QUANTIDADES ===")

print(validar_quantidade("3"))
print(validar_quantidade("-1"))
print(validar_quantidade("0"))
print(validar_quantidade("abc"))


print("\n=== TESTE DE VALIDAÇÃO DE PREÇOS ===")

print(validar_preco("132.5"))
print(validar_preco("0"))
print(validar_preco("-10"))
print(validar_preco(""))
print(validar_preco("abc"))


print("\n=== VALIDAÇÃO DOS DADOS NUMÉRICOS ===")

print("Quantidades inválidas:", quantidades_invalidas)

print("Preços inválidos:", precos_invalidos)

print("Pedidos com problemas numéricos:", len(pedidos_com_problema))


print("\n=== TESTE DE CONVERSÃO DE DATAS ===")

data = converter_data("2025-10-12 14:35:00")

print(data)
print(data.year)
print(data.month)
print(data.day)
print(data.hour)

print(converter_data("data_invalida"))

#Convertendo para padrao Brasileiro a data
print("Data brasileira:", formatar_data_br(data)) 


#Exibindo o total de datas inválidas

print("\n=== VALIDAÇÃO DAS DATAS ===")

print("Datas inválidas:", datas_invalidas)

print("\n=== EXEMPLO DE DATA CONVERTIDA ===")

for registro in registros:
    if registro["data_venda_dt"] is not None:
        print("Original:", registro["data_venda"])
        print("Ano:", registro["ano"])
        print("Mês:", registro["mes"])
        print("Dia:", registro["dia"])
        print("Hora:", registro["hora"])
        print("Data BR:", registro["data_br"])
        break

#Investigando os registros que não possuem data de entrega

print("\n=== INVESTIGAÇÃO DA ENTREGA ===")

entrega = investigar_entrega(registros)

print("Cancelados sem entrega:", entrega["sem_entrega_cancelado"])

print("Outros status sem entrega:", entrega["sem_entrega_outros"])

print("Hipótese verdadeira:", entrega["hipotese_verdadeira"])

print("Primeiro exemplo:", entrega["exemplos"][0])


#Relatorio de pedidos por canal

print("\n=== RELATÓRIO DE PEDIDOS POR CANAL ===")

contagem_canais, canais_desconhecidos = contar_pedidos_por_canal(registros)

for canal, quantidade in contagem_canais.items():
    print(canal, ":", quantidade)

print("Canais desconhecidos:", canais_desconhecidos)

#Verificando relatorio de pedidos por ano e mês

print("\n=== RELATÓRIO DE PEDIDOS POR ANO E MÊS ===")

contagem_periodos, datas_excluidas = contar_pedidos_por_periodo(registros)

for periodo in sorted(contagem_periodos):
    print(periodo, ":", contagem_periodos[periodo])

print("Datas excluídas:", datas_excluidas)


#calculando o percentual de pedidos por canal

print("\n=== PERCENTUAL DE PEDIDOS POR CANAL ===")

total_pedidos = len(registros)

for canal, quantidade in contagem_canais.items():
    percentual = (quantidade / total_pedidos) * 100

    print(canal, ":", round(percentual, 1), "%")

#Comparando o mês de outubro de 2024 e 2025

print("\n=== COMPARAÇÃO DE OUTUBRO ===")

outubro_2024 = contagem_periodos["2024-10"]
outubro_2025 = contagem_periodos["2025-10"]

diferenca = outubro_2025 - outubro_2024

variacao = (diferenca / outubro_2024) * 100

print("Outubro de 2024:", outubro_2024)
print("Outubro de 2025:", outubro_2025)
print("Diferença:", diferenca)
print("Variação percentual:", round(variacao, 1), "%")