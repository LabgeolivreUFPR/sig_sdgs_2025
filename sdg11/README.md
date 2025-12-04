# Mapa do Transporte Público da URBS

Trabalho final da disciplina de Sistemas de Informações Geográficas (GA222) da Universidade Federal do Paraná do semestre 2025/2 realizada pelos discentes Christopher Pinheiro Dobb e João Victor Correia Stoski.

## 1. Objetivo do Mapa
Este mapa apresenta a distribuição geográfica e a abrangência das diferentes categorias de linhas de ônibus que compõem o sistema de transporte público de Curitiba da rede URBS.

Ele serve como uma visualização fundamental para a análise da cobertura espacial do serviço na cidade, auxiliando na avaliação da meta 11.2 do ODS 11, 
que busca _"Proporcionar o acesso a sistemas de transporte seguros, acessíveis, sustentáveis e a preço acessível para todos"_.

## 2. SDG Relacionado
### SDG 11 – Cidades e Comunidades Sustentáveis 
<!-- > O Objetivo 11 busca tornar as cidades e os assentamentos humanos inclusivos, seguros, resilientes e sustentáveis. A Meta 11.2 tem como foco o acesso a sistemas de transporte público seguro, acessível e sustentável. -->
> Tornar as cidades e os assentamentos humanos inclusivos, seguros, resilientes e sustentáveis. Inclui o accesso à habitação adequada e acessível, proteção do patrimônio cultural e natural, redução do impacto ambiental urbano, aumento da resiliênia contra desastres e fortalecimento do transporte público.

## 3. Descrição do Mapa
O mapa possui duas categorias de camadas, "linhas" e "fundo", em que somente um de cada pode ser habilitado simultaneamente:
> Todas as camadas desta categoria utilizarão o [conjunto de dados disponibilizado pelo IPPUC via MapServer](https://geocuritiba.ippuc.org.br/server/rest/services/GeoCuritiba/URBS_Transporte_Publico/MapServer).

### 3.1. Linhas
Apresenta as diversas linhas de ônibus da rede URBS, representando-as com os temas:


**3.1.1. Capacidade do ônibus:** a média da quantidade de pessoas que podem ocupar o tipo de ônibus da linha.

Quanto mais verde, maior é a capacidade, quanto mais avermelhado, menor.
> À partir da [tabela disponibilizada pela URBS](https://www.urbs.curitiba.pr.gov.br/transporte/rede-integrada-de-transporte/42), realiza-se uma média ponderada da capacidade de cada categoria de ônibus, e depois é feito um _join_ na camada das linhas.

**3.1.2. Linha de turismo:** mostra a linha dedicada ao turismo, que passa pelos pontos mais atrativos da cidade. Inclui os pontos de parada e os parques que são observados.
> Isolando a linha de turismo com `categoria_servico='JARDINEIRA'`, tendo os pontos de parada de parada do conjunto do MapServer, e os polígonos dos parques nos [Geodownloads do IPPUC](https://ippuc.org.br/geodownloads/geo.htm):
> 1. Cria-se um buffer de 50 metros na linha de turismo;
> 2. Extrai-se os pontos de paradas contidos nesse buffer;
> 3. Extrai-se os polígonos que interceptam o buffer.

**3.1.3. Períodos de passagem da linha:** representa o tempo médio da passagem de dois ônibus consecutivos nos terminais da linha, em dias úteis. Pode ser analizado o período geral (dia inteiro), nos horários de pico ou fora deles.

Quanto menor esse período (verde), mais frequentemente o ônibus passa, quanto maior (vermelho), a passagem é menos frequente.
> Utiliza-se a rotina em `python/get_schedule.py` para consultar a [tabela de horários](https://www.urbs.curitiba.pr.gov.br/horario-de-onibus) de todas as linhas contidas em `python/cod_linhas.csv`, escrevendo um .JSON com as chegadas em minutos desde o início do itinerário (5:00). Com isso, usa-se a rotina `python/get_periods.py` junto ao GeoPackage das linhas de ônibus do MapServer para obter os valores médios de passagem nas categorias apresentadas.

### 3.2. Fundo
Apresenta informações sobre o acesso local às linhas de ônibus:

**3.2.1. Densidade de pontos por bairro:** demonstra a proporção de pontos de parada pela área do bairro que as contém.

Quanto mais escuro a coloração do bairro, maior é sua densidade.
> Usando a divisão de bairros dos [Geodownloads do IPPUC](https://ippuc.org.br/geodownloads/geo.htm), utiliza-se a função de contagem de pontos do QGIS com os pontos de parada do conjunto do MapServer. Dividindo esse valor pela área de cada bairro, obtem-se a densidade de pontos.

**3.2.2. Cobertura dos terminais:** com a divisão em polígonos, representa qual o terminal mais próximo de qualquer ponto da cidade, levando em consideração a malha viária e desconsiderando velocidades e sentidos.
> 1. Para cada terminal, usa-se a função `v.net.alloc` do GDAL com os [eixos de vias do IPPUC](https://ippuc.org.br/geodownloads/geo.htm) , obtendo-se uma malha com identificadores para cada terminal;
> 2. Obtem-se os centroides de cada linha da malha criada, que preservam os atributos de suas respectivas linhas;
> 3. Criam-se polígonos de Voronoi para estes pontos, dissolvendo-os em relação ao identificador do terminal;
> 4. Corrige-se as bordas desse conjunto de polígonos com o limite municipal de Curitiba pelos [dados do IPPUC](https://ippuc.org.br/geodownloads/geo.htm).

**3.2.3. População das coberturas:** à partir das áreas das abrangências dos terminais, os colore em função da quantidade da população contida.

Quanto mais escuro a coloração da área, maior é a população contida.
> 1. Relacionando a [camada vetorial](https://ippuc.org.br/geodownloads/geo.htm) dos setores censitários do IBGE do censo de 2022 em Curitiba com os respectivos dados sobre a [quantidade de pessoas por setor](https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html), realiza-se um join que atribui o último à camada espacial;
> 2. Calcula-se a área de cada setor, que é salva em um campo da camada;
> 3. Realiza-se a operação "intercessão" dos setores com a camada das abrangências;
> 4. Calcula-se a nova área de cada setor;
> 5. Estima-se uma nova população com uma proporção com a área antiga;
> 6. Realiza-se uma agregação de todos os setores em relação à abrangência que os contêm, realizando a soma da nova população de cada.

## 4. Acesse o Mapa Publicado
Link para visualização web: [https://labgeolivreufpr.github.io/sig_sdgs_2025/sdg11/](https://labgeolivreufpr.github.io/sig_sdgs_2025/sdg11/)

## 5. Fontes de Dados
**IPPUC (Instituto de Pesquisa e Planejamento Urbano de Curitiba):**
- Camada vetorial das linhas de ônibus, terminais e pontos de parada: https://geocuritiba.ippuc.org.br/server/rest/services/GeoCuritiba/URBS_Transporte_Publico/MapServer

- Divisão dos bairros, eixos das ruas, parques e bosques: https://ippuc.org.br/geodownloads/geo.htm

**URBS:**
- Tabela de horários: https://www.urbs.curitiba.pr.gov.br/horario-de-onibus

- Tabela da composição da frota: https://www.urbs.curitiba.pr.gov.br/transporte/rede-integrada-de-transporte/42

**IBGE (Instituto Brasileiro de Geografia e Estatística):**
- Setores censitários: https://www.ibge.gov.br/geociencias/downloads-geociencias.html?caminho=organizacao_do_territorio/malhas_territoriais/malhas_de_setores_censitarios__divisoes_intramunicipais/censo_2022/setores/gpkg/UF

- Dados do censo de 2022: https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html

**OpenStreetMap:**
- Camada de fundo: https://www.openstreetmap.org/

## 6. Processo de Exportação
Feito cada procedimento para a geração das camadas:
```
1. Criar campos com o valor de cor para cada análise da camada.;
2. Salvar as camadas como GeoJSON;
3. No index.html, modificar os nomes dos arquivos e campos especificados para se conformizar com o gerado pelo usuário;
4. Testar a visualização por meio de um servidor local (Ex.: utilizando o comando "python3 -m server.http")
```

## 7. Imagem Ilustrativa
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/95310ea6-5d27-4985-91c4-7b06866299c9" />

