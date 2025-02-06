CREATE OR REPLACE VIEW utilizadores_view AS 
SELECT * FROM utilizadores;

CREATE OR REPLACE VIEW garcons_view AS 
SELECT * FROM utilizadores
WHERE id_cargo = 1;

CREATE OR REPLACE VIEW cozinheiros_view AS 
SELECT * FROM utilizadores
WHERE id_cargo = 2;

CREATE OR REPLACE VIEW administradores_view AS 
SELECT * FROM utilizadores
WHERE id_cargo = 3;

CREATE OR REPLACE VIEW superusers_view AS
SELECT * FROM utilizadores
WHERE is_superuser IS TRUE;

CREATE OR REPLACE VIEW cargos_view AS 
SELECT * FROM cargos;