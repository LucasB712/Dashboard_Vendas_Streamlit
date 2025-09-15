# 📊 Dashboard de Vendas

Bem-vindo ao **Dashboard de Vendas**, um aplicativo interativo criado com **Streamlit** para visualização e análise de dados de vendas. Ele permite analisar receitas, quantidade de vendas, performance de vendedores e outras métricas, com gráficos interativos e filtros personalizados.

---

## 🚀 Funcionalidades

- **Filtros Dinâmicos**: 
  - Selecione **Região**, **Ano** e **Vendedores** para personalizar sua análise.
  
- **Gráficos Interativos**:
  - **Receita Total**: Visualize a receita por estado, categoria de produto e vendedor.
  - **Quantidade de Vendas**: Analise a quantidade de vendas mensais, por estado e categoria.
  - **Performance de Vendedores**: Compare a performance dos vendedores em termos de receita e número de vendas.
  - **Geolocalização**: Mapa interativo de vendas e receita por estado.

- **Tabelas**:
  - Exibição de dados detalhados com filtros, como vendas por estado, categoria de produto e vendedor.

---

## 🛠️ Tecnologias Utilizadas

Este projeto utiliza as seguintes ferramentas e bibliotecas:

- **Streamlit**: Framework para a criação de dashboards interativos em Python.
- **Requests**: Para fazer requisições à API externa e obter os dados de vendas.
- **Pandas**: Para manipulação e análise de dados.
- **Plotly**: Para criar gráficos interativos de alta qualidade.

---

## 💻 Como Rodar o Projeto

### 1. Clonar o Repositório

```bash
git clone https://github.com/LucasB712/dash-vendas.git
cd dash-vendas

2. Instalar as Dependências
Crie um ambiente virtual (opcional) e instale as dependências:

```



```bash
Copiar código
pip install -r requirements.txt

3. Executar o Aplicativo
Execute o Streamlit para rodar o aplicativo:


```


```bash
Copiar código
streamlit run arquivo.py
Acesse o dashboard através de http://localhost:8501.


```
## 🔍 Descrição do Código

📦 Funções Principais


formata_numero(valor, prefixo=''):

Formata valores numéricos para exibição com prefixo (por exemplo, "R$") e unidades de medida (milhares, milhões).

requests.get(url, params=query_string):
Faz uma requisição à API para buscar os dados de vendas, filtrando por região e ano.

Gráficos com Plotly:
Utiliza Plotly Express para criar gráficos interativos que são renderizados diretamente no Streamlit.

## 📊 Visualizações
O dashboard exibe várias visualizações, incluindo:

1. Receita Total
Gráficos de barra mostrando a receita por estado e por categoria de produto.

Gráfico de linha mostrando a evolução da receita mensal.

2. Quantidade de Vendas
Gráfico de barras para quantidade de vendas por estado e categoria.

Gráfico de linha mostrando o número de vendas por mês.

3. Geolocalização
Mapa de Vendas e Receita: Visualiza a distribuição de vendas e receita por estado na América do Sul.

4. Performance dos Vendedores
Gráfico de barras para mostrar os vendedores que mais geraram receita e os que mais venderam em quantidade.

## 🖼️ Exemplos de Visualizações
🔹 Top 5 Estados com Maior Receita

🔹 Quantidade de Vendas por Mês

🔹 Mapa de Vendas por Estado

🔹 Top Vendedores por Receita e Vendas

## 🛠️ Estrutura de Abas no Dashboard
O dashboard está organizado em três abas principais:

1. Receita
Exibe métricas como receita total, receita por estado e categoria, além de gráficos de receita mensal.

2. Quantidade de Vendas
Focado em analisar a quantidade de vendas por estado, categoria e ao longo do tempo.

3. Vendedores
Apresenta dados sobre os vendedores: a receita total e quantidade de vendas geradas por cada um.

## 🎨 Personalização
O código permite fácil personalização:

Alteração dos filtros disponíveis no painel lateral (região, ano, vendedores).

Adição ou remoção de métricas e gráficos conforme necessidade.

Ajuste no número de vendedores a ser exibido.

## 📝 Como Contribuir
Faça um fork deste repositório.

Crie uma branch para suas alterações (git checkout -b feature/novas-funcionalidades).

Faça commit das suas alterações (git commit -am 'Adiciona novas funcionalidades').

Envie para o repositório remoto (git push origin feature/novas-funcionalidades).

Abra um Pull Request explicando suas alterações.

## 📜 Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 💡 Aproveite o dashboard e comece a explorar os dados de vendas! 😄
