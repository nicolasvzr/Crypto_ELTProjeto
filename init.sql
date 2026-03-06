-- Essa visão calcula a dominância do Bitcoin no seu banco
CREATE VIEW visao_dominancia AS
SELECT 
    name, 
    market_cap,
    (market_cap / SUM(market_cap) OVER()) * 100 as percentual_dominancia
FROM precos_cripto;

