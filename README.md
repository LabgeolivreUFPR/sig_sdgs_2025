# ODS 11: CIDADES E COMUNIDADES SUSTENTÁVEIS

## 1. Objetivo do Mapa

Este projeto visa aplicar técnicas avançadas de Sistemas de Informação Geográfica (SIG) para diagnosticar, em Curitiba, os desafios relacionados à
equidade no acesso a infraestruturae àvulnerabilidade socioespacial, em alinhamento direto com oObjetivo de Desenvolvimento Sustentável 11 (Cidades Sustentáveis).
A análise demonstra o potencial das geotecnologias para a geração de conhecimento aplicado ao planejamento urbano e à tomada de decisão. 
O mapa web interativo (Leaflet) serve como plataforma de disseminação, permitindo a visualização das zonas de alta demanda (Hotspots), as áreas de cobertura real 
de serviços e as carências infraestruturais.

---

## 2. Descrição das Análises

 O projeto compõe-se de três análises espaciais principais, representando diferentes modelos de dados (Vetorial, Raster e Rede), conforme a ementa da disciplina 

| Camada | Meta ODS | Modelo de Dados | Função Analítica |
| :--- | :--- | :--- | :--- |
|Cobertura de Lazer por Bairro| 11.7 | Polígono (Coroplético) | Mede a disponibilidade de espaços públicos normalizada pela demanda populacional. |
|Acessibilidade ao Transporte| 11.2 | Polígono (Rede/Isócronas) | Quantifica o alcance temporal a pé aos Terminais, avaliando a eficácia da rede de mobilidade. |
|Hotspots de Ocupação Irregular| 11.1 | Raster (Densidade) | Identifica os núcleos de maior concentração e pressão por moradia, indicando vulnerabilidade social. |

---

## 3. Detalhamento da Metodologia e Simbologia

### 3.1. Cobertura de Lazer por Bairro (Índice {m}^2/{Hab}
A análise visa criar um indicador deEquidadede acesso a espaços públicos.
 Processamento:O índice é umCálculo de Proporção. Inicialmente, utilizou-se a ferramentaUnir Atributos por Local (Spatial Join)com a funçãoSomapara agregar 
a área total das feições de Área Verde dentro do polígono de cada Bairro (Camada Base). Posteriormente, aTabela de População (IBGE)foi incorporada viaJoin de Atributos . 
O índice final {m}^2/{Hab} foi calculado naCalculadora de Campo.
 Simbologia:Graduada (Coroplética)com a classificaçãoQuebras Naturais de Jenks. O gradiente de verde reforça a leitura do recurso natural, onde a tonalidade mais 
escura corresponde à maior disponibilidade de recurso por habitante.

### 3.2. Acessibilidade ao Transporte (Isócronas)
A análise foca naAcessibilidade de Primeiro/Último Quilômetroe na eficácia da integração da rede.
 Processamento:É umaAnálise de Redebaseada noTempo de Viagem('Time'). Os pontos de Terminais de Ônibus (Origem) foram validados no SRCEPSG:4326e o plugin
ORS Tools(acesso à rede OpenStreetMap) foi configurado com o perfil'walking'(caminhada) para Meta 11.2. O cálculo gerou polígonos de alcance para os intervalos de10, 20 e 30 minutos.
 Simbologia:Categorizada por Tempo. As Isócronas são representadas com transparência para visualizar as áreas de sobreposição e a diferença de tempo no alcance da rede viária.

### 3.3. Hotspots de Ocupação Irregular
Esta análise utiliza a densidade para identificar focos de alta pressão social e vulnerabilidade.
 Processamento:É umaAnálise Raster de Densidade. Os Polígonos de Ocupação foram convertidos emCentróides(Pontos) para servir como insumo discreto. A ferramenta
Estimativa de Densidade Kernelfoi aplicada, criando uma superfície contínua (Raster) que mapeia a intensidade da concentração.
 Simbologia:Falsa Cor de Banda Única(Mapa de Calor). O gradiente (ex: de baixa densidade para Hotspot) ilustra a concentração, com o Raster sobreposto aos contornos dos
Bairros para contextualização administrativa.

---

## 4. Infraestrutura de Dados Espaciais (IDE) e Fontes

 O projeto utiliza o conceito de IDE, integrando dados de múltiplas fontes governamentais e colaborativas.

 Geometrias (Bairros, Ciclovias, Terminais, Área Verde):IPPUC – Dados Abertos da Prefeitura de Curitiba.
 Dados Populacionais e Malha Censitária:IBGE – Censo (Insumos para a normalização social).
 Rede de Roteamento:OpenStreetMap (via plugin ORS Tools).
 Publicação Web:Utilização do QGIS2Web (opção Leaflet) para transformar o projeto desktop em um geo-serviço acessível via web.
 Software Utilizado:QGIS 3.40 (Ambiente de Geotecnologia Livre).

---

## 5. Processo de Entrega e Publicação Web (GitHub Pages)

1.O projeto foi unificado ('.qgz') com as três análises e a simbologia finalizada.
2.A exportação foi realizada usando o pluginQGIS2Web(opçãoLeaflet), gerando a pasta de arquivos web ('index.html', 'data/', 'css/', 'js').
3.Os arquivos foram copiados para o diretório 'sdg11_cidades_sustentaveis/' e enviados para o repositório GitHub.

## 6. Acesse o Mapa Publicado

🔗Mapa Web (Exemplo):'file:///C:/sdg11_cidades_sustentaveis/qgis2web_2025_12_01-21_56_47_585823/index.html#11/-25.4966/-49.3595'

