Com base nos metadados originais de Cortez et al. (2009), nas diretrizes oficiais da OIV (Organização Internacional da Vinha e do Vinho), nas especificações do arquivo winequality.names, e na literatura complementar do artigo Measuring Wine Quality and
Typicity, apresento o detalhamento e as restrições lógicas para cada variável.

### 1. Fixed Acidity (Acidez Fixa)
*  **Definição:** Representa os ácidos não voláteis (que não evaporam facilmente) presentes no vinho, majoritariamente os ácidos tartárico, málico e succínico.
*  **Unidade:** g(ácido tartárico) / dm³ (Cortez et al., 2009).
*  **Papel enológico:** Fornece frescor, estrutura, preserva a cor e atua como conservante natural contra contaminações microbianas.
*  **Qualidade sensorial:** Existe um limite de aceitação; níveis equilibrados trazem frescor, mas o excesso torna o vinho adstringente e excessivamente azedo. Uma análise baseada em regressão linear simples aponta que a acidez fixa tem um efeito positivo na qualidade. Contudo, em modelos de regressão linear múltipla, ela parece não ser um fator principal de influência na qualidade.
*  **Intervalo típico:** 4.0 a 15.9 g/dm³ (observado nos dados originais).
*  **Erros de medição:** Valores negativos ou superiores a 20 g/dm³ (fisicamente implausível para um vinho bebível).
*  **Por que não remover outliers:** Uma acidez extremamente alta pode ser decorrente de colheita muito precoce ou erro humano na correção de acidez, resultando em uma nota sensorial legitimamente baixa (qualidade ruim).

### 2. Volatile Acidity (Acidez Volátil)
*  **Definição:** Quantidade de ácidos voláteis, primariamente o ácido acético.
*  **Unidade:** g(ácido acético) / dm³ (Cortez et al., 2009).
*  **Papel enológico:** É um subproduto natural da fermentação bacteriana e do envelhecimento. Em níveis altos, é o principal indicador de que o vinho está "picado" (virando vinagre).
*  **Qualidade sensorial:** Tem uma relação linear significativa e negativa com a qualidade do vinho tinto. Níveis elevados causam sabor e aroma desagradáveis de vinagre. 
*  **Intervalo típico:** 0.1 a 1.6 g/dm³. A OIV geralmente estabelece o limite legal máximo de acidez volátil em torno de 1.0 a 1.2 g/L para a maioria dos vinhos.
*  **Erros de medição:** Valores negativos ou extremos como > 5.0 g/dm³ (seria puramente vinagre, improvável de ser submetido como vinho comercial).
*  **Por que não remover outliers:** Vinhos com acidez volátil alta (1.5 - 2.0) violam normas técnicas e apresentam falha óbvia (defeito enológico). O modelo precisa desses outliers para aprender que altos valores resultam fatalmente em notas baixas.

### 3. Citric Acid (Ácido Cítrico)
*  **Definição:** Um ácido orgânico menor no vinho, às vezes adicionado artificialmente para corrigir a acidez total.
*  **Unidade:** g / dm³ (Cortez et al., 2009).
*  **Papel enológico:** Adiciona "frescor" e vivacidade. Também atua estabilizando o ferro no vinho, prevenindo turbidez (casse férrica).
*  **Qualidade sensorial:** Gráficos de barras demonstram que a quantidade de ácido cítrico é diretamente proporcional à qualidade do vinho. À medida que a qualidade sobe, a quantidade de ácido cítrico também aumenta, indicando ser uma característica básica para a dependência da qualidade. Apesar disso, análises de correlação multivariada apontam que ele não é o fator principal isolado.
*  **Intervalo típico:** 0.0 a 1.0 g/dm³. A OIV permite adição de ácido cítrico até o limite máximo de 1.0 g/L no produto final.
*  **Erros de medição:** Valores negativos ou superiores a 3.0 g/dm³ (adição excessiva ilegal e quimicamente rara).
*  **Por que não remover outliers:** Uma adulteração (excesso de ácido cítrico) tornaria o vinho desequilibrado e receberia uma nota baixa. Remover esse dado ocultaria o impacto de adulterações.

### 4. Residual Sugar (Açúcar Residual)
*  **Definição:** Açúcares da uva (glicose e frutose) que não foram convertidos em álcool pelas leveduras ao final da fermentação.
*  **Unidade:** g / dm³ (Cortez et al., 2009).
*  **Papel enológico:** Determina a percepção de doçura e influencia o "peso" e corpo do vinho no paladar.
*  **Qualidade sensorial:** Depende do estilo do vinho. Análises de correlação e regressão linear simples indicam que o açúcar residual quase não tem efeito direto sobre a qualidade do vinho tinto neste dataset. Além disso, em análises de regressão multivariada, ele demonstrou pouca influência na qualidade.
*  **Intervalo típico:** 0.5 a 65.8 g/dm³ nos dados de Cortez (vinhos brancos *Vinho Verde* frequentemente têm mais açúcar residual).
*  **Erros de medição:** Valores negativos. Valores acima de 150 g/dm³ são normais para vinhos de sobremesa, mas atípicos para a denominação *Vinho Verde* tradicional de mesa.
*  **Por que não remover outliers:** Há estilos específicos (como vinhos levemente doces ou de colheita tardia) que possuem alta concentração de açúcar natural. São dados válidos que o modelo deve generalizar.

### 5. Chlorides (Cloretos)
*  **Definição:** Quantidade de sais presentes no vinho.
*  **Unidade:** g(cloreto de sódio) / dm³ (Cortez et al., 2009).
*  **Papel enológico:** Deriva principalmente do solo (terroir) e da água de irrigação. Contribui para o perfil mineral e sensação salina.
*  **Qualidade sensorial:** Possui uma relação linear significativa e negativa com a qualidade do vinho tinto. Níveis muito altos mascaram o sabor frutado.
*  **Intervalo típico:** 0.01 a 0.6 g/dm³. 
*  **Erros de medição:** Valores negativos ou anomalias acima de 2.0 g/dm³ (teria gosto literal de água do mar).
*  **Por que não remover outliers:** Vinhedos costeiros ou erros de filtragem/clarificação podem gerar vinhos salgados, o que pune legitimamente a avaliação sensorial.

### 6. Free Sulfur Dioxide (Dióxido de Enxofre Livre)
*  **Definição:** É a fração do SO2 não ligada a outras moléculas, existindo em equilíbrio físico no vinho.
*  **Unidade:** mg / dm³ (Cortez et al., 2009).
*  **Papel enológico:** É o principal conservante ativo. Protege contra oxidação (escurecimento) e impede o crescimento de leveduras selvagens e bactérias indesejadas.
*  **Qualidade sensorial:** Tem uma correlação positiva com a qualidade do vinho tinto, sendo um fator que impacta positivamente nas avaliações quando em equilíbrio. Gráficos de barras mostram uma contribuição significativa para a qualidade.
*  **Intervalo típico:** 1.0 a 70 mg/dm³ (geralmente mantido entre 20 e 50 mg/L pelos enólogos).
*  **Erros de medição:** Valores negativos, ou situações em que o SO2 Livre seja numericamente maior que o SO2 Total (uma impossibilidade matemática e química).
*  **Por que não remover outliers:** Se o enólogo exagerar no sulfito, o vinho apresentará um odor "picante" e metálico, recebendo nota baixa. A relação causa-efeito é real.

### 7. Total Sulfur Dioxide (Dióxido de Enxofre Total)
*  **Definição:** Soma do dióxido de enxofre livre e da fração que se ligou quimicamente a aldeídos, açúcares e pigmentos.
*  **Unidade:** mg / dm³ (Cortez et al., 2009).
*  **Papel enológico:** Representa o histórico de todo o sulfito adicionado ao longo do processo de vinificação.
*  **Qualidade sensorial:** Apresenta uma relação linear significativa, correlacionando-se negativamente com a qualidade do vinho tinto. Excesso causa asfixia aromática (aromas de fósforo riscado).
*  **Intervalo típico:** 6.0 a 289 mg/dm³. A OIV limita estritamente o SO2 total (variando de 150 mg/L em tintos secos a cerca de 400 mg/L em brancos muito doces).
*  **Erros de medição:** Valores negativos ou superiores a 500 mg/dm³ em vinhos de mesa normais.
*  **Por que não remover outliers:** Níveis que extrapolam os limites da OIV sinalizam má qualidade e toxicidade, correspondendo a escores baixos legítimos dados por avaliadores.

### 8. Density (Densidade)
*  **Definição:** Relação de massa por volume do líquido.
*  **Unidade:** g / cm³ (Cortez et al., 2009).
*  **Papel enológico:** É um parâmetro físico ditado principalmente pelo balanço entre água (densidade ~1.0), álcool (densidade ~0.79) e açúcar residual (que aumenta a densidade).
*  **Qualidade sensorial:** Não é um fator principal isolado. A literatura aponta que a densidade tem pouca influência direta sobre a qualidade do vinho tinto.
*  **Intervalo típico:** 0.985 a 1.030 g/cm³.
*  **Erros de medição:** Valores inferiores a 0.900 ou superiores a 1.100.
*  **Por que não remover outliers:** Outliers aqui costumam ser meras consequências matemáticas de vinhos extremamente doces (alta densidade) ou extremamente alcoólicos (baixa densidade), que já explicamos serem dados legítimos.

### 9. pH
*  **Definição:** Medida logarítmica da concentração de íons de hidrogênio livres, definindo o quão ácido ou básico o líquido é de fato.
*  **Unidade:** Adimensional (escala logarítmica).
*  **Papel enológico:** É vital para a estabilidade química, define a tonalidade da cor em tintos, e regula a eficácia protetora do SO2.
*  **Qualidade sensorial:** É negativamente correlacionado com a qualidade do vinho tinto. Vinhos com pH muito alto são percebidos como "chatos", sem vida ("flácidos").
*  **Intervalo típico:** 2.7 a 4.0. 
*  **Erros de medição:** Abaixo de 2.0 ou acima de 5.0.
*  **Por que não remover outliers:** Um pH de 4.1 ou 4.2 representa falha grave de produção, deixando o vinho suscetível a bactérias. Isso explica diretamente notas de qualidade ruins (ex: nota 3).

### 10. Sulphates (Sulfatos)
*  **Definição:** Concentração de íons sulfato, geralmente originários de aditivos como o metabissulfito de potássio ou sulfato de potássio usados na vinificação.
*  **Unidade:** g(sulfato de potássio) / dm³ (Cortez et al., 2009).
*  **Papel enológico:** Resulta da oxidação do sulfito e aditivos minerais, auxiliando na estabilização.
*  **Qualidade sensorial:** Tem uma correlação significativa e efeito positivo na qualidade do vinho tinto. Em excesso, no entanto, pode deixar o vinho amargo e duro.
*  **Intervalo típico:** 0.3 a 2.0 g/dm³. As resoluções da OIV tradicionalmente toleram um limite em torno de 2.0 a 2.5 g/L expresso em sulfato de potássio.
*  **Erros de medição:** Valores negativos ou absurdamente altos (> 5.0 g/dm³).
*  **Por que não remover outliers:** Novamente, refletem o nível tecnológico do produtor. Erros na adição geram penalidade sensorial, o que reflete a realidade do experimento.

### 11. Alcohol (Álcool)
*  **Definição:** Quantidade de etanol presente no vinho, resultante da fermentação alcoólica dos açúcares.
*  **Unidade:** % vol (Porcentagem por volume) (Cortez et al., 2009).
*  **Papel enológico:** Base estrutural do vinho. Interfere na percepção de calor, peso (corpo) e na volatilização dos compostos aromáticos.
*  **Qualidade sensorial:** É a variável que tem a maior correlação positiva com a qualidade do vinho tinto. Consumidores que buscam melhor qualidade demonstram preferência por maiores níveis de álcool.
*  **Intervalo típico:** 8.0 a 14.9 % vol (Vinhos Verdes brancos tradicionais chegam a ser mais leves, a partir de 8.5%).
*  **Erros de medição:** Menor que 4.0 % ou maior que 25.0 % (improvável num vinho não-fortificado).
*  **Por que não remover outliers:** Vinhos com teores muito altos ou muito baixos são apenas extremos de estilos enológicos (ex: muito maduro ou muito verde). Removê-los introduziria um viés de distribuição no seu dataset.


### Tabela de Resumo para Criação de Regras de Validação (Data Quality)

Esta tabela apresenta limites físicos/lógicos onde os dados podem ser considerados erros de sistema, digitação ou sensores, justificando limpeza. Qualquer valor dentro destes limites lógicos deve ser preservado (mesmo que seja um outlier estatístico visualizado num boxplot).

| Variável | Unidade | Limite Inferior (Erro se menor que) | Limite Superior Lógico (Erro se maior que) | Restrição Lógica Cruzada |
| :--- | :--- | :--- | :--- | :--- |
| fixed acidity | $g/dm^3$ | $0.0$ | $20.0$ | - |
| volatile acidity | $g/dm^3$ | $0.0$ | $5.0$ | - |
| citric acid | $g/dm^3$ | $0.0$ | $3.0$ | - |
| residual sugar | $g/dm^3$ | $0.0$ | $300.0$ | - |
| chlorides | $g/dm^3$ | $0.0$ | $2.0$ | - |
| free sulfur dioxide | $mg/dm^3$ | $0.0$ | $1000.0$ | `free_sulfur_dioxide <= total_sulfur_dioxide` |
| total sulfur dioxide | $mg/dm^3$ | $0.0$ | $1000.0$ | `total_sulfur_dioxide >= free_sulfur_dioxide` |
| density | $g/cm^3$ | $0.900$ | $1.100$ | - |
| pH | adimensional | $2.0$ | $5.0$ | - |
| sulphates | $g/dm^3$ | $0.0$ | $5.0$ | - |
| alcohol | $\%$ vol | $4.0$ | $25.0$ | - |
