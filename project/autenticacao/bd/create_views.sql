CREATE OR REPLACE VIEW utilizadores_view AS 
SELECT * FROM utilizadores;

CREATE OR REPLACE VIEW garcons_view AS 
SELECT utilizadores.* FROM utilizadores
JOIN cargos ON utilizadores.id_cargo = cargos.id_cargo
WHERE designacao = 'Garcom';

CREATE OR REPLACE VIEW cozinheiros_view AS 
SELECT utilizadores.* FROM utilizadores
JOIN cargos ON utilizadores.id_cargo = cargos.id_cargo
WHERE designacao = 'Cozinheiro';

CREATE OR REPLACE VIEW administradores_view AS 
SELECT utilizadores.* FROM utilizadores
JOIN cargos ON utilizadores.id_cargo = cargos.id_cargo
WHERE designacao = 'Administrador';

CREATE OR REPLACE VIEW superusers_view AS
SELECT * FROM utilizadores
WHERE is_superuser IS TRUE;

CREATE OR REPLACE VIEW cargos_view AS 
SELECT * FROM cargos;