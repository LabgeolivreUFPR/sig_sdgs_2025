# ODS 06: Água Potável e Saneamento

  O ODS 6 faz parte da Agenda 2030 e trata da garantia de água potável, esgotamento sanitário e gestão sustentável dos recursos hídricos. Esse objetivo engloba metas de ampliação do acesso à água tratada, redução da poluição hídrica, tratamento adequado de efluentes, proteção de mananciais e fortalecimento da gestão integrada de águas superficiais e subterrâneas.
  No Brasil, o saneamento é uma das áreas mais desiguais entre regiões. A avaliação espacial por meio de SIG é uma ferramenta essencial para apoiar políticas públicas, identificar riscos ambientais, otimizar infraestruturas e compreender padrões espaciais de vulnerabilidade. Os três mapas apresentados neste repositório dialogam diretamente com diferentes metas do ODS 6, oferecendo análises espaciais complementares que vão desde a desigualdade territorial da coleta de esgoto até o risco de contaminação e a distribuição da infraestrutura de água subterrânea.
  
## Mapas elaborados

- Taxa de Coleta de Esgoto por Estado no Brasil
- Análise de Risco: Proximidade entre Poços Tabulares e Hidrografia em Curitiba
- Distribuição Espacial e Áreas de Abrangência dos Poços Tabulares em Curitiba 

### Mapa 01: Taxa de Coleta de Esgoto por Estado no Brasil

  Este mapa apresenta um diagnóstico nacional da coleta de esgoto, utilizando uma análise coroplética por unidade federativa. A classificação foi organizada por intervalos de porcentagem, facilitando a comparação visual entre regiões brasileiras. Essa representação permite identificar padrões regionais marcantes, como a maior cobertura nas regiões Sul e Sudeste e níveis significativamente menores no Norte e Nordeste.
  A análise foi estruturada para ser intuitiva e de fácil interpretação, destacando a magnitude das desigualdades espaciais. A abordagem coroplética é adequada nesse caso, pois trabalha com valores proporcionais e permite visualizar a distribuição nacional da infraestrutura de saneamento. Foi realizada uma junção (Join Attributes by Field) entre a malha das Unidades da Federação (IBGE) e uma tabela CSV tratada contendo a taxa de coleta.
  Ao revelar desigualdades espaciais, o mapa permite identificar estados prioritários e subsidiar estratégias de universalização da coleta e tratamento de esgoto. É uma ferramenta útil para planejamento governamental e para a compreensão de como o saneamento se distribui territorialmente no Brasil.

#### Análise feita:

- Importação da malha estadual do IBGE (arquivo vetorial dos estados brasileiros);
- Importação da tabela percentual de coleta de esgoto (dados CENSO);
- Junção espacial/atributária entre tabela e polígonos dos estados (campo de sigla);
- Classificação dos dados em faixas de porcentagem usando método Jenks;
- Aplicação de paleta sequencial para representação temática;
- Adição de labels com a sigla das unidades federativas;
- Exportação via QGIS2Web (Leaflet), mantendo simbologia e legendas.

#### Simbologia Utilizada:

- Polígonos dos estados: gradiente do verde claro ao verde escuro, representando do menor ao maior percentual de coleta de esgoto;
- Borda dos estados: cinza escuro para dar estrutura ao mapa;
- Labels: siglas dos estados para identificação imediata;
- Base cartográfica para referência espacial.

### Mapa 02: Análise de Risco: Proximidade entre Poços Tabulares e Hidrografia em Curitiba

  Este mapa investiga áreas de risco de contaminação de águas subterrâneas a partir da proximidade entre poços tubulares e corpos hídricos. Poços próximos a corpos hídricos têm maior chance de sofrer infiltração de efluentes urbanos, contaminações superficiais e infiltrações difusas. O mapa permite identificar áreas críticas, auxiliando em ações de monitoramento, fiscalização e gestão dos recursos hídricos subterrâneos. Essa análise é fundamental em ambientes urbanizados como Curitiba, onde o uso da água subterrânea é intenso e a impermeabilização do solo aumenta o transporte de poluentes. A análise espacial foi realizada por meio de:

#### Análise feita:

- Importação da camada de hidrografia (linhas e polígonos) e dos poços tabulares (pontos);
- Geração de um buffer de 50 metros ao redor da hidrografia, representando área de risco maior;
- Interseção espacial entre "poços tabulares" e "buffer da hidrografia"; permitindo identificar quais poços estão dentro da zona vulnerável;
- Classificação visual:
 - poços dentro do buffer destacados em vermelho;
 - poços fora do buffer em cor diferenciada, se necessário;
- Inserção dos limites de bairros como camada de referência espacial;
- Organização da ordem das camadas para leitura clara (hidrografia → buffer → poços → limites);
- Exportação via QGIS2Web, garantindo transparência do buffer e destaque dos pontos.

A técnica de buffer é uma das ferramentas mais utilizadas em análises ambientais, pois permite identificar zonas de influência ou risco ao redor de determinados elementos geográficos. A interseção mostra objetivamente quais poços estão potencialmente mais expostos a contaminações superficiais, especialmente em áreas urbanas.

#### Simbologia Utilizada

- Rede hidrográfica (linhas): azul padrão;
- Hidrografia poligonal: azul claro, reforçando trechos mais largos;
- Buffer: laranja transparente, abrangendo 50 m ao redor dos cursos d’água;
- Poços tabulares: pontos vermelhos (poços em risco), pontos cinza escuro (poços comuns);
- Limite de bairros: bege, apenas para referência espacial;
- Base cartográfica para referência espacial.

### Mapa 03 – Distribuição Espacial e Áreas de Abrangência dos Poços Tabulares em Curitiba

O mapa fornece uma visão estratégica da distribuição da infraestrutura subterrânea, contribuindo para o manejo sustentável dos recursos de água. Foi aplicada a técnica de Polígonos de Thiessen (ou Voronoi), que divide o território em regiões de influência para cada poço. Cada polígono representa a área mais próxima de um poço específico, formando zonas de domínio espacial.Essa abordagem é muito utilizada para analisar cobertura territorial de infraestruturas, identificar vazios de atendimento, auxiliar no planejamento da ampliação de redes de monitoramento, avaliar a distribuição espacial dos recursos.
Os polígonos permitem identificar se os poços estão bem distribuídos ou concentrados, e se existem regiões extensas sem cobertura potencial de monitoramento, planejar instalação de novos poços e avaliar possíveis conflitos de uso, por exemplo.

#### Análise feita

- Importação da camada de poços tabulares (pontos);
- Aplicação do algoritmo “Polígonos de Thiessen/Voronoi” no QGIS, gerando células de influência ao redor de cada poço;
- Conversão opcional dos polígonos para camada vetorial editável, para ajustes de layout;
- Inserção das camadas de referência espacial: hidrografia, bairros e limites administrativos;
- Aplicação de simbologia categorizada nos polígonos;
- Destaque dos poços com pontos escuros como marcadores centrais do processo;
- Exportação via QGIS2Web, preservando a diferença visual entre polígonos.

#### Simbologia Utilizada

- Polígonos: Azul suave;
- Poços tabulares: pontos azul escuro;
- Bairros: contornos cinza para referência.

### Fontes de Dados

#### Mapa 1 – Nível Nacional

- Censo IBGE – Informações sobre esgotamento sanitário
https://sidra.ibge.gov.br/acervo#/A/110/T/1160

- IBGE – Malha Territorial do Brasil (Estados, 2022)
https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/15774-malhas.html

#### Mapas 2 e 3 - Curitiba

- IPPUC – Bases de Hidrografia, Limites, Bairros
https://ippuc.org.br/geodownloads/geo.htm

- Poços Tabulares – Base fornecida pela disciplina de SIG (2025)
https://siagasweb.sgb.gov.br/layout/pesquisa_complexa.php
