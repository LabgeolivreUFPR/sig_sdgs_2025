# Edificações e ocupações irregulares em APP’s de Curitiba: análise espacial aplicada aos ODS

**Autores:** Elian Eckel Treinty • Luiggi Martins Bettone  
**Disciplina:** Sistemas de Informação Geográfica — UFPR

Este repositório contém um **mapa web (QGIS2Web + Leaflet)** e a documentação do trabalho sobre **edificações/ocupações irregulares em Áreas de Preservação Permanente (APP)** no município de Curitiba.

---

## 1. Objetivo do Mapa

Responder, de forma espacial e visual, à pergunta: **“Onde e quanto a cidade está edificada dentro de APP?”**, discutindo impactos e priorização de áreas para gestão urbana/ambiental.

---

## 2. ODS relacionados

Este trabalho se relaciona principalmente com:  
- **ODS 6** — proteção de recursos hídricos (bacias/APP)  
- **ODS 11** — planejamento urbano, habitação e redução de risco  
- **ODS 13** — adaptação a eventos extremos  
- **ODS 15** — conservação de ecossistemas terrestres e ripários

---

## 3. Descrição do Mapa

### 3.1 Área de estudo
- **Município de Curitiba**.

### 3.2 Bases e unidades de análise
**Bases utilizadas:**
- Edificações (**IPPUC**, polígonos)  
- APP’s (**FBDS**, polígonos)  
- **Censo 2022** (variáveis de moradores — por bairro)  
- Camada de ocupações irregulares (**IPPUC**)

**Unidades de análise:**
- Bairros (IBGE)  
- Regionais (IPPUC)  
- Bacias hidrográficas (IPPUC)

### 3.3 Principais análises implementadas
- **Interseção (Intersect)**: *Edificações × APP* → polígonos de edificações que caem em APP.  
- **Kernel Density (heatmap)**: centroides das edificações em APP + densidade de Kernel para destacar hotspots.  
- **Join espacial + agregação** por:
  - **Bairros** (coroplético)  
  - **Regionais** (coroplético)  
  - **Bacias hidrográficas** (coroplético)  
- **Ocupação irregular (IPPUC) dentro de APP** com **símbolos proporcionais**, evidenciando conflito socioambiental.

### 3.4 Indicadores e resultados (resumo)
- Total de **edificações** no município (base): **1.499.300 unidades**.  
- **Edificações em APP** (interseção): **116.208 polígonos**.  
- **Área total edificada em APP**: **5.136.122 m²**.  
- Destaque do Censo 2022: **bairros da região norte** com maior população afetada.

### 3.5 Camadas do mapa web (Leaflet)
O `index.html` do mapa web foi exportado via QGIS2Web e inclui:
- **Mapas base:** OpenStreetMap (padrão) e Google Satélite (opcional).  
- **Camadas temáticas (overlays):**
  - Mapa de calor (heatmap recortado)  
  - Pessoas em edificações irregulares (coroplético por bairro)  
  - Densidade por bairro / por região / por bacia (coropléticos)  
  - Hidrografia, APP, Hidrobacias, Divisa de bairros  
- **Legenda dinâmica**: muda conforme a camada ativa. (Ligar duas camadas e desligar a que você não quer que apareça caso apresente erro)

---

## 4. Acesse o mapa publicado

🔗 **Mapa Web (GitHub Pages):**  
`https://SEU_USUARIO.github.io/SEU_REPOSITORIO/SUA_PASTA/`

> Substitua o link acima conforme o caminho real do seu repositório/pasta.

---

## 5. Fontes de Dados

- **IPPUC** — edificações, ocupações irregulares, regionais, hidrografia/bacias (camadas vetoriais)  
- **FBDS** — polígonos de APP  
- **IBGE** — bairros (malha)  
- **Censo 2022** — variáveis de moradores por bairro  
- Basemap: **OpenStreetMap** / **Google Satélite** (consumo via tiles no Leaflet).

---

## 6. Processo de Exportação (resumo)

Fluxo utilizado:

```
1. Preparar as camadas no QGIS (projeção, recortes, atributos)
2. Configurar simbologia, classes e rótulos
3. Rodar análises: Intersect, centroides, Kernel Density, join espacial e dissolves
4. Abrir o plugin QGIS2Web
5. Exportar em Leaflet
6. Copiar para o diretório do repositório (index.html + pastas data/, css/, js/)
7. Publicar via GitHub Pages
```
---

## 8. Observações finais

- O mapa inicia com algumas camadas ligadas (heatmap + divisas + hidrobacias) e a legenda é ajustada automaticamente.  
- No `index.html`, os **pop-ups foram desabilitados** (navegação focada em leitura temática).  
- Recomendações gerais (nomes sem acentos/espaços, garantir funcionamento no GitHub Pages etc.).

---

## 9. Limitações e próximos passos

**Limitações:**
- Diferenças de escala/ano entre as bases (IPPUC/FBDS/Censo)  
- Edificações ≠ população (ex.: galpões, usos diversos)  
- APP mapeada por base externa pode divergir do enquadramento local

**Próximos passos:**
- Cruzar com declividade, rede de drenagem e histórico de cheias  
- Validar hotspots com imagens/situação de campo  
- Criar indicador por bairro: “pressão urbanística em APP”

