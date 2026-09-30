# Projeto Final - Qualidade de Vinhos com Machine Learning

## Objetivo
Classificar a qualidade de vinhos brancos em **baixa, média ou alta** usando dois modelos clássicos estudados na disciplina:

- Regressão Logística
- K-Nearest Neighbors (KNN)

`DummyClassifier` é usado somente como baseline.

## Conteúdos aplicados
- leitura e auditoria dos dados;
- EDA;
- valores ausentes e outliers;
- divisão treino/teste estratificada;
- `Pipeline`;
- imputação pela mediana;
- `StandardScaler`;
- validação cruzada;
- ajuste simples de `C` e `K`;
- Accuracy, Precision, Recall, F1-Score e matriz de confusão.

## Execução
1. Instale as dependências: `pip install -r requirements.txt`
2. Abra `notebooks/Projeto_Completo.ipynb`.
3. Execute todas as células em ordem.

Os arquivos produzidos são salvos em `outputs/`.
