# RELATÓRIO TÉCNICO: PROJETO SIG & ODS 11
**Análise Espacial de Adequabilidade e Acessibilidade Cicloviária em Curitiba/PR**

**Aluno:** Halan Patrick Pereira Nowak  

---

## 1. Acesso aos Produtos Finais

### Aplicação Web (WebGIS)
O mapa interativo contendo todas as camadas processadas e funcionalidades de navegação está publicado e acessível através do link abaixo:
* **Link de Acesso:** [https://labgeolivre.github.io/sig_sdgs_2025/sdg11_cidades_sustentaveis/](https://labgeolivreufpr.github.io/sig_sdgs_2025/sdg11_cidades_sustentaveis/)

### Pranchas Cartográficas (Download PDF)
Para visualização estática e impressão em alta resolução (formato A4), disponibilizam-se os seguintes arquivos:
* **[Mapa 01: Índice de Adequabilidade Cicloviária (PDF)](pdfs/mapa1.pdf)**
* **[Mapa 02: Acessibilidade Temporal aos Terminais (PDF)](pdfs/mapa2.pdf)**
* **[Mapa 03: Esforço Físico e Declividade Viária (PDF)](pdfs/mapa3.pdf)**

---

## 2. Resumo e Objetivos
Este projeto técnico tem como objetivo aplicar rotinas de Geoprocessamento e Análise Espacial para avaliar a infraestrutura de mobilidade ativa na cidade de Curitiba/PR. O estudo foca na identificação de áreas prioritárias para expansão da malha cicloviária, análise de barreiras físicas impostas pelo relevo e mensuração da acessibilidade temporal aos terminais de transporte público, visando a integração intermodal.

O trabalho foi desenvolvido alinhado ao **Objetivo de Desenvolvimento Sustentável 11 (Cidades e Comunidades Sustentáveis)** da ONU, especificamente na meta de proporcionar acesso a sistemas de transporte seguros, acessíveis e sustentáveis para todos.

---

## 3. Metodologia e Procedimentos Técnicos
Todo o processamento vetorial e matricial foi realizado utilizando o software **QGIS 3.34.5**. Abaixo, o detalhamento dos métodos aplicados para cada produto cartográfico:

### 3.1. Mapa 01: Índice de Adequabilidade (MCDA)
Foi aplicada uma **Análise Multicritério (MCDA)** baseada na Álgebra de Mapas para gerar um índice contínuo de adequabilidade (0 a 10).
* **Variáveis:** Declividade do terreno, Densidade Demográfica e Proximidade de Polos Geradores de Viagem (Escolas e Comércios).
* **Processamento:** As variáveis foram rasterizadas e normalizadas (Fuzzy). Em seguida, aplicou-se uma Soma Ponderada, onde a Declividade e a Densidade receberam os maiores pesos.
* **Resultado:** Identificação de vetores de expansão em áreas com topografia favorável e alta demanda latente.

### 3.2. Mapa 02: Acessibilidade Temporal (Isócronas)
Análise de redes para mensurar a eficiência da integração entre a bicicleta e o transporte coletivo.
* **Ferramenta:** Plugin **QNEAT3** (Algoritmo *Iso-Area as Interpolation*).
* **Parâmetros:** Utilizou-se a malha viária oficial do IPPUC com topologia corrigida. A velocidade média estipulada para o ciclista foi de 15 km/h.
* **Resultado:** Geração de áreas de serviço (isócronas) classificadas por tempo de deslocamento até os Terminais de Transporte. Áreas classificadas em azul (< 5 min) indicam alta potencialidade para integração modal.

### 3.3. Mapa 03: Esforço Físico (Declividade Viária)
Classificação da rede viária existente conforme a inclinação longitudinal, destacando barreiras físicas naturais.
* **Processamento:** Extração de valores do Modelo Digital de Terreno (MDT) para os segmentos de logradouros via Estatística Zonal.
* **Otimização de Desempenho (Nota Técnica):** Devido à alta densidade da malha viária de Curitiba (superior a 50.000 segmentos), optou-se pela conversão da camada vetorial final para o formato **Raster (.tif)**. Esta técnica foi necessária para garantir a fluidez da renderização na interface WebGIS (Leaflet), evitando sobrecarga de processamento no navegador do usuário.

---

## 4. Fonte de Dados
A base de dados geoespaciais foi constituída a partir de fontes oficiais e dados abertos:

1.  **IPPUC (2024):** Base cartográfica oficial de Curitiba, contendo eixos de logradouros, sistema cicloviário, localização dos terminais de transporte e limites administrativos.
    * Fonte: [https://ippuc.org.br/geodownloads/geo.htm](https://ippuc.org.br/geodownloads/geo.htm)
2.  **TOPODATA (INPE):** Modelo Digital de Terreno (MDT) e variáveis geomorfométricas derivadas do SRTM.
    * Fonte: [http://www.dsr.inpe.br/topodata/index.php](http://www.dsr.inpe.br/topodata/index.php)
3.  **IBGE (Censo 2022):** Malha de setores censitários e dados agregados de população residente.
    * Fonte: [https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais.html](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais.html)

---

## 5. Processo de Publicação Web
A publicação do WebGIS utilizou a biblioteca **Leaflet**, gerada através do plugin **QGIS2Web**, com as seguintes customizações de Front-end implementadas diretamente no código fonte (HTML/CSS/JS):

1.  **Interface de Navegação:** Desenvolvimento de um menu inferior fixo ("Dock") para alternância rápida entre os mapas temáticos.
2.  **Narrativa Interativa:** Implementação de um painel lateral dinâmico que atualiza as informações técnicas e metodológicas conforme a camada ativa selecionada.
3.  **Gerenciamento de Camadas:** Criação de um controle de camadas personalizado (Layer Control) para permitir a visualização seletiva dos dados.
4.  **Legendas Externas:** Utilização de imagens estáticas para as legendas complexas (gradientes raster), garantindo a fidelidade visual do projeto cartográfico original.

