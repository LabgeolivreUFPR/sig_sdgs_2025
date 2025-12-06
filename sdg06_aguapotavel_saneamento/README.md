# 🗺 Mapas de Saneamento, Saúde, Educação e Vulnerabilidade Urbana  

### Trabalho final – Sistemas de Informações Geográficas (GA222) – UFPR  

*Discente:* Arthur Dalmaz Waltrik e José Eduardo Alessi Peixoto  

*Semestre:* 2025/2  

*Acesse o mapa publicado:*

🔗 **Mapa Web:** [https://labgeolivre-ufpr.github.io/sig_sdgs_2025/sdg06_aguapotavel_saneamento/](https://labgeolivre-ufpr.github.io/sig_sdgs_2025/sdg06_aguapotavel_saneamento/)

---

## 🎯 1. Objetivo do Mapa

Os mapas produzidos analisam a relação espacial entre:

- Cobertura da rede geral de água    
- Educação (IDEB)  
- Mortalidade infantil  
- Casos de dengue  
  
O foco está em *identificar padrões regionais*, áreas críticas e desigualdades territoriais, utilizando técnicas de SIG e estatística espacial.

As perguntas orientadoras foram:

- Quais regiões apresentam maior vulnerabilidade sanitária e social?
- Como o saneamento se relaciona com saúde e educação?
- Há clusters e outliers estruturais no território?

---

## 🌍 2. ODS Relacionados

### *ODS 6 – Água Potável e Saneamento*

Metas relevantes:

- 6.1 – Acesso universal à água segura  
- 6.2 – Saneamento e higiene adequados  
- 6.b – Gestão participativa da água  

---

## 🗂 3. Descrição Geral dos Mapas

O trabalho foi organizado em seis grupos de análise:

1. *Mapa bivariado:* Água × IDEB  
2. *Análises LISA* (cluster e outliers espaciais) entre cobertura da rede geral de água e renda municipal média
3. *Comparação temporal (2010 × 2022)* da cobertura da rede geral de água e aumento populacional.
4. Comparação entre casos de dengue por 100 mil habitantes e cobertura da rede geral de água.
5. Comparação entre índice normalizado de óbitos infantis e cobertura da rede geral de água.
6. *LISA de cobertura da rede geral de água*

Cada etapa utiliza métodos estatísticos e geoespaciais replicáveis no QGIS .

---
  
# 📊 4. Análises Realizadas

---

## 🔵 4.1. Água × IDEB

- Grande parte dos municípios apresenta condições *intermediárias ou favoráveis* (classes bivariadas 2–2, 2–3 e 3–2).  
- Regiões *centro–norte* mostram forte associação entre *alta cobertura da rede geral de água* e *IDEB elevado*.  
- Áreas no *extremo sul e leste* destacam-se na classe 1–1 (baixa água × baixo IDEB).  
- Casos discrepantes indicam fatores educacionais independentes da infraestrutura.

---

## 🔵 4.2. Saúde Pública: Saneamento vs. Agravos

Esta seção analisa a relação espacial entre a cobertura da rede geral de água e os indicadores de saúde (Mortalidade Infantil e Dengue).

### 👶 *Mortalidade Infantil*
* *Padrão:* O mapa de símbolos proporcionais (círculos de óbitos) não mostra concentração óbvia nas áreas de baixa cobertura de água (fundo claro).
* *Destaque:* Há ocorrência de altas taxas de mortalidade (círculos grandes) em áreas de *alta cobertura de água*.
* *Conclusão:* A Mortalidade Infantil no Paraná, neste estágio de desenvolvimento, está mais relacionada a *fatores sistêmicos* (acesso e qualidade dos serviços de saúde pré-natal e neonatal) do que a uma correlação direta com a ausência de água encanada.

### 🦟 *Dengue*
* *Padrão:* Observa-se um *cluster de alta incidência de dengue* (grandes círculos) nas regiões *Norte, Noroeste e Oeste*.
* *Contradição:* Essa concentração de casos ocorre majoritariamente em áreas de *alta cobertura de água* (fundo azul escuro).
* *Conclusão:* A distribuição da Dengue é primariamente influenciada por *fatores bioclimáticos* (temperatura e umidade) e *urbanos* (densidade e manejo de resíduos), e *não* pela deficiência no acesso à rede geral de água. A doença persiste mesmo com a universalização do saneamento hídrico.

---

## 🔵 4.3. Comparação LISA (Cobertura de Água × Renda Média)

Esta análise confronta a infraestrutura básica com a riqueza municipal, revelando um *descompasso espacial* no território paranaense.

### 🔴 Legenda (Padrão LISA)
* *High-High (Vermelho):* Cluster de Alta.
* *Low-Low (Azul Escuro):* Cluster de Baixa.
* *Low-High (Azul Claro):* Outlier / "Buraco".
* *High-Low (Amarelo):* Outlier / "Ilha".

### 📋 Análise Comparativa
1.  *Polarização da Infraestrutura (Água):* O cluster *High-High* de água está consolidado no *Norte e Norte-Central. O cluster **Low-Low* forma uma grande mancha no *Centro-Sul*.
2.  *Polarização da Renda:* O cluster *High-High* de renda concentra-se em regiões de forte *agronegócio (Oeste e Sudoeste)*.
3.  *O Paradoxo do Sudoeste:* O Sudoeste é um cluster *HH de Renda, mas está inserido no cluster **LL de Cobertura de Água*.
    * *Interpretação:* A alta renda em áreas rurais não exige a rede geral de água, com predominância de soluções individuais (poços). A falta de cobertura de rede não é, necessariamente, um indicador de pobreza nessa região, mas sim de *característica de uso da terra*.

---

## 🔵 4.4. Variação Temporal da Cobertura da Rede Geral de Água (2010 × 2022)

A evolução da cobertura demonstra progresso na maior parte do estado, mas com zonas de retrocesso.

* *Expansão (Aumento):* Predominância na metade *Leste e Sul*, indicando que os investimentos em saneamento superaram o crescimento populacional, elevando o índice de atendimento no período.
* *Retração (Redução - Azul):* Manchas no *Oeste e Noroeste*.
    * *Alerta:* Nesses municípios, o percentual de cobertura da rede geral *diminuiu, sugerindo que a infraestrutura **não acompanhou o crescimento populacional acelerado* ou que houve falhas de manutenção/gestão que diluíram a taxa de cobertura total.

---

## 🔵 4.5. LISA da Cobertura da Rede Geral de Água

A análise LISA univariada confirma a *polarização espacial* do saneamento básico.

* *Cluster Alto-Alto (HH):* Predomina no *Norte e Norte-Central*. É a "zona de consolidação" da infraestrutura, onde municípios com bons índices são vizinhos de outros com o mesmo perfil.
* *Cluster Baixo-Baixo (LL):* Extensa mancha no *Centro-Sul. Representa um **déficit estrutural e regionalizado*; a precaridade do acesso à água de um município tende a se repetir no vizinho.
* *Outliers (Alto-Baixo e Baixo-Alto):* Zonas de transição e desigualdade intra-regional. Indicam ilhas de excelência cercadas por precariedade, ou vice-versa.

---

# 📦 5. Fontes de Dados

- *IBGE* – Censo e indicadores municipais  
- *SNIS / ANA* – Dados de saneamento  
- *DATASUS / SISAB* – Saúde  
- *GeoDa / QGIS* – Processamento estatístico e geoespacial  

---

# 🛠 6. Processamento em SIG

1. Importação dos dados (IBGE, SNIS, DATASUS)  
2. Junção espacial com os municípios  
3. Normalização e padronização dos indicadores
	- Para evitar distorções causadas por valores extremos e diferenças populacionais entre municípios, foram aplicadas transformações logarítmicas aos dados.
		- *Mortalidade infantil:* aplicada transformação log₁₀ diretamente às contagens de óbitos:
				$$\text{taxa de óbitos infantis normalizada} = \log_{10}({\frac{\text{óbitos infantis por município}}{\text{população total por município}}+1)}$$
		- *Casos de dengue:* inicialmente foi calculada a taxa por 100.000 habitantes, seguida de transformação log₁₀:
				 $$\text{casos de dengue por 100 mil habitantes} = (\frac{\text{casos de dengue por município}}{\text{população total por município}}) \times 100.000$$
				 $$\text{taxa de casos de dengue por 100 mil habitantes} = \log_{10}{(\text{casos de dengue por 100 mil habitantes} + 1)}$$
4. Construção das matrizes bivariadas (3×3)  
5.  Criação de mapas para 2022 e 2010
6. Criação de simbologias graduadas com base nos indicadores
7.  Geração de LISA global e local 
8. Exportação em GeoJSON / PNG para publicação no GitHub  

