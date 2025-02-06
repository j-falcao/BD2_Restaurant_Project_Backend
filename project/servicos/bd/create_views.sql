CREATE OR REPLACE VIEW estadosmesas_view AS 
SELECT * FROM estadosmesas;

CREATE OR REPLACE VIEW mesas_view AS 
SELECT * FROM mesas;

CREATE OR REPLACE VIEW mesas_disponiveis_view AS 
SELECT mesas.* FROM mesas
JOIN estadosmesas ON mesas.id_estado_mesa = estadosmesas.id_estado_mesa
WHERE designacao = 'Disponivel';

CREATE OR REPLACE VIEW mesas_ocupadas_view AS 
SELECT mesas.* FROM mesas
JOIN estadosmesas ON mesas.id_estado_mesa = estadosmesas.id_estado_mesa
WHERE designacao = 'Ocupada';

CREATE OR REPLACE VIEW mesas_reservadas_view AS 
SELECT mesas.* FROM mesas
JOIN estadosmesas ON mesas.id_estado_mesa = estadosmesas.id_estado_mesa
WHERE designacao = 'Reservada';

CREATE OR REPLACE VIEW estadosreservas_view AS 
SELECT * FROM estadosreservas;

CREATE OR REPLACE VIEW reservas_view AS 
SELECT * FROM reservas;

CREATE OR REPLACE VIEW servicos_view AS 
SELECT * FROM servicos;

CREATE OR REPLACE VIEW pedidos_view AS 
SELECT * FROM pedidos;

CREATE OR REPLACE VIEW pedidosprodutos_view AS 
SELECT * FROM pedidosprodutos;