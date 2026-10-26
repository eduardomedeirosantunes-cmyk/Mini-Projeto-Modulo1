# Mini-Projeto-Avaliativo-Modulo1
Machine Learning e Visão Computacional - Turma 04  / Mini-Projeto Avaliativo - Módulo 1 - Semana 07
Aluno: Eduardo Medeiros Antunes

# Mini-Projeto — Festa em Cena

## 1. Apresentação do projeto

Este mini-projeto foi desenvolvido durante o Módulo 1 do curso de Machine Learning e Visão Computacional — SCTEC.

O objetivo é analisar a qualidade dos dados de uma empresa fictícia chamada Festa em Cena, responsável pela comercialização de fantasias e acessórios de Halloween.

O conjunto de dados contém 1.500 pedidos registrados entre agosto e novembro dos anos de 2024 e 2025.

O projeto utiliza Python para leitura, limpeza, validação e análise dos dados, preservando os valores originais e identificando registros inconsistentes.

## 2. Tecnologias utilizadas

- Python
- Pandas, exclusivamente para leitura do arquivo CSV e conversão inicial para registros
- Biblioteca `re`, para limpeza de textos
- Biblioteca `datetime`, para validação e formatação de datas
- Listas, dicionários, conjuntos e funções do Python
- Git e GitHub para versionamento do projeto

O processamento dos registros e os relatórios são realizados em Python nativo.

## 3. Descrição dos dados

O arquivo `halloween_vendas.csv` possui 1.500 registros e 14 colunas.

Cada linha representa um pedido de um produto, que pode conter uma ou mais unidades.

Quatro colunas importantes para a análise são:

| Coluna | Descrição |
|---|---|
| `pedido_id` | Identificador único do pedido |
| `data_venda` | Data e horário em que o pedido foi registrado |
| `quantidade` | Quantidade de unidades compradas no pedido |
| `status_pedido` | Situação do pedido: Concluído, Cancelado ou Devolvido |

Outras colunas utilizadas no projeto incluem `categoria`, `canal_venda`, `preco_unitario` e `data_entrega`.

## 4. Tratamento dos dados

### 4.1 Limpeza das categorias

As categorias foram tratadas utilizando `strip()`, `lower()` e `re.sub()`.

Essas operações permitem remover espaços desnecessários, converter letras para minúsculas e eliminar caracteres não permitidos pela regra adotada.

As categorias vazias foram identificadas e representadas como `sem categoria`, preservando o texto original.

Resultados:

- 18 categorias vazias preenchidas.
- 131 categorias alteradas no conteúdo.
- 1.351 categorias com alteração somente de letras maiúsculas para minúsculas.

A expressão regular utilizada preserva letras de `a` a `z` e espaços, removendo também caracteres acentuados.

### 4.2 Padronização dos canais

Os canais de venda foram normalizados utilizando um dicionário e o método `.get()`.

Os canais reconhecidos são Mercado, Loja física e Web.

Foram identificados 45 registros cuja escrita precisou ser padronizada.

### 4.3 Validação de quantidade e preço

A quantidade é considerada válida quando pode ser convertida em número inteiro maior que zero.

O preço é considerado válido quando está preenchido e pode ser convertido em número maior ou igual a zero.

As conversões foram realizadas com `int()`, `float()` e tratamento de erros com `try/except`.

Resultados:

- 7 quantidades inválidas.
- 12 preços inválidos ou ausentes.
- 19 pedidos distintos com problemas numéricos.

Os pedidos afetados foram identificados por meio de um conjunto (`set`) para evitar contagem duplicada.

Nenhum valor inválido foi substituído por valores inventados.

### 4.4 Validação das datas

A coluna `data_venda` foi convertida utilizando `datetime.strptime()`.

O formato utilizado foi `%Y-%m-%d %H:%M:%S`.

Foram extraídas informações de ano, mês, dia e hora. Também foi criada uma representação da data no formato brasileiro.

Foram identificadas 4 datas inválidas, mantidas sem substituição.

## 5. Investigação da regra de negócio

A hipótese investigada foi:

**Todo pedido sem data de entrega possui status Cancelado.**

O programa encontrou:

- 143 pedidos sem data de entrega.
- 109 pedidos cancelados sem data de entrega.
- 34 pedidos com outro status e sem data de entrega.

A hipótese foi considerada falsa, pois existem pedidos concluídos sem data de entrega.

Um exemplo encontrado foi o pedido 1170, com status Concluído.

O conjunto de dados não informa o motivo da ausência da data de entrega nesses pedidos.

## 6. Análise por canal

| Canal | Pedidos | Participação |
|---|---:|---:|
| Web | 666 | 44,4% |
| Loja física | 551 | 36,7% |
| Mercado | 283 | 18,9% |
| Total | 1.500 | 100% |

Nenhum pedido foi excluído por canal desconhecido.

A análise considera pedidos registrados, incluindo diferentes status, e não representa diretamente unidades vendidas ou faturamento.

## 7. Análise por ano e mês

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

Foram agrupados 1.496 pedidos. Outros 4 foram excluídos dessa análise devido a datas inválidas.

## 8. Principais descobertas

**Descoberta 1 — Participação da Web**

Número: A Web registrou 666 pedidos, representando 44,4% do total.

Interpretação: A Web foi o canal com maior participação nos pedidos registrados.

Limitação: O resultado não representa necessariamente maior faturamento, lucro ou quantidade de unidades vendidas.

**Descoberta 2 — Concentração em outubro**

Número: Outubro registrou 393 pedidos em 2024 e 410 em 2025, uma diferença de 17 pedidos e crescimento aproximado de 4,3%.

Interpretação: Outubro concentrou o maior volume mensal de pedidos nos dois anos.

Limitação: A análise considera apenas os meses de agosto a novembro de dois anos de uma empresa fictícia. Os resultados não demonstram causalidade.

## 9. Organização do projeto

- `main.py`: realiza a execução do programa e apresenta os resultados.
- `funcoes.py`: reúne as funções de leitura, limpeza, validação e análise.
- `dados/halloween_vendas.csv`: contém a base original de pedidos.
- `README.md`: apresenta o projeto e suas instruções.
- `REPORT.md`: documenta os resultados, a hipótese investigada, as descobertas e as limitações da análise.

## 10. Planejamento e organização do desenvolvimento com Git

O código deste mini-projeto foi desenvolvido e testado antes desta reorganização. Para apresentar as funcionalidades por etapas e facilitar o acompanhamento do versionamento, foi realizada uma **reconstrução organizada do mesmo código em três branches**, mantendo a lógica e os resultados do projeto original.

A divisão foi definida conforme a dependência entre as atividades: primeiro a leitura e a limpeza dos dados; depois, as validações numéricas e de datas; por último, a análise, os relatórios e a documentação. Cada etapa aproveita as funcionalidades da anterior.

| Branch | Objetivo | Arquivos trabalhados |
|---|---|---|
| `feature/ingestao-strings` | Ler o CSV com Pandas, converter para registros, limpar categorias e padronizar canais de venda. | `main.py` e `funcoes.py` |
| `feature/validacao-datas` | Acrescentar validações de quantidades e preços, identificar pedidos com problemas numéricos e converter e formatar datas. | `main.py` e `funcoes.py` |
| `feature/relatorios-documentacao` | Acrescentar a investigação da hipótese de entrega, a contagem por canal e período, os percentuais, a comparação entre os meses de outubro e a documentação final. | `main.py`, `funcoes.py`, `README.md` e `REPORT.md` |

A branch `main` representa a versão integrada do projeto. Em cada etapa, o código é executado e conferido antes do commit e do envio ao GitHub. As alterações são revisadas por meio de Pull Requests antes de sua integração à `main`.

**Registro do processo:** a primeira etapa já foi integrada à `main` pelo Pull Request #1, que também reuniu o histórico inicial criado no GitHub com o histórico local. A segunda branch foi publicada para revisão; a terceira corresponde à etapa final de relatórios e documentação. A divisão em três branches documenta a **reorganização posterior** do projeto, e não substitui o histórico original do seu desenvolvimento.

## 11. Como executar

É necessário possuir Python e a biblioteca Pandas instalados.

No terminal, dentro da pasta principal do projeto, instalar o Pandas, caso necessário:

```bash
python -m pip install pandas
```

Com o arquivo CSV disponível na pasta `dados`, executar:

```bash
python main.py
```

O programa realizará a leitura do CSV e apresentará as validações, a investigação da entrega e os relatórios.

## 12. Reflexão sobre qualidade de dados e Machine Learning

A qualidade dos dados é uma etapa fundamental para análises confiáveis e para o desenvolvimento de modelos de Machine Learning.

Valores inconsistentes, categorias escritas de maneiras diferentes e datas inválidas podem comprometer as informações produzidas por um sistema.

Neste projeto, foi possível compreender a importância de validar os dados, identificar inconsistências e preservar os valores originais.

A limpeza dos dados não garante, isoladamente, um modelo de Machine Learning adequado, mas contribui para a preparação de uma base mais confiável para análises e aplicações futuras.

## 13. Limitações gerais

Os dados são fictícios e não representam o comportamento real do mercado.

Os relatórios de pedidos incluem diferentes status e não devem ser interpretados como relatórios de receita.

Os valores ausentes e inválidos foram identificados, mas não substituídos.

As conclusões referem-se somente aos registros e períodos disponíveis na base analisada.

