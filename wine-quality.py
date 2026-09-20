import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import warnings

# 1. Carregar os datasets separadamente
red_wine = pd.read_csv('winequality-red.csv', sep=';')
white_wine = pd.read_csv('winequality-white.csv', sep=';')

# Função para treinar o modelo e gerar o feedback de precisão
def avaliar_modelo_vinho(df, tipo_vinho):

    # Ignorar o aviso de divisão por zero na tela
    warnings.filterwarnings('ignore')

    # 2. AGRUPAMENTO DE DADOS (BINNING)
    # Criando os intervalos de corte e as etiquetas
    intervalos = (2, 4.5, 6.5, 10) # Corta em: 3-4, 5-6, 7-10
    categorias = ['Ruim', 'Normal', 'Excelente']

    # Substituindo as notas de 0 a 10 pelas 3 categorias
    df['qualidade_categoria'] = pd.cut(df['quality'], bins=intervalos, labels=categorias)

    # 3. Separar os parâmetros. Note que removemos a 'quality' antiga e a nova categoria
    X = df.drop(['quality', 'qualidade_categoria'], axis=1)
    y = df['qualidade_categoria']

    # 4. Dividir em Treino e Teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 5. Treinar o modelo utilizando Pesos Balanceados (Solução 1 em conjunto)
    modelo = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    modelo.fit(X_train, y_train)

    # 6. Realizar as previsões e avaliar
    previsoes = modelo.predict(X_test)
    precisao = accuracy_score(y_test, previsoes)
    relatorio = classification_report(y_test, previsoes, zero_division=0)

    print("========== NOVO FEEDBACK: VINHO TINTO AGRUPADO ==========")
    print(f"Precisão Global: {precisao:.2%}\n")
    print(relatorio)

# 2. Executar a avaliação para cada tipo de vinho
avaliar_modelo_vinho(red_wine, "Tinto")
avaliar_modelo_vinho(white_wine, "Branco")
