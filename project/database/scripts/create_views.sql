CREATE OR REPLACE VIEW estadosmesas_view AS 
SELECT * FROM estadosmesas;

CREATE OR REPLACE VIEW utilizadores_view AS 
SELECT u.*, c.designacao AS designacao_cargo FROM utilizadores u
JOIN utilizadorescargos uc ON uc.id_utilizador = u.id_utilizador
JOIN cargos c ON c.id_cargo = uc.id_cargo;

CREATE OR REPLACE VIEW cargos_view AS 
SELECT c.*, CONCAT(u.first_name, ' ', u.last_name) AS nome_utilizador, u.username, u.url_imagem FROM cargos c
JOIN utilizadorescargos uc ON uc.id_utilizador = c.id_cargo
JOIN utilizadores u ON u.id_utilizador = uc.id_utilizador;

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
SELECT i.*, p.nome AS nome_produto, p.preco AS preco_produto FROM itens i
JOIN produtos_view p ON p.id_produto = i.id_item;

CREATE OR REPLACE VIEW itenscategorias_view AS
SELECT ic.*, c.designacao AS designacao_categoria, c.designacao AS nome_item FROM itenscategorias ic
JOIN itens_view i ON i.id_item = ic.id_item
JOIN categorias_view c ON c.id_categoria = ic.id_categoria;

CREATE OR REPLACE VIEW itenstipos_view AS
SELECT it.*, i.nome_produto AS nome_item, t.designacao AS designacao_tipo FROM itenstipos it
JOIN itens_view i ON i.id_item = it.id_item
JOIN tipos_view t ON t.id_tipo = it.id_tipo;

CREATE OR REPLACE VIEW itensopcoes_view AS
SELECT io.*, i.nome_produto AS nome_item, o.designacao AS designacao_opcao FROM itensopcoes io
JOIN itens_view i ON i.id_item = io.id_item
JOIN opcoes_view o ON o.id_opcao = io.id_opcao;

CREATE OR REPLACE VIEW menus_view AS
SELECT m.*, p.nome AS designacao_menu FROM menus m
JOIN produtos_view p ON p.id_produto = m.id_menu;

CREATE OR REPLACE VIEW itensmenus_view AS
SELECT im.*, i.nome_produto AS nome_item, m.designacao_menu FROM itensmenus im
JOIN itens_view i ON i.id_item = im.id_item
JOIN menus_view m ON m.id_menu = im.id_menu;

CREATE OR REPLACE VIEW fornecedores_view AS
SELECT * FROM fornecedores;

CREATE OR REPLACE VIEW ingredientes_view AS
SELECT i.*, f.nome AS nome_fornecedor FROM ingredientes i
JOIN fornecedores_view f ON f.id_fornecedor = i.id_fornecedor;

CREATE OR REPLACE VIEW utensilios_view AS
SELECT u.*, f.nome AS nome_fornecedor FROM utensilios u
JOIN fornecedores_view f ON f.id_fornecedor = u.id_fornecedor;

CREATE OR REPLACE VIEW utensilioscarrinhos_view AS
SELECT uc.*, u.nome AS designacao_utensilio FROM utensilioscarrinhos uc
JOIN utensilios_view u ON u.id_utensilio = uc.id_utensilio;

CREATE OR REPLACE VIEW ingredientescarrinhos_view AS
SELECT ic.*, i.nome AS nome_ingrediente FROM ingredientescarrinhos ic
JOIN ingredientes_view i ON i.id_ingrediente = ic.id_ingrediente;

CREATE OR REPLACE VIEW carrinhos_view AS
SELECT c.*, i.nome AS nome_ingrediente, u.nome AS nome_utensilio FROM carrinhos c
JOIN ingredientescarrinhos_view ic ON ic.id_carrinho = c.id_carrinho
JOIN ingredientes_view i ON i.id_ingrediente = ic.id_ingrediente
JOIN utensilioscarrinhos_view uc ON uc.id_carrinho = c.id_carrinho
JOIN utensilios_view u ON u.id_utensilio = uc.id_utensilio;

CREATE OR REPLACE VIEW mesas_view AS 
SELECT m.*, em.designacao AS designacao_estado FROM mesas m
JOIN estadosmesas_view em ON em.id_estado_mesa = m.id_estado_mesa;

CREATE OR REPLACE VIEW reservas_view AS 
SELECT r.*, m.numero FROM reservas r
JOIN mesas_view m ON m.id_mesa = r.id_mesa;

CREATE OR REPLACE VIEW servicos_view AS 
SELECT s.*, m.numero FROM servicos s
JOIN mesas_view m ON m.id_mesa = s.id_mesa;

CREATE OR REPLACE VIEW pedidos_view AS 
SELECT p.* FROM pedidos p
JOIN servicos_view s ON s.id_servico = p.id_servico;

CREATE OR REPLACE VIEW pedidosprodutos_view AS 
SELECT pp.*, p.id_servico FROM pedidosprodutos pp
JOIN pedidos_view p ON p.id_pedido = pp.id_pedido;

CREATE OR REPLACE VIEW pedidosprodutositensopcoes_view AS 
SELECT ppio.*, pp.id_produto FROM pedidosprodutositensopcoes ppio
JOIN pedidosprodutos_view pp ON pp.id_pedido_produto = ppio.id_pedido_produto;

CREATE OR REPLACE VIEW instrucoes_view AS
SELECT i.*, i.nome AS nome_ingrediente, u.nome AS nome_utensilio FROM instrucoes ins
JOIN instrucoesingredientes ii ON ii.id_instrucao = ins.id_instrucao
JOIN ingredientes i ON i.id_ingrediente = ii.id_ingrediente
JOIN instrucoesutensilios iu ON iu.id_instrucao = ins.id_instrucao
JOIN utensilios u ON u.id_utensilio = iu.id_utensilio;

CREATE OR REPLACE VIEW instrucoesingredientes_view AS
SELECT * FROM instrucoesingredientes;

CREATE OR REPLACE VIEW instrucoesutensilios_view AS
SELECT * FROM instrucoesutensilios;

CREATE OR REPLACE VIEW utensiliosreceitas_view AS
SELECT * FROM utensiliosreceitas;

CREATE OR REPLACE VIEW ingredientesreceitas_view AS
SELECT * FROM ingredientesreceitas;

CREATE OR REPLACE VIEW receitas_view AS
SELECT r.*, i.nome AS designacao_ingrediente, u.nome AS designacao_utensilio FROM receitas r
JOIN utensiliosreceitas ur ON ur.id_receita = r.id_receita
JOIN utensilios u ON u.id_utensilio = ur.id_utensilio
JOIN ingredientesreceitas ir ON ir.id_receita = r.id_receita
JOIN ingredientes i ON i.id_ingrediente = ir.id_ingrediente
JOIN instrucoes ins ON ins.id_receita = r.id_receita;