CREATE OR REPLACE VIEW estadosmesas_view AS 
SELECT * FROM estadosmesas;

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

CREATE OR REPLACE VIEW tiposcarrinhos_view AS
SELECT * FROM tipos_carrinhos;

CREATE OR REPLACE VIEW carrinhos_view AS
SELECT * FROM carrinhos;

CREATE OR REPLACE VIEW ingredientescarrinhos_view AS
SELECT
    ingredientescarrinhos.id_ingrediente_carrinho,
    ingredientescarrinhos.id_carrinho,
    ingredientescarrinhos.quantidade,
    ingredientescarrinhos.created_at,
    ingredientescarrinhos.updated_at,
    ingredientes.id_ingrediente,
    ingredientes.nome AS nome_ingrediente,
    ingredientes.url_imagem AS url_imagem_ingrediente,
    utilizadores.id_utilizador AS id_administrador,
    utilizadores.username AS username,
    utilizadores.url_imagem AS url_imagem_administrador
FROM carrinhos
INNER JOIN ingredientescarrinhos ON ingredientescarrinhos.id_carrinho = carrinhos.id_carrinho
INNER JOIN ingredientes ON ingredientes.id_ingrediente = ingredientescarrinhos.id_ingrediente
INNER JOIN utilizadores ON utilizadores.id_utilizador = ingredientescarrinhos.id_administrador;

CREATE OR REPLACE VIEW utensilioscarrinhos_view AS
SELECT 
    utensilioscarrinhos.id_utensilio_carrinho,
    utensilioscarrinhos.id_carrinho,
    utensilioscarrinhos.quantidade,
    utensilioscarrinhos.created_at,
    utensilioscarrinhos.updated_at,
    utensilios.id_utensilio,
    utensilios.nome AS nome_utensilio,
    utensilios.url_imagem AS url_imagem_utensilio,
    utilizadores.id_utilizador AS id_administrador,
    utilizadores.username AS username_administrador,
    utilizadores.url_imagem AS url_imagem_administrador
FROM carrinhos
INNER JOIN utensilioscarrinhos ON utensilioscarrinhos.id_carrinho = carrinhos.id_carrinho
INNER JOIN utensilios ON utensilios.id_utensilio = utensilioscarrinhos.id_utensilio
INNER JOIN utilizadores ON utilizadores.id_utilizador = utensilioscarrinhos.id_administrador;

CREATE OR REPLACE VIEW carrinho_atual_view AS
SELECT * FROM carrinhos
WHERE data_compra IS NULL; 

CREATE OR REPLACE VIEW ingredientescarrinho_atual_view AS
SELECT 
    ingredientescarrinhos.*,
    ingredientes.nome AS nome_ingrediente,
    ingredientes.url_imagem AS url_imagem_ingrediente,
    utilizadores.username AS username_administrador,
    utilizadores.url_imagem AS url_imagem_administrador
FROM carrinhos
INNER JOIN ingredientescarrinhos ON ingredientescarrinhos.id_carrinho = carrinhos.id_carrinho
INNER JOIN ingredientes ON ingredientes.id_ingrediente = ingredientescarrinhos.id_ingrediente
INNER JOIN utilizadores ON utilizadores.id_utilizador = ingredientescarrinhos.id_administrador
WHERE carrinhos.data_compra = NULL;

CREATE OR REPLACE VIEW utensilioscarrinho_atual_view AS
SELECT 
    utensilioscarrinhos.*,
    utensilios.nome AS nome_utensilio,
    utensilios.url_imagem AS url_imagem_utensilio,
    utilizadores.username AS username_administrador,
    utilizadores.url_imagem AS url_imagem_administrador
FROM carrinhos
INNER JOIN utensilioscarrinhos ON utensilioscarrinhos.id_carrinho = carrinhos.id_carrinho
INNER JOIN utensilios ON utensilios.id_utensilio = utensilioscarrinhos.id_utensilio
INNER JOIN utilizadores ON utilizadores.id_utilizador = utensilioscarrinhos.id_administrador
WHERE carrinhos.data_compra = NULL;

CREATE OR REPLACE VIEW mesas_view AS 
SELECT * FROM mesas;

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

-- CREATE OR REPLACE VIEW pedidosprodutositensopcoes_view AS 
-- SELECT * FROM pedidosprodutositensopcoes;

CREATE OR REPLACE VIEW instrucoes_view AS
SELECT * FROM instrucoes;

CREATE OR REPLACE VIEW receitas_view AS
SELECT * FROM receitas;

CREATE OR REPLACE VIEW ingredientesreceitas_view AS
SELECT
    ir.*,
    i.nome AS nome_ingrediente,
    i.url_imagem AS url_imagem_ingrediente
FROM ingredientesreceitas ir
JOIN ingredientes i ON i.id_ingrediente = ir.id_ingrediente;

CREATE OR REPLACE VIEW utensiliosreceitas_view AS
SELECT 
    ur.*,
    u.nome AS nome_utensilio,
    u.url_imagem AS url_imagem_utensilio
FROM utensiliosreceitas ur
JOIN utensilios u ON u.id_utensilio = ur.id_utensilio;