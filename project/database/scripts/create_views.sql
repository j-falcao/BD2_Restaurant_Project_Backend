CREATE OR REPLACE VIEW estadosmesas_view AS 
SELECT * FROM estadomesa;

CREATE OR REPLACE VIEW utilizadores_view AS 
SELECT * FROM utilizadores;

CREATE OR REPLACE VIEW produto_view AS
SELECT * FROM produto;

CREATE OR REPLACE VIEW categoria_view AS
SELECT * FROM categoria;

CREATE OR REPLACE VIEW tipo_view AS
SELECT * FROM tipo;

CREATE OR REPLACE VIEW opcao_view AS
SELECT * FROM opcao;

CREATE OR REPLACE VIEW item_view AS
SELECT * FROM item
JOIN produto_view p_v ON p_v.id_produto = item.id_item;

CREATE OR REPLACE VIEW itemcategoria_view AS
SELECT * FROM itemcategoria
JOIN item_view i_v ON i_v.id_item = itemcategoria.id_item
JOIN categoria_view c_v ON c_v.id_categoria = itemcategoria.id_categoria;

CREATE OR REPLACE VIEW itemtipo_view AS
SELECT * FROM itemtipo
JOIN item_view i_v ON i_v.id_item = itemtipo.id_item
JOIN tipo_view t_v ON t_v.id_tipo = itemtipo.id_tipo;

CREATE OR REPLACE VIEW itemopcao_view AS
SELECT * FROM itemopcao
JOIN item_view i_v ON i_v.id_item = itemopcao.id_item
JOIN opcao_view o_v ON o_v.id_opcao = itemopcao.id_opcao;

CREATE OR REPLACE VIEW menu_view AS
SELECT * FROM menu
JOIN produto_view p_v ON p_v.id_produto = menu.id_menu;

CREATE OR REPLACE VIEW itemmenu_view AS
SELECT * FROM itemmenu
JOIN item_view i_v ON i_v.id_item = itemmenu.id_item
JOIN menu_view m_v ON m_v.id_menu = itemmenu.id_menu;

CREATE OR REPLACE VIEW fornecedores_view AS
SELECT * FROM fornecedores;

CREATE OR REPLACE VIEW ingredientes_view AS
SELECT * FROM ingredientes
JOIN fornecedores_view f_v ON f_v.id_fornecedor = ingredientes.id_fornecedor;

CREATE OR REPLACE VIEW utensilios_view AS
SELECT * FROM utensilios
JOIN fornecedores_view f_v ON f_v.id_fornecedor = utensilios.id_fornecedor;

CREATE OR REPLACE VIEW utensilioscarrinhos_view AS
SELECT * FROM utensilioscarrinhos
JOIN utensilios_view u_v ON u_v.id_utensilio = utensilioscarrinhos.id_utensilio;

CREATE OR REPLACE VIEW ingredientescarrinhos_view AS
SELECT * FROM ingredientescarrinhos
JOIN ingredientes_view i_v ON i_v.id_ingrediente = ingredientescarrinhos.id_ingrediente;

CREATE OR REPLACE VIEW carrinhos_view AS
SELECT * FROM carrinhos
JOIN ingredientescarrinhos_view ic_v ON ic_v.id_carrinho = carrinhos.id_carrinho
JOIN utensilioscarrinhos_view uc_v ON uc_v.id_carrinho = carrinhos.id_carrinho;

CREATE OR REPLACE VIEW mesas_view AS 
SELECT * FROM mesa
JOIN estadosmesas_view em_v ON em_v.id_estado_mesa = mesa.id_estado_mesa;

CREATE OR REPLACE VIEW reservas_view AS 
SELECT * FROM reserva
JOIN mesas_view m_v ON m_v.id_mesa = reserva.id_mesa;

CREATE OR REPLACE VIEW servicos_view AS 
SELECT * FROM servico
JOIN mesas_view m_v ON m_v.id_mesa = servico.id_mesa;

CREATE OR REPLACE VIEW pedidos_view AS 
SELECT * FROM pedido
JOIN servicos_view s_v ON s_v.id_servico = pedido.id_servico;

CREATE OR REPLACE VIEW pedidosprodutos_view AS 
SELECT * FROM pedidoproduto
JOIN pedidos_view p_v ON p_v.id_pedido = pedidoproduto.id_pedido;

CREATE OR REPLACE VIEW pedidosprodutositensopcoes_view AS 
SELECT * FROM pedidoprodutoitemopcao
JOIN pedidosprodutos_view pp_v ON pp_v.id_pedido_produto = pedidoprodutoitemopcao.id_pedido_produto;

CREATE OR REPLACE VIEW instrucoes_view AS
SELECT * FROM instrucoes;

CREATE OR REPLACE VIEW utensiliosreceitas_view AS
SELECT * FROM utensiliosreceitas
JOIN utensilios_view u_v ON u_v.id_utensilio = utensiliosreceitas.id_utensilio;

CREATE OR REPLACE VIEW ingredientesreceitas_view AS
SELECT * FROM ingredientesreceitas
JOIN ingredientes_view i_v ON i_v.id_ingrediente = ingredientesreceitas.id_ingrediente;

CREATE OR REPLACE VIEW receitas_view AS
SELECT * FROM receitas
JOIN utensiliosreceitas_view ur_v ON ur_v.id_receita = receitas.id_receita
JOIN ingredientesreceitas_view ir_v ON ir_v.id_receita = receitas.id_receita
JOIN instrucoes_view ins_v ON ins_v.id_receita = receitas.id_receita;
