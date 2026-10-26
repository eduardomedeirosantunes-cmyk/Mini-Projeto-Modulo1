# Relatório de Análise de Dados — 

**Curso:** Machine Learning e Visão Computacional — SCTEC  
**Módulo:** 1 — Semana 07  

---

## 1. Objetivo da análise

Este relatório apresenta os resultados do mini-projeto Festa em Cena, desenvolvido para aplicar conceitos de qualidade de dados com Python.

A base utilizada contém 1.500 pedidos de uma empresa fictícia que comercializa fantasias e acessórios de Halloween, registrados entre agosto e novembro de 2024 e 2025.

O objetivo foi identificar inconsistências, investigar uma hipótese sobre entregas e produzir relatórios que permitissem interpretar os dados de maneira fundamentada.

O processamento foi realizado com estruturas nativas do Python, utilizando Pandas somente na leitura inicial do CSV e na conversão dos dados para registros.

## 2. Resumo da qualidade dos dados

Durante o processamento, foram identificadas inconsistências em categorias, canais, quantidades, preços e datas.

| Indicador | Resultado |
|---|---:|
| Total de pedidos | 1.500 |
| Categorias vazias identificadas | 18 |
| Categorias com alteração de conteúdo | 131 |
| Categorias com alteração somente de caixa | 1.351 |
| Canais padronizados | 45 |
| Quantidades inválidas | 7 |
| Preços inválidos ou ausentes | 12 |
| Pedidos distintos com problemas numéricos | 19 |
| Datas de venda inválidas | 4 |

As inconsistências foram identificadas e tratadas conforme as regras estabelecidas no projeto, preservando as informações originais e sem substituir valores numéricos ou datas inválidas por dados inventados.

## 3. Investigação da hipótese de entrega

### Hipótese investigada

**Todo pedido sem data de entrega possui status Cancelado.**

Para verificar essa afirmação, foram analisados os pedidos com a coluna `data_entrega` vazia.

### Resultados encontrados

| Situação | Pedidos |
|---|---:|
| Cancelados sem data de entrega | 109 |
| Outros status sem data de entrega | 34 |
| **Total sem data de entrega** | **143** |

O programa identificou o pedido **1170**, com status **Concluído**, como exemplo de registro sem data de entrega.

### Conclusão

**A hipótese foi refutada.**

Dos 143 pedidos sem data de entrega, 34 não possuem status Cancelado.

Portanto, a ausência de data de entrega não é suficiente para afirmar que um pedido foi cancelado.

**Limitação:** a base não informa a causa da ausência da data de entrega nos pedidos identificados. Não é possível determinar se houve falha de registro, atraso ou outra situação.

## 4. Relatório de pedidos por canal

Após a padronização dos canais, foram obtidos os seguintes resultados:

| Canal | Pedidos | Participação |
|---|---:|---:|
| Web | 666 | 44,4% |
| Loja física | 551 | 36,7% |
| Mercado | 283 | 18,9% |
| **Total** | **1.500** | **100%** |

**Canais desconhecidos:** 0.

A Web apresentou a maior quantidade de pedidos registrados, seguida pela Loja física e pelo Mercado.

A contagem considera pedidos, independentemente da quantidade de unidades compradas, e inclui os diferentes status registrados na base.

## 5. Relatório de pedidos por ano e mês

Os pedidos foram agrupados utilizando simultaneamente o ano e o mês da venda.

| Período | Pedidos |
|---|---:|
| 2024-08 | 77 |
| 2024-09 | 104 |
| 2024-10 | 393 |
| 2024-11 | 174 |
| 2025-08 | 62 |
| 2025-09 | 94 |
| 2025-10 | 410 |
| 2025-11 | 182 |
| **Total agrupado** | **1.496** |

**Datas inválidas excluídas do agrupamento:** 4.

A soma dos 1.496 pedidos agrupados com os quatro registros excluídos corresponde aos 1.500 pedidos da base original.

O mês de outubro apresentou a maior quantidade de pedidos nos dois anos analisados.

## 6. Descoberta 1 — Participação do canal Web

### Número

O canal Web registrou **666 pedidos**, correspondendo a **44,4% dos 1.500 pedidos** da base.

### Interpretação

A Web apresentou a maior participação individual na quantidade de pedidos registrados.

O resultado mostra que esse canal concentra uma parcela relevante dos registros de pedidos da empresa fictícia.

### Limitação

O relatório contabiliza pedidos, não unidades vendidas, faturamento ou lucro.

Além disso, a contagem inclui pedidos com diferentes status, como cancelados e devolvidos.

Portanto, não é possível concluir que a Web seja o canal mais lucrativo ou que tenha registrado a maior quantidade de vendas efetivamente concluídas.

## 7. Descoberta 2 — Concentração de pedidos em outubro

### Número

O mês de outubro apresentou os seguintes resultados:

| Período | Pedidos |
|---|---:|
| Outubro de 2024 | 393 |
| Outubro de 2025 | 410 |

A diferença entre os dois períodos foi de **17 pedidos**, equivalente a um crescimento aproximado de **4,3%** em outubro de 2025 em relação a outubro de 2024.

### Interpretação

Outubro foi o mês com o maior volume mensal de pedidos em ambos os anos.

Essa concentração é compatível com a proximidade do Halloween, considerando os produtos comercializados pela empresa fictícia.

### Limitação

A base contempla apenas os meses de agosto a novembro de 2024 e 2025.

Não é possível afirmar que o comportamento se repete em outros anos nem demonstrar que o Halloween foi a causa do aumento dos pedidos.

Além disso, quatro registros não foram incluídos no agrupamento devido a datas inválidas.

## 8. Relação com a qualidade dos dados e Machine Learning

O projeto demonstrou a importância de verificar a qualidade dos dados antes de realizar análises ou utilizar informações em futuros modelos de Machine Learning.

Categorias inconsistentes podem comprometer agrupamentos, valores inválidos podem distorcer cálculos e datas incorretas podem prejudicar análises temporais.

A identificação dessas inconsistências e a preservação dos valores originais contribuíram para tornar os resultados mais transparentes.

Entretanto, a limpeza e a validação dos dados não garantem, isoladamente, a qualidade de um futuro modelo de Machine Learning.

Também seriam necessárias etapas adicionais de preparação, treinamento e avaliação dos modelos.

## 9. Limitações gerais

A análise possui as seguintes limitações:

- Os dados são fictícios e não representam necessariamente o mercado real.
- O período disponível abrange apenas agosto a novembro de dois anos.
- Os relatórios contabilizam pedidos de diferentes status.
- Quantidades e preços inválidos foram identificados, mas não substituídos.
- Quatro datas inválidas foram excluídas apenas do agrupamento temporal.
- Os resultados não permitem estabelecer relações de causa e efeito.

## 10. Organização das etapas e controle de versões

O desenvolvimento foi organizado posteriormente em três etapas de reconstrução, para que a evolução do **código original** pudesse ser acompanhada por commits e Pull Requests no GitHub. Essa divisão não altera as regras nem os resultados da análise.

A ordem das etapas foi definida a partir da dependência entre as funcionalidades:

1. **`feature/ingestao-strings` — leitura e limpeza:** leitura do CSV, conversão para registros, limpeza de categorias e padronização dos canais de venda.
2. **`feature/validacao-datas` — validação:** verificação de quantidades e preços, contagem de pedidos distintos com problemas numéricos, conversão e formatação das datas.
3. **`feature/relatorios-documentacao` — análise e documentação:** investigação dos registros sem data de entrega, relatórios por canal e por ano-mês, cálculos percentuais, descobertas, README e este relatório.

Os códigos foram separados entre `main.py`, responsável pela execução e apresentação dos resultados, e `funcoes.py`, que concentra as funções. O CSV original permanece em `dados/halloween_vendas.csv`. As alterações de cada etapa são testadas e registradas em sua própria branch; a `main` recebe as etapas revisadas por Pull Request.

Na reorganização, o Pull Request #1 integrou a primeira etapa à `main` e reuniu os históricos Git inicialmente separados. A segunda etapa foi enviada ao GitHub para revisão e a terceira foi planejada para fechar a análise e a documentação. Trata-se de uma **reconstrução organizada após a elaboração do código**, preservando o conteúdo original.

## 11. Conclusão

O mini-projeto Festa em Cena permitiu aplicar conhecimentos de Python na leitura, limpeza, validação e análise de dados.

Foram identificadas inconsistências textuais, numéricas e temporais, além de uma hipótese sobre entregas que não foi confirmada.

A análise mostrou que a Web apresentou a maior participação nos pedidos registrados e que outubro concentrou os maiores volumes mensais em 2024 e 2025.

O trabalho reforçou a importância de preservar os dados originais, registrar os problemas encontrados e interpretar os resultados considerando suas limitações.

Essas práticas constituem uma base importante para o desenvolvimento de análises mais confiáveis e futuras aplicações de Machine Learning.

