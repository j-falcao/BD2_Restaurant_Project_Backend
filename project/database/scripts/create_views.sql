CREATE OR REPLACE VIEW estadosmesas_view AS 
SELECT * FROM estadosmesas;

CREATE OR REPLACE VIEW permissoescargos_view AS
SELECT * FROM permissoescargos
JOIN permissoes ON permissoes.id_permissao = permissoescargos.id_permissao
JOIN cargos ON cargos.id_cargo = permissoescargos.id_cargo;

CREATE OR REPLACE VIEW utilizadores_view AS 
SELECT * FROM utilizadores
JOIN permissoes ON permissoes.id_permissao = utilizadores.id_permissao
JOIN cargos ON cargos.id_cargo = utilizadores.id_cargo;

CREATE OR REPLACE VIEW produtos_view AS
SELECT * FROM produtos;

CREATE OR REPLACE VIEW categorias_view AS
SELECT * FROM categorias;

CREATE OR REPLACE VIEW tipos_view AS
SELECT * FROM tipos;

CREATE OR REPLACE VIEW opcoes_view AS
SELECT * FROM opcoes;

CREATE OR REPLACE VIEW itens_view AS
SELECT * FROM itens
JOIN produtos_view ON produtos_view.id_produto = itens.id_item;

CREATE OR REPLACE VIEW itenscategorias_view AS
SELECT * FROM itenscategorias
JOIN itens_view ON itens_view.id_item = itenscategorias.id_item
JOIN categorias_view ON categorias_view.id_categoria = itenscategorias.id_categoria;

CREATE OR REPLACE VIEW itenstipos_view AS
SELECT * FROM itenstipos
JOIN itens_view ON itens_view.id_item = itenstipos.id_item
JOIN tipos_view ON tipos_view.id_tipo = itenstipos.id_tipo;

CREATE OR REPLACE VIEW itensopcoes_view AS
SELECT * FROM itensopcoes
JOIN itens_view ON itens_view.id_item = itensopcoes.id_item
JOIN opcoes_view ON opcoes_view.id_opcao = itensopcoes.id_opcao;

CREATE OR REPLACE VIEW menus_view AS
SELECT * FROM menus
JOIN produtos_view ON produtos_view.id_produto = menus.id_menu;

CREATE OR REPLACE VIEW itensmenus_view AS
SELECT * FROM itensmenus
JOIN itens_view ON itens_view.id_item = itensmenus.id_item
JOIN menus_view ON menus_view.id_menu = itensmenus.id_menu;

CREATE OR REPLACE VIEW fornecedores_view AS
SELECT * FROM fornecedores;

CREATE OR REPLACE VIEW ingredientes_view AS
SELECT * FROM ingredientes
JOIN fornecedores_view ON fornecedores_view.id_fornecedor = ingredientes.id_fornecedor;

CREATE OR REPLACE VIEW utensilios_view AS
SELECT * FROM utensilios
JOIN fornecedores_view ON fornecedores_view.id_fornecedor = utensilios.id_fornecedor;

CREATE OR REPLACE VIEW utensilioscarrinhos_view AS
SELECT * FROM utensilioscarrinhos
JOIN utensilios_view ON utensilios_view.id_utensilio = utensilioscarrinhos.id_utensilio;

CREATE OR REPLACE VIEW ingredientescarrinhos_view AS
SELECT * FROM ingredientescarrinhos
JOIN ingredientes_view ON ingredientes_view.id_ingrediente = ingredientescarrinhos.id_ingrediente;

CREATE OR REPLACE VIEW carrinhos_view AS
SELECT * FROM carrinhos
JOIN ingredientescarrinhos_view ON ingredientescarrinhos_view.id_carrinho = carrinhos.id_carrinho
JOIN utensilioscarrinhos_view ON utensilioscarrinhos_view.id_carrinho = carrinhos.id_carrinho;

CREATE OR REPLACE VIEW mesas_view AS 
SELECT * FROM mesas
JOIN estadosmesas_view ON estadosmesas_view.id_estado_mesa = mesas.id_estado_mesa;

CREATE OR REPLACE VIEW reservas_view AS 
SELECT * FROM reservas
JOIN mesas_view ON mesas_view.id_mesa = reservas.id_mesa;

CREATE OR REPLACE VIEW servicos_view AS 
SELECT * FROM servicos
JOIN mesas_view ON mesas_view.id_mesa = servicos.id_mesa;

CREATE OR REPLACE VIEW pedidos_view AS 
SELECT * FROM pedidos
JOIN servicos_view ON servicos_view.id_servico = pedidos.id_servico;

CREATE OR REPLACE VIEW pedidosprodutos_view AS 
SELECT * FROM pedidosprodutos
JOIN pedidos_view ON pedidos_view.id_pedido = pedidosprodutos.id_pedido;

CREATE OR REPLACE VIEW pedidosprodutositensopcoes_view AS 
SELECT * FROM pedidosprodutositensopcoes
JOIN pedidosprodutos_view ON pedidosprodutos_view.id_pedido_produto = pedidosprodutositensopcoes.id_pedido_produto;

CREATE OR REPLACE VIEW instrucoes_view AS
SELECT * FROM instrucoes;

CREATE OR REPLACE VIEW utensiliosreceitas_view AS
SELECT * FROM utensiliosreceitas
JOIN utensilios_view ON utensilios_view.id_utensilio = utensiliosreceitas.id_utensilio;

CREATE OR REPLACE VIEW ingredientesreceitas_view AS
SELECT * FROM ingredientesreceitas
JOIN ingredientes_view ON ingredientes_view.id_ingrediente = ingredientesreceitas.id_ingrediente;

CREATE OR REPLACE VIEW receitas_view AS
SELECT * FROM receitas
JOIN utensiliosreceitas_view ON utensiliosreceitas_view.id_receita = receitas.id_receita
JOIN ingredientesreceitas_view ON ingredientesreceitas_view.id_receita = receitas.id_receita
JOIN instrucoes_view ON instrucoes_view.id_receita = receitas.id_receita;
