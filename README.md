# Projeto Final - Qualidade de Vinhos com Machine Learning

Versão revisada para ficar estritamente alinhada ao conteúdo das aulas fornecidas.

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

## Conteúdos removidos da versão anterior
Foram retirados para evitar ultrapassar o conteúdo das aulas: SVM/SVR, Random Forest, regressão como segunda tarefa paralela, balanced accuracy, experimento de corrupção sintética e regras físicas especializadas.

## Execução
1. Instale as dependências: `pip install -r requirements.txt`
2. Abra `notebooks/Projeto_Completo.ipynb`.
3. Execute todas as células em ordem.

Os arquivos produzidos são salvos em `outputs/`.
