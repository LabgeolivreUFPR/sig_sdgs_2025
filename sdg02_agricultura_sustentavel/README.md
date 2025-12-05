ODS 2: Fome Zero e Agricultura Sustentável

O segundo Objetivo do Desenvolvimento Sustentável tem como foco principal acabar com a fome, alcançar a segurança alimentar, melhorar a nutrição e promover a agricultura sustentável. Este conjunto de mapas busca explorar relações espaciais relevantes para compreender desafios e oportunidades na produção agrícola, segurança alimentar e disponibilidade de alimentos na Região de Curitiba, a partir de dados públicos e análises geográficas.


➝  Base Cartográfica

Todo o processamento foi realizado no QGIS, utilizando dados de diferentes instituições públicas. As bases cartográficas e temáticas utilizadas foram:
 Malha Estadual – IBGE
 Uso e Cobertura do Solo (2015 e 2024) – MAPBIOMAS
 Focos de Incêndio – MAPBIOMAS
 Áreas de Preservação Permanente (APPs) – EMBRAPA
 Pontos de Centros de Abastecimento – Prefeitura Municipal de Curitiba (Dados Abertos)
 Escolas Municipais e CMEIs – IPPUC


➝  Metodologia

  MAPA 1: Expansão Agrícola vs Focos de Incêndio

A análise utilizou dados raster de uso do solo agrícola (2015 e 2024) e focos de incêndio disponibilizados pelo MAPBIOMAS. Após o recorte da área de interesse (Região Geográfica de Curitiba/IBGE), os rasters foram padronizados para resolução de 100 m e reprojetados para UTM. Em seguida, aplicou-se classificação via Raster Calculator, atribuindo o valor 1 às células correspondentes às áreas agrícolas ou aos focos de incêndio, permitindo sua vetorização.
Com os vetores gerados, foi possível calcular a distância média entre cada foco de incêndio e a área agrícola mais próxima, permitindo comparar a evolução espacial ao longo dos nove anos. Esse procedimento possibilita observar se os focos estão se aproximando ou se afastando das áreas produtivas, contribuindo para compreender padrões de pressão antrópica e risco ambiental sobre sistemas agrícolas.


  MAPA 2: Mapa Isométrico: Áreas de Preservação Permanente vs Produção Agrícola

Para identificar relações entre produção agrícola e áreas legalmente protegidas, a classe agrícola do MAPBIOMAS foi convertida para vetor e recortada à área de interesse, assim como a camada de APPs da EMBRAPA. Aplicou-se o operador de interseção, resultando em um vetor com todas as áreas onde existe sobreposição entre agricultura e APPs.
Sobre a área de estudo, foi criado um grid regular de 2500 m × 2500 m, permitindo uma representação isométrica contínua. Por meio de join espacial, os valores de sobreposição (em área) foram atribuídos a cada célula, e o grid foi classificado por gradações, destacando regiões com maior ou menor conflito entre produção e preservação.


  MAPA 3: Distribuição de Alimentos vs Escolas

Os dados de alvarás dos centros de distribuição de alimentos foram obtidos em CSV, geocodificados no Google MyMaps, convertidos para KML no Google Earth e finalmente importados para o QGIS. As escolas e CMEIs foram baixados diretamente do IPPUC já em coordenadas métricas.
A partir da camada de pontos dos centros de abastecimento (CEASA), aplicou-se o algoritmo de Polígonos de Voronoi, criando regiões equidistantes em torno de cada ponto. Um buffer de 50% foi adicionado aos polígonos, resultando em áreas de influência com alcance aproximado de até 4,5 km. Dentro de cada região de influência, foi calculado o número de escolas potencialmente atendidas por cada centro de distribuição, permitindo observar lacunas e desigualdades na rede de suprimento alimentar.


➝ Conclusão

  MAPA 1: Expansão Agrícola vs Focos de Incêndio

Os resultados mostram que os focos de incêndio não estão distribuídos aleatoriamente. Há evidente correlação espacial entre áreas agrícolas e a ocorrência de queimadas. Contudo, ao comparar as médias de distância entre 2015 e 2024, observa-se um aumento de 1,8km em 2015 para 2,4km em 2024, representando uma evolução de aproximadamente 30%.
Essa tendência indica possível melhoria na gestão territorial, alinhando-se ao ODS 2 ao reduzir riscos ambientais que comprometem a produção sustentável.


  MAPA 2: APPs vs Produção Agrícola

O mapa isométrico não revelou situações críticas para a região, mas evidencia que áreas rurais mais afastadas do centro urbano apresentam maior sobreposição entre produção agrícola e APPs, enquanto regiões de parques e áreas monitoradas mostram menor incidência.
Esse resultado reforça a importância da conciliação entre conservação ambiental e produção de alimentos, um dos pilares centrais do ODS 2, que incentiva práticas agrícolas compatíveis com a preservação de ecossistemas.


  MAPA 3: Distribuição de Alimentos vs Escolas

A localização dos centros de distribuição é pouco homogênea, concentrando-se principalmente entre Santa Quitéria e Água Verde, possivelmente por razões logísticas e proximidade com outros distribuidores. A baixa quantidade de pontos de abastecimento amplia distâncias e pode prejudicar a eficiência da distribuição de alimentos às escolas, impactando diretamente a segurança alimentar de crianças e adolescentes.
Esse cenário reforça a importância de fortalecer cadeias de abastecimento locais — uma das metas do ODS 2, que visa garantir acesso físico e econômico a alimentos de qualidade.


➝ Fontes

https://brasil.un.org/pt-br/sdgs  Acesso em 23/11/25. 
https://brasil.mapbiomas.org/#  Acesso em 23/11/25.
https://www.ibge.gov.br/geociencias/organizacao-do-territorio/divisao-regional/15778-divisoes-regionais-do-brasil.html  Acesso em 23/11/25.
https://www.embrapa.br/publicacoes-e-bibliotecas Acesso em 23/11/25.
https://dadosabertos.curitiba.pr.gov.br/ Acesso em 28/11/25.

BRUNA LOEFFLER, 05/12/2025
