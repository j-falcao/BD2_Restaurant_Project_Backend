CREATE OR REPLACE VIEW estadosmesas_view AS 
SELECT * FROM estadosmesas;

CREATE OR REPLACE VIEW utilizadores_view AS 
SELECT * FROM utilizadores;

CREATE OR REPLACE VIEW cargos_view AS 
SELECT * FROM cargos;

CREATE OR REPLACE VIEW utilizadorescargos_view AS
SELECT * FROM utilizadorescargos;

CREATE OR REPLACE VIEW produtos_view AS
SELECT * FROM produtos;

CREATE OR REPLACE VIEW categorias_view AS
SELECT * FROM categorias;

CREATE OR REPLACE VIEW tipos_view AS
SELECT * FROM tipos;

CREATE OR REPLACE VIEW opcoes_view AS
SELECT * FROM opcoes;

CREATE OR REPLACE VIEW itens_view AS
SELECT * FROM itens;

CREATE OR REPLACE VIEW itenscategorias_view AS
SELECT * FROM itenscategorias;

CREATE OR REPLACE VIEW itenstipos_view AS
SELECT * FROM itenstipos;

CREATE OR REPLACE VIEW itensopcoes_view AS
SELECT * FROM itensopcoes;

CREATE OR REPLACE VIEW menus_view AS
SELECT * FROM menus;

CREATE OR REPLACE VIEW itensmenus_view AS
SELECT * FROM itensmenus;

CREATE OR REPLACE VIEW fornecedores_view AS
SELECT * FROM fornecedores;

CREATE OR REPLACE VIEW ingredientes_view AS
SELECT * FROM ingredientes; 

CREATE OR REPLACE VIEW utensilios_view AS
SELECT * FROM utensilios;

CREATE OR REPLACE VIEW utensilioscarrinhos_view AS
SELECT * FROM utensilioscarrinhos;

CREATE OR REPLACE VIEW ingredientescarrinhos_view AS
SELECT * FROM ingredientescarrinhos;

CREATE OR REPLACE VIEW carrinhos_view AS
SELECT * FROM carrinhos;

CREATE OR REPLACE VIEW mesas_view AS 
SELECT * FROM mesas;

CREATE OR REPLACE VIEW reservas_view AS 
SELECT * FROM reservas;

CREATE OR REPLACE VIEW servicos_view AS 
SELECT * FROM servicos;

CREATE OR REPLACE VIEW pedidos_view AS 
SELECT * FROM pedidos;

CREATE OR REPLACE VIEW pedidosprodutos_view AS 
SELECT * FROM pedidosprodutos;

CREATE OR REPLACE VIEW pedidosprodutositensopcoes_view AS 
SELECT * FROM pedidosprodutositensopcoes;

CREATE OR REPLACE VIEW instrucoes_view AS
SELECT * FROM instrucoes;

CREATE OR REPLACE VIEW instrucoesingredientes_view AS
SELECT * FROM instrucoesingredientes;

CREATE OR REPLACE VIEW instrucoesutensilios_view AS
SELECT * FROM instrucoesutensilios;

CREATE OR REPLACE VIEW utensiliosreceitas_view AS
SELECT * FROM utensiliosreceitas;

CREATE OR REPLACE VIEW ingredientesreceitas_view AS
SELECT * FROM ingredientesreceitas;

CREATE OR REPLACE VIEW receitas_view AS
SELECT * FROM receitas;