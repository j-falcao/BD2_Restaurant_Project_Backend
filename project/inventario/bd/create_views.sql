CREATE OR REPLACE VIEW fornecedores_view AS
SELECT * FROM fornecedores;

CREATE OR REPLACE PROCEDURE get_ingredientes_by_fornecedor(_id_fornecedor_in INT, OUT resultado JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(ingredientes)) INTO resultado
    FROM (
        SELECT i.*
        FROM ingredientes i
        WHERE i.id_fornecedor = _id_fornecedor_in
    ) ingredientes;
END;
$$;

CREATE OR REPLACE PROCEDURE get_utensilios_by_fornecedor(_id_fornecedor_in INT, OUT resultado JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(utensilios)) INTO resultado
    FROM (
        SELECT u.*
        FROM utensilios u
        WHERE u.id_fornecedor = _id_fornecedor_in
    ) utensilios;
END;
$$;

CREATE OR REPLACE VIEW ingredientes_view AS
SELECT * FROM ingredientes; 

CREATE OR REPLACE VIEW utensilios_view AS
SELECT * FROM utensilios;

CREATE OR REPLACE VIEW tiposcarrinhos_view AS
SELECT * FROM tiposcarrinhos;

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
JOIN ingredientescarrinhos ON ingredientescarrinhos.id_carrinho = carrinhos.id_carrinho
JOIN ingredientes ON ingredientes.id_ingrediente = ingredientescarrinhos.id_ingrediente
JOIN utilizadores ON utilizadores.id = ingredientescarrinhos.id_administrador
JOIN tiposcarrinhos ON tiposcarrinhos.id_tipo_carrinho = carrinhos.id_carrinho
WHERE tiposcarrinhos.designacao = 'Ingredientes';

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
JOIN utensilioscarrinhos ON utensilioscarrinhos.id_carrinho = carrinhos.id_carrinho
JOIN utensilios ON utensilios.id_utensilio = utensilioscarrinhos.id_utensilio
JOIN utilizadores ON utilizadores.id = utensilioscarrinhos.id_administrador
JOIN tiposcarrinhos ON tiposcarrinhos.id_tipo_carrinho = carrinhos.id_carrinho
WHERE tiposcarrinhos.designacao = 'Utensilios';

CREATE OR REPLACE VIEW carrinho_atual_ingredientes_view AS
SELECT carrinhos.* FROM carrinhos
JOIN tiposcarrinhos ON tiposcarrinhos.id_tipo_carrinho = carrinhos.id_carrinho
WHERE data_compra IS NULL
AND tiposcarrinhos.designacao = 'Ingredientes';

CREATE OR REPLACE VIEW carrinho_atual_utensilios_view AS
SELECT carrinhos.* FROM carrinhos
JOIN tiposcarrinhos ON tiposcarrinhos.id_tipo_carrinho = carrinhos.id_carrinho
WHERE data_compra IS NULL
AND tiposcarrinhos.designacao = 'Utensilios';

CREATE OR REPLACE VIEW ingredientescarrinho_atual_view AS
SELECT 
    ingredientescarrinhos.*,
    ingredientes.nome AS nome_ingrediente,
    ingredientes.url_imagem AS url_imagem_ingrediente,
    utilizadores.username AS username_administrador,
    utilizadores.url_imagem AS url_imagem_administrador
FROM carrinhos
JOIN ingredientescarrinhos ON ingredientescarrinhos.id_carrinho = carrinhos.id_carrinho
JOIN ingredientes ON ingredientes.id_ingrediente = ingredientescarrinhos.id_ingrediente
JOIN utilizadores ON utilizadores.id = ingredientescarrinhos.id_administrador
JOIN tiposcarrinhos ON tiposcarrinhos.id_tipo_carrinho = carrinhos.id_carrinho
WHERE carrinhos.data_compra IS NULL
AND tiposcarrinhos.designacao = 'Ingredientes';

CREATE OR REPLACE VIEW utensilioscarrinho_atual_view AS
SELECT 
    utensilioscarrinhos.*,
    utensilios.nome AS nome_utensilio,
    utensilios.url_imagem AS url_imagem_utensilio,
    utilizadores.username AS username_administrador,
    utilizadores.url_imagem AS url_imagem_administrador
FROM carrinhos
JOIN utensilioscarrinhos ON utensilioscarrinhos.id_carrinho = carrinhos.id_carrinho
JOIN utensilios ON utensilios.id_utensilio = utensilioscarrinhos.id_utensilio
JOIN utilizadores ON utilizadores.id = utensilioscarrinhos.id_administrador
JOIN tiposcarrinhos ON tiposcarrinhos.id_tipo_carrinho = carrinhos.id_carrinho
WHERE carrinhos.data_compra IS NULL
AND tiposcarrinhos.designacao = 'Utensilios';

CREATE OR REPLACE VIEW instrucoes_view AS
SELECT * FROM instrucoes;

CREATE OR REPLACE VIEW receitas_view AS
SELECT * FROM receitas;

CREATE OR REPLACE PROCEDURE get_receitas_by_ingrediente(_id_ingrediente_in INT, OUT resultado JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(receitas)) INTO resultado
    FROM (
        SELECT r.*
        FROM receitas r
        JOIN ingredientesreceitas ir ON r.id_receita = ir.id_receita
        WHERE ir.id_ingrediente = _id_ingrediente_in
    ) receitas;
END;
$$;

CREATE OR REPLACE PROCEDURE get_receitas_by_utensilio(_id_utensilio_in INT, OUT resultado JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(receitas)) INTO resultado
    FROM (
        SELECT r.*
        FROM receitas r
        JOIN utensiliosreceitas ur ON r.id_receita = ur.id_receita
        WHERE ur.id_utensilio = _id_utensilio_in
    ) receitas;
END;
$$;

CREATE OR REPLACE PROCEDURE get_ingredientes_by_receita(_id_receita_in INT, OUT resultado JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(ingredientes)) INTO resultado
    FROM (
        SELECT
            ir.*,
            i.nome AS nome_ingrediente,
            i.url_imagem AS url_imagem_ingrediente
        FROM ingredientesreceitas ir
        JOIN ingredientes i ON i.id_ingrediente = ir.id_ingrediente
    ) ingredientes;
END;
$$;

CREATE OR REPLACE PROCEDURE get_utensilios_by_receita(_id_receita_in INT, OUT resultado JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(utensilios)) INTO resultado
    FROM (
        SELECT
            ur.*,
            u.nome AS nome_utensilio,
            u.url_imagem AS url_imagem_utensilio
        FROM utensiliosreceitas ur
        JOIN utensilios u ON u.id_utensilio = ur.id_utensilio
    ) utensilios;
END;
$$;
