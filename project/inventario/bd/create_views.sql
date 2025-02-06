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
    utilizadores.id AS id_administrador,
    utilizadores.username AS username,
    utilizadores.url_imagem AS url_imagem_administrador
FROM carrinhos
INNER JOIN ingredientescarrinhos ON ingredientescarrinhos.id_carrinho = carrinhos.id_carrinho
INNER JOIN ingredientes ON ingredientes.id_ingrediente = ingredientescarrinhos.id_ingrediente
INNER JOIN utilizadores ON utilizadores.id = ingredientescarrinhos.id_administrador;

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
    utilizadores.id AS id_administrador,
    utilizadores.username AS username_administrador,
    utilizadores.url_imagem AS url_imagem_administrador
FROM carrinhos
INNER JOIN utensilioscarrinhos ON utensilioscarrinhos.id_carrinho = carrinhos.id_carrinho
INNER JOIN utensilios ON utensilios.id_utensilio = utensilioscarrinhos.id_utensilio
INNER JOIN utilizadores ON utilizadores.id = utensilioscarrinhos.id_administrador;

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
INNER JOIN utilizadores ON utilizadores.id = ingredientescarrinhos.id_administrador
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
INNER JOIN utilizadores ON utilizadores.id = utensilioscarrinhos.id_administrador
WHERE carrinhos.data_compra = NULL;

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