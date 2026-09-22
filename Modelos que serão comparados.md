# Modelos que serão comparados

Para avaliar diferentes abordagens de **Machine Learning** aplicadas ao conjunto de dados, serão comparados modelos clássicos de **classificação e regressão**. A seleção dos algoritmos considera diferentes estratégias de modelagem, permitindo analisar métodos lineares e não lineares, além de estabelecer modelos de referência (*baselines*).

A comparação não estabelecerá previamente um algoritmo como superior aos demais. A definição do modelo final será realizada posteriormente, com base nos resultados obtidos durante as etapas de validação e avaliação. Serão considerados critérios como **desempenho preditivo, estabilidade, interpretabilidade e custo computacional**.

---

## 5.1 Modelos de classificação

### 5.1.1 Dummy Classifier

O `DummyClassifier` será utilizado como **modelo de referência (*baseline*)** para a tarefa de classificação. Seu objetivo não é apresentar alto desempenho preditivo, mas estabelecer uma referência que permita verificar se os demais classificadores conseguem identificar padrões relevantes nos dados.

Sua utilização possibilitará comparar o desempenho dos modelos desenvolvidos com estratégias simples de previsão baseadas na distribuição das classes, permitindo avaliar se os algoritmos de Machine Learning apresentam ganhos efetivos em relação a uma abordagem de referência.

### 5.1.2 Regressão Logística

A **Regressão Logística** será utilizada como um dos modelos de classificação, atuando como uma abordagem relativamente simples e interpretável. Sua utilização permitirá verificar o desempenho de um modelo baseado principalmente em relações lineares entre as características físico-químicas e as classes de qualidade.

O processamento será realizado por meio de um *pipeline* contendo as etapas de:

- **Imputação de dados**;
- **Padronização das variáveis** com `StandardScaler`;
- Aplicação do modelo `LogisticRegression`.

### 5.1.3 Support Vector Machine — SVM

O terceiro modelo de classificação será o **Support Vector Machine (SVM)**, utilizando a implementação `SVC` com **kernel RBF**.

A utilização do kernel RBF possibilita representar relações não lineares entre as características físico-químicas e as categorias de qualidade. O modelo será integrado a um *pipeline* contendo as etapas de imputação e padronização dos dados.

Durante o processo de otimização, serão avaliados diferentes valores para os principais hiperparâmetros do modelo, incluindo:

- `C`;
- `gamma`;
- `kernel`.

### 5.1.4 Random Forest Classifier

O `RandomForestClassifier` será utilizado como uma abordagem baseada em **árvores de decisão**, sendo capaz de representar relações não lineares e interações entre as variáveis sem exigir a padronização dos atributos.

Além do desempenho preditivo, o Random Forest possibilita analisar a **importância das características** utilizadas pelo modelo. Essa análise poderá auxiliar na identificação das propriedades físico-químicas que apresentam maior contribuição para as previsões realizadas.

Os principais hiperparâmetros considerados serão:

- `n_estimators`;
- `max_depth`;
- `min_samples_split`;
- `min_samples_leaf`;
- `max_features`;
- `class_weight`.

> **Configuração atual:** na implementação atualmente desenvolvida, o Random Forest já está sendo utilizado para a classificação das categorias de qualidade, configurado com **100 árvores**, `random_state=42` e `class_weight='balanced'`.

---

## 5.2 Modelos de regressão

### 5.2.1 Dummy Regressor

O `DummyRegressor` será utilizado como **modelo de referência (*baseline*)** para a tarefa de regressão. Sua função será estabelecer uma referência simples para verificar se os modelos desenvolvidos conseguem obter desempenho superior a uma estratégia de previsão baseada na média dos valores da variável `quality`.

### 5.2.2 Regressão Linear Múltipla

A `LinearRegression` será utilizada como modelo de referência para a previsão numérica da variável `quality`.

Esse modelo permitirá avaliar em que medida uma relação aproximadamente linear entre as características físico-químicas e a qualidade sensorial é capaz de explicar os valores observados.

Além disso, por apresentar uma estrutura relativamente simples e interpretável, a Regressão Linear será utilizada como **baseline** para comparação com modelos de maior complexidade.

### 5.2.3 Support Vector Regression — SVR

Para a tarefa de regressão, será utilizado o **Support Vector Regression (SVR)** com **kernel RBF**.

O SVR possibilita representar relações não lineares entre as características físico-químicas e a variável `quality`. O modelo será utilizado em conjunto com `StandardScaler`, uma vez que a escala das variáveis pode influenciar o funcionamento do algoritmo.

Durante a etapa de otimização, serão avaliados diferentes valores para os principais hiperparâmetros, incluindo:

- `C`;
- `gamma`;
- `epsilon`.

### 5.2.4 Random Forest Regressor

O `RandomForestRegressor` será utilizado como uma abordagem baseada em árvores para a tarefa de regressão.

Assim como sua versão para classificação, o algoritmo permite representar relações não lineares e interações entre as características sem a necessidade de especificar previamente essas relações.

Os principais hiperparâmetros considerados serão:

- `n_estimators`;
- `max_depth`;
- `min_samples_split`;
- `min_samples_leaf`;
- `max_features`.

---

## 5.3 Estratégia de comparação

A comparação entre os modelos será realizada utilizando **o mesmo procedimento de validação e os mesmos conjuntos de dados**, buscando evitar diferenças metodológicas que possam favorecer artificialmente determinado algoritmo.

### 5.3.1 Métricas de classificação

Para a tarefa de **classificação**, serão consideradas principalmente as seguintes métricas e análises:

| Métrica / análise | Objetivo |
|---|---|
| **F1-Score macro** | Avaliar o equilíbrio entre *precision* e *recall* considerando todas as classes de forma equivalente. |
| **Accuracy** | Medir a proporção geral de previsões corretas. |
| **Precision macro** | Avaliar a precisão média das previsões entre as classes. |
| **Recall macro** | Avaliar a capacidade média de identificar corretamente as classes. |
| **Balanced Accuracy** | Avaliar o desempenho considerando o equilíbrio entre as diferentes classes. |
| **Matriz de confusão** | Identificar padrões de acertos e erros entre as classes. |

### 5.3.2 Métricas de regressão

Para a tarefa de **regressão**, serão utilizadas as seguintes métricas e análises:

| Métrica / análise | Objetivo |
|---|---|
| **MAE (Mean Absolute Error)** | Medir o erro absoluto médio das previsões. |
| **RMSE (Root Mean Squared Error)** | Medir a magnitude dos erros, atribuindo maior peso a erros elevados. |
| **R² (Coeficiente de Determinação)** | Avaliar a proporção da variabilidade dos valores reais explicada pelo modelo. |
| **Análise dos resíduos** | Investigar padrões e possíveis problemas nos erros das previsões. |
| **Desempenho em relação aos valores reais de `quality`** | Verificar a proximidade entre os valores previstos e observados. |

### 5.3.3 Processo de validação e otimização

Após a comparação inicial, os modelos que apresentarem resultados mais consistentes serão submetidos ao processo de **otimização de hiperparâmetros**.

Somente após essa etapa será realizada a **avaliação final no conjunto de teste**.

O conjunto de teste permanecerá **intocado durante as etapas de treinamento, validação e ajuste dos modelos**, sendo utilizado exclusivamente para estimar o desempenho final dos modelos selecionados.

---

## 5.4 Considerações finais

Dessa forma, a metodologia proposta permite realizar uma **comparação sistemática** entre modelos com diferentes características, contemplando tanto abordagens simples quanto métodos capazes de representar relações não lineares.

Além disso, a estratégia possibilita investigar de que maneira problemas relacionados à **qualidade dos dados** podem influenciar o desempenho preditivo dos algoritmos.

### Resumo dos modelos

| Tarefa | Modelo | Abordagem |
|---|---|---|
| Classificação | `DummyClassifier` | Baseline |
| Classificação | `LogisticRegression` | Linear |
| Classificação | `SVC (RBF)` | Não linear |
| Classificação | `RandomForestClassifier` | Árvores / ensemble |
| Regressão | `DummyRegressor` | Baseline |
| Regressão | `LinearRegression` | Linear |
| Regressão | `SVR (RBF)` | Não linear |
| Regressão | `RandomForestRegressor` | Árvores / ensemble |

---

> **Nota metodológica:** a escolha do modelo final será realizada somente após a execução dos experimentos, validação, otimização dos hiperparâmetros e avaliação no conjunto de teste. Dessa forma, evita-se estabelecer previamente um algoritmo como superior sem suporte nos resultados experimentais.
