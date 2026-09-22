# Arquitetura Metodológica do Projeto

A metodologia do projeto foi estruturada de forma **sequencial e sistemática**, abrangendo desde a preparação e auditoria do conjunto de dados até o treinamento, a avaliação e a comparação dos modelos de *Machine Learning*. O objetivo é garantir a **reprodutibilidade dos experimentos** e possibilitar uma comparação justa entre os diferentes algoritmos avaliados.

## 4.1 Conjunto de dados

Inicialmente, será utilizado o conjunto de dados **Wine Quality**, disponibilizado pelo **UCI Machine Learning Repository**, tendo como base principal o arquivo referente aos vinhos brancos.

O conjunto de dados contém características físico-químicas dos vinhos, utilizadas como variáveis de entrada, e a variável `quality`, que representa a avaliação sensorial atribuída ao vinho.

## 4.2 Auditoria dos dados

A primeira etapa da metodologia será a **auditoria do conjunto de dados**, com o objetivo de identificar e documentar suas características antes da aplicação de qualquer procedimento de tratamento.

Serão verificadas informações como:

- quantidade de registros e variáveis;
- tipos de dados;
- presença de valores ausentes;
- existência de registros duplicados;
- estatísticas descritivas;
- distribuição da variável `quality`;
- correlação entre as variáveis;
- identificação de possíveis valores extremos.

Durante essa etapa, **nenhuma alteração será realizada na base original**. O objetivo é registrar o estado inicial dos dados e estabelecer uma referência para as etapas posteriores.

## 4.3 Definição dos problemas de modelagem

Após a auditoria, serão definidos dois problemas distintos de modelagem: **classificação** e **regressão**.

No problema de **classificação**, a variável `quality` será transformada em categorias por meio da criação da variável `quality_class`. Inicialmente, serão consideradas três classes:

- **Baixa qualidade**;
- **Média qualidade**;
- **Alta qualidade**.

No problema de **regressão**, a variável `quality` será utilizada diretamente como variável-alvo, permitindo estimar numericamente a avaliação sensorial do vinho.

## 4.4 Divisão dos dados e validação

Após a definição dos problemas, os dados serão divididos em **conjunto de desenvolvimento** e **conjunto de teste**.

O conjunto de teste permanecerá **separado e intocado** durante todas as etapas de treinamento, ajuste e seleção dos modelos. Dessa forma, sua utilização ocorrerá somente na avaliação final, evitando interferências no processo de desenvolvimento.

No conjunto de desenvolvimento, será aplicada **validação cruzada**, permitindo uma comparação mais confiável entre os algoritmos.

Para o problema de classificação, será utilizado o método **StratifiedKFold**, enquanto para o problema de regressão será utilizado o método **KFold**. Em ambos os casos, serão consideradas **cinco divisões (5-fold cross-validation)**.

## 4.5 Experimento de corrupção dos dados

Uma etapa fundamental da metodologia será o experimento relacionado à **qualidade dos dados**.

Após a separação do conjunto de teste, serão criadas cópias dos dados de desenvolvimento para a inserção de **corrupções sintéticas controladas**. Entre os problemas simulados, poderão ser incluídos:

- valores ausentes;
- registros duplicados;
- valores fisicamente inválidos;
- erros de escala;
- problemas de formatação;
- inconsistências nos tipos de dados.

Todas as alterações realizadas serão registradas, permitindo avaliar posteriormente tanto a capacidade de **detecção e correção dos problemas** quanto o impacto dessas corrupções sobre o desempenho dos modelos.

## 4.6 Cenários experimentais

A partir da inserção das corrupções, serão avaliados três cenários principais.

### Cenário 1 — Dados originais

Treinamento dos modelos utilizando os dados em seu estado original, sem a inserção de corrupções.

### Cenário 2 — Dados corrompidos

Treinamento dos modelos utilizando os dados após a inserção das corrupções sintéticas.

### Cenário 3 — Dados corrompidos e limpos

Aplicação do processo de limpeza e tratamento aos dados corrompidos, seguida pelo treinamento dos modelos.

Nos três cenários, será utilizado o **mesmo conjunto de teste limpo**, garantindo uma base comum para comparação.

Essa abordagem permitirá avaliar tanto o **impacto da corrupção dos dados sobre o desempenho preditivo** quanto a **recuperação proporcionada pelo processo de limpeza**.

## 4.7 Processo de tratamento dos dados

O tratamento dos dados seguirá uma ordem previamente definida, contemplando as seguintes etapas:

1. padronização dos tipos de dados;
2. conversão e normalização de valores quando necessário;
3. identificação de valores inválidos;
4. tratamento de registros duplicados;
5. imputação de valores ausentes;
6. análise de possíveis *outliers*.

Os *outliers* identificados por métodos estatísticos **não serão automaticamente removidos**. Será realizada uma distinção entre valores que representam apenas observações estatisticamente extremas e valores considerados efetivamente inválidos de acordo com regras relacionadas ao domínio dos dados.

## 4.8 Treinamento e avaliação dos modelos

Após o tratamento dos dados, serão treinados os modelos candidatos para os problemas de **classificação** e **regressão**.

Cada modelo será avaliado utilizando as **mesmas divisões de dados, procedimentos de validação e métricas**, garantindo condições equivalentes para a comparação dos algoritmos.

### Classificação

Para o problema de classificação, a principal métrica será o **F1-Score macro**, acompanhado das seguintes métricas:

- **Accuracy**;
- **Precision**;
- **Recall**;
- **Balanced Accuracy**;
- **Matriz de confusão**.

### Regressão

Para o problema de regressão, serão utilizadas as seguintes métricas:

- **MAE** (*Mean Absolute Error*);
- **RMSE** (*Root Mean Squared Error*);
- **R²** (*Coeficiente de Determinação*).

## 4.9 Comparação e análise dos resultados

Por fim, os resultados obtidos nos diferentes experimentos serão comparados com o objetivo de analisar o comportamento dos algoritmos em diferentes condições de qualidade dos dados.

Serão considerados aspectos como:

- desempenho preditivo dos modelos;
- impacto das corrupções nos resultados;
- recuperação do desempenho após a limpeza;
- tipos de erros cometidos pelos modelos;
- importância das características físico-químicas;
- diferenças entre os resultados de classificação e regressão;
- influência da qualidade dos dados sobre o desempenho preditivo.

A escolha do modelo a ser utilizado na **aplicação final** será realizada somente após a conclusão dos experimentos e análise dos resultados. Dessa forma, evita-se a seleção antecipada de um algoritmo e garante-se que a decisão seja fundamentada nos resultados obtidos experimentalmente.
