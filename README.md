Com base nos metadados originais de Cortez et al. (2009), nas diretrizes oficiais da OIV (Organização Internacional da Vinha e do Vinho), nas especificações do arquivo winequality.names, e na literatura complementar do artigo Measuring Wine Quality and
Typicity, apresento o detalhamento e as restrições lógicas para cada variável.

**1. Fixed acidity (Acidez fixa)**

* **Definição:** Representa os ácidos orgânicos não voláteis do vinho, predominando o ácido tartárico, málico, cítrico e succínico.
* **Unidade:** g/dm³ expresso em equivalente de ácido tartárico (Cortez et al., 2009).
* **Papel enológico:** Fornece a estrutura química básica ("esqueleto") do vinho, essencial para sua estabilidade microbiológica e categorização.
* **Qualidade sensorial:** Responsável pela percepção de vivacidade e frescor. A carência torna o vinho "chato" ou plano; o excesso gera forte adstringência e acidez agressiva.
* **Intervalo típico:** O dataset UCI apresenta variação entre $3.8$ e $15.9$ g/dm³.
* **Erro de medição:** Valores $< 0$ (impossível) ou superando níveis biologicamente viáveis de um mosto vinificável (ex: $> 30$ g/dm³).
* **Por que não remover:** Vinhos de climas extremos ou colheitas precoces atingem valores de acidez legítimos, porém extremamente altos, alterando sua representatividade e pontuação sensorial de modo real.

**2. Volatile acidity (Acidez volátil)**

* **Definição:** Medida dos ácidos destiláveis a vapor, primariamente o ácido acético resultante de subprodutos da fermentação e do metabolismo bacteriano.
* **Unidade:** g/dm³ expresso em equivalente de ácido acético (Cortez et al., 2009).
* **Papel enológico:** É o principal indicativo do estado sanitário da bebida e de falhas microbiológicas.
* **Qualidade sensorial:** Acima dos limiares de tolerância, gera defeitos (aromas de vinagre ou removedor de esmalte). Entretanto, há raríssimas exceções em que taxas consideradas falhas adicionam apreciada complexidade organoléptica, como ocorreu no tinto Cheval Blanc de 1947.
* **Intervalo típico:** Varia entre $0.08$ e $1.58$ g/dm³. A OIV define o limite regulatório padrão para vinhos comuns próximo a $1.2$ g/L.
* **Erro de medição:** $< 0$ ou artificialmente superior a limites onde a bebida seria essencialmente vinagre balsâmico industrial ($> 4.0$ g/dm³).
* **Por que não remover:** Vinhos como o de $1.58$ g/dm³ violam as leis de mercado e representam uma falha, porém devem receber notas severamente baixas na variável de saída. Remover esse outlier impede o modelo de aprender os padrões de um vinho tecnicamente defeituoso.

**3. Citric acid (Ácido cítrico)**

* **Definição:** Ácido orgânico que pode estar em pequenas proporções naturais ou ser injetado artificialmente durante o processo como regulador.
* **Unidade:** g/dm³ (Cortez et al., 2009).
* **Papel enológico:** Acidificação rápida e estabilização de turbidez.
* **Qualidade sensorial:** Auxilia o perfil ácido a se tornar levemente mais cortante ou fresco, porém pode resultar em cheiros lácteos ("manteiga") se atacado por bactérias.
* **Intervalo típico:** $0.0$ a $1.66$ g/dm³. A OIV limita a adição externa a no máximo $1$ g/L.
* **Erro de medição:** $< 0$ ou acima de patamares de saturação de acidificação irreal (ex: $> 5.0$ g/dm³, o que indicaria erro na casa decimal inserida).
* **Por que não remover:** Reflete práticas intervencionistas de adegas diferentes; doses cavalares explicam rejeições sensoriais da prova.

**4. Residual sugar (Açúcar residual)**

* **Definição:** Glicose e frutose residuais não convertidas em etanol no fim da fermentação alcoólica.
* **Unidade:** g/dm³ (Cortez et al., 2009).
* **Papel enológico:** Parâmetro decisivo de classificação e precificação das categorias técnicas (Seco, Meio Seco, Doce, etc.).
* **Qualidade sensorial:** Modula severamente o "corpo" do vinho e precisa ser contrabalançado perfeitamente com a acidez natural e com a agressividade do álcool para harmonizar o produto.
* **Intervalo típico:** Varia absurdamente de $0.6$ a $65.8$ g/dm³ na base UCI. A OIV descreve patamares de $\le 4$ g/L (vinhos secos) até limites abertos $> 45$ g/L (vinhos de sobremesa).
* **Erro de medição:** $< 0$ ou superior à capacidade hídrica do mosto (xaropes saturados em excesso de $350$ g/dm³ não constituiriam um líquido vinificável com etanol).
* **Por que não remover:** Ice Wines e Vinhos de Colheita Tardia comporão estatisticamente pequenos "ilhas" isoladas de açúcar extremo em meio a milhares de vinhos secos, gerando assimetria nas classes. Remove-los destrói inteiramente o aprendizado de estilos enológicos legítimos.

**5. Chlorides (Cloretos)**

* **Definição:** Sais inorgânicos dissociados expressando a salinidade da bebida (advindos muitas vezes do solo).
* **Unidade:** g/dm³ expresso em equivalente de cloreto de sódio (Cortez et al., 2009).
* **Papel enológico:** Componente inorgânico residual muitas vezes oriundo do lençol freático das vinhas ou processos de clarificação.
* **Qualidade sensorial:** Ajuda no peso da mineralidade. Extremos geram amargor e gosto salino atípico rejeitado por provadores.
* **Intervalo típico:** $0.009$ a $0.611$ g/dm³.
* **Erro de medição:** $< 0$ ou picos salgados de água do mar intragáveis ($> 2.0$ g/dm³).
* **Por que não remover:** A salinidade é um biomarcador essencial do *terroir* das parcelas geográficas (como planícies calcárias costeiras).

**6. Free sulfur dioxide (SO2 livre)**

* **Definição:** Forma solúvel gasosa e íons ativos (bissulfito e sulfito) que permanecem soltos na matriz coloidal do líquido.
* **Unidade:** mg/dm³ (Cortez et al., 2009).
* **Papel enológico:** O preservativo essencial, com ação antioxidante e bactericida para bloquear contaminações.
* **Qualidade sensorial:** Subdosagens causam quebras de cor (escurecimento e "browning") e traços oxidativos como o aldeído. Superdosagens causam sensação pungente nas vias aéreas e aromas grosseiros de enxofre ou "fósforo riscado".
* **Intervalo típico:** De $1.0$ a cerca de $289$ mg/dm³. A OIV recomenda níveis estocados próximos de $25$ mg/L (tintos) e $30$ mg/L (brancos).
* **Erro de medição:** $< 0$, valor absoluto irreal (ex: $> 500$ mg/dm³) ou, de forma crucial, valor superior ao **total sulfur dioxide**.
* **Por que não remover:** Um número atípico alto de SO2 livre penaliza sensivelmente a percepção nasal. Ele é uma intercorrência da vinificação que necessita estar nos dados.

**7. Total sulfur dioxide (SO2 total)**

* **Definição:** Quantidade bruta, resultante de todas as formas (livres e ligadas estruturalmente às proteínas e fenóis) adicionadas.
* **Unidade:** mg/dm³ (Cortez et al., 2009).
* **Papel enológico:** Critério central da inspeção legal que barra a distribuição do vinho por toxicidade humana.
* **Qualidade sensorial:** Modifica drasticamente o tempo de vida do vinho e encobre frutados delicados se exagerado.
* **Intervalo típico:** $6$ a $440$ mg/dm³. Limites máximos toleráveis da OIV oscilam de $150$ a cerca de $400$ mg/L, estendidos a vinhos que possuam altíssimo teor de açúcar livre propenso à re-fermentação.
* **Erro de medição:** $< 0$ ou discrepâncias absurdas como $> 1000$ mg/dm³.
* **Por que não remover:** A legislação permite altíssimas injeções em vinhos doces de alta qualidade. Tais vinhos aparecerão nas avaliações estatísticas como concentrações massivas anormais.

**8. Density (Densidade)**

* **Definição:** Razão da massa do vinho sobre um referencial de volume.
* **Unidade:** g/cm³ (Cortez et al., 2009).
* **Papel enológico:** Derivado de interações físicas puras, balanceando a água ($\sim 1.0$) frente a carga alcóolica redutora ($\text{etanol} = 0.789$) e carga sólida aditiva ($\text{açúcares minerais} > 1.0$).
* **Qualidade sensorial:** Influencia o nível de extração e a textura pesada e espessa em boca (ou "body").
* **Intervalo típico:** Próximo à densidade da água: de $0.987$ a $1.038$ g/cm³.
* **Erro de medição:** $< 0.789$ g/cm³ (o mosto seria literalmente menos denso que álcool etílico puro) ou maior que $1.150$ g/cm³.
* **Por que não remover:** Uma densidade de $1.03$ denuncia que o líquido possui muito açúcar e álcool simultâneos, não indicando erro do equipamento laboratorial, mas apenas um produto untuoso.

**9. pH**

* **Definição:** Medida da atividade exponencial logarítmica de íons hidrogênio do meio.
* **Unidade:** Adimensional na escala de pH (Cortez et al., 2009).
* **Papel enológico:** Base fundamental para gerir toda reatividade da garrafa. Aumentos de pH diminuem exponencialmente a eficiência ativa do SO2.
* **Qualidade sensorial:** Influencia drasticamente a cor e o frescor estrito. pH altos são propensos a ataques fétidos de leveduras selvagens.
* **Intervalo típico:** Oscila de $2.7$ a $4.0$.
* **Erro de medição:** $< 2.0$ ou $> 5.0$ (vinhos comerciais se degradam quimicamente ao cruzar esses limiares; apontam quebra mecânica do eletrodo de leitura, descalibração ou erro humano de digitação de casa decimal).
* **Por que não remover:** Um pH isolado de $4.1$ é perigosamente base, mas acontece em climas secos em safras atípicas. É verídico e explica deficiências.

**10. Sulphates (Sulfatos)**

* **Definição:** Extrato de ânions de potássio na matriz resultante da sulfatação do mosto e quebra biológica.
* **Unidade:** g/dm³ expresso em equivalente de sulfato de potássio (Cortez et al., 2009).
* **Papel enológico:** Ligado à estabilização de mostos tintos ou a acidez indireta de regiões secas (prática de "plastering").
* **Qualidade sensorial:** Produzem impactos discretos de limpeza salina ou traços adstringentes metálicos se extrapolados.
* **Intervalo típico:** $0.22$ a $2.0$ g/dm³.
* **Erro de medição:** $< 0$ ou picos irreais ($> 10.0$ g/dm³).
* **Por que não remover:** Retrato das particularidades produtivas de diferentes enólogos.

**11. Alcohol (Álcool)**

* **Definição:** Percentagem etílica oriunda estritamente pela digestão fermentativa.
* **Unidade:** % vol. (Cortez et al., 2009).
* **Papel enológico:** Fornece a identidade taxonômica oficial e conservação ao vinho, cujas métricas basais são defendidas pela OIV a $\ge 8.5\%$ vol, permitindo reduções regionais até $7\%$.
* **Qualidade sensorial:** Imprime calor na boca, eleva o corpo e dilui traços secos, porém, quando extrapolado pelas mudanças climáticas ou desajustado, ele domina excessivamente o conjunto, gerando queimação irritante.
* **Intervalo típico:** $8.0$ a $14.9\%$ vol no dataset UCI.
* **Erro de medição:** $< 0$ ou acima do limiar biológico absoluto em que a própria levedura sucumbe ($> 22.0\%$ vol).
* **Por que não remover:** Níveis de extrema base como $8.0\%$ não são erros e referem-se à tipicidade climática dos vinhos portugueses originais do dataset ("Vinho Verde").

### Tabela de Validação e Consistência (Data Quality Rules)

Abaixo está o roteiro de regras para aplicação nas suas pipelines de pré-processamento. Apenas registros que ultrapassarem os **Limites Físicos Absolutos** devem ser classificados como *erros de digitação/dado corrompido*.

| Variável Físico-Química | Tipo de Dado | Limite Físico (Corrupção) Mín. | Limite Físico (Corrupção) Máx. | Regra Lógica Interdependente |
| --- | --- | --- | --- | --- |
| **fixed acidity** | numérico | $< 0.0$ | $> 30.0$ | - |
| **volatile acidity** | numérico | $< 0.0$ | $> 4.0$ | - |
| **citric acid** | numérico | $< 0.0$ | $> 5.0$ | - |
| **residual sugar** | numérico | $< 0.0$ | $> 350.0$ | - |
| **chlorides** | numérico | $< 0.0$ | $> 2.0$ | - |
| **free sulfur dioxide** | numérico | $< 0.0$ | $> 500.0$ | $\le \text{total sulfur dioxide}$ |
| **total sulfur dioxide** | numérico | $< 0.0$ | $> 1000.0$ | $\ge \text{free sulfur dioxide}$ |
| **density** | numérico | $< 0.789$ | $> 1.150$ | - |
| **pH** | numérico | $< 2.0$ | $> 5.0$ | - |
| **sulphates** | numérico | $< 0.0$ | $> 10.0$ | - |
| **alcohol** | numérico | $< 0.0$ | $> 22.0$ | - |
