# Crypto ETL Pipeline - Docker & Python

Este projeto consiste em um pipeline de dados automatizado que extrai dados em tempo real da API CoinGecko, processa-os utilizando Python (Pandas) e armazena as informações em um banco de dados PostgreSQL, tudo orquestrado via Docker.

O objetivo foi entender na prática o uso do Docker e Docker Compose para orquestrar um ambiente de Engenharia de Dados, resolvendo desafios reais de:

- Comunicação entre serviços (Network).
- Persistência de dados (Volumes).
- Variáveis de ambiente e isolamento de processos.

## Arquitetura do Projeto

- Linguagem: Python 3.11+
- Bibliotecas: Pandas, SQLAlchemy, Requests.
- Banco de Dados: PostgreSQL 17.
- Infraestrutura: Docker e Docker Compose.

### Resultado do SQL 
<p align="center">
<img width="1097" height="193" alt="image" src="https://github.com/user-attachments/assets/4e6fa5da-d5d3-4104-8eb7-13fe189a860a"  title="Resultado do SQl"/>
</p>

## Como executar


#### 1. Clone o repositório
git clone [https://github.com/nicolasvzr/Crypto_ELTProjeto.git](https://github.com/nicolasvzr/Crypto_ELTProjeto.git)

#### 2. Entre na pasta
cd Crypto_ELTProjeto

#### 3. Suba o ambiente
docker-compose up --build

## Estrutura do Banco de Dados 

**Tabela precos_cripto**: Armazena ID, Símbolo, Nome, Preço (USD), Market Cap e a data da carga.

**View visao_dominancia**: Um cálculo SQL que mostra o percentual de market cap de cada moeda em relação ao total capturado.

## O que eu aprendi 
 - Containerização: Isolamento de ambientes para garantir que o projeto rode em qualquer máquina.

- Tratamento de Erros: Implementação de retentativas e logs para falhas de conexão com o banco.

- Data Lineage: Uso de data_carga para permitir análises históricas temporais.


