CREATE OR REPLACE PROCEDURE create_cargos(_new_designacao VARCHAR(100), OUT _new_cargo JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO cargos (designacao)
    VALUES (_new_designacao)
    RETURNING row_to_json(cargos) INTO _new_cargo;
END;
$$;

CREATE OR REPLACE PROCEDURE update_cargos(id_cargo_in INT, _new_designacao VARCHAR(100), OUT _new_cargo JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE cargos
    SET designacao = _new_designacao
    WHERE id_cargo = id_cargo_in
    RETURNING row_to_json(cargos) INTO _new_cargo;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_cargos(id_cargo_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM cargos
    WHERE id_cargo = id_cargo_in;
END;
$$;


CREATE OR REPLACE PROCEDURE create_utilizadores(_new_username VARCHAR(50), _new_id_cargo INT, _new_first_name VARCHAR(100), _new_last_name VARCHAR(100), _new_is_superuser BOOLEAN, _new_url_imagem VARCHAR(2048), _new_password VARCHAR(255), OUT _new_utilizador JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO utilizadores (username, id_cargo, first_name, last_name, is_superuser, url_imagem, password)
    VALUES (_new_username, _new_id_cargo, _new_first_name, _new_last_name, _new_is_superuser, _new_url_imagem, _new_password)
    RETURNING row_to_json(utilizadores) INTO _new_utilizador;
END;
$$;


CREATE OR REPLACE PROCEDURE update_utilizadores(id_in INT, _new_id_cargo INT, _new_first_name VARCHAR(100), _new_last_name VARCHAR(100), _new_is_superuser BOOLEAN, _new_username VARCHAR(50), _new_url_imagem VARCHAR(2048), _new_password VARCHAR(255), OUT _new_utilizador JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE utilizadores
    SET id_cargo = _new_id_cargo, first_name = _new_first_name, last_name = _new_last_name, is_superuser = _new_is_superuser, username = _new_username, url_imagem = _new_url_imagem, password = _new_password
    WHERE id = id_in
    RETURNING row_to_json(utilizadores) INTO _new_utilizador;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_utilizadores(id_in INT, OUT _id INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM utilizadores
    WHERE id = id_in
    RETURNING id INTO _id;
END;
$$;

-- CREATE OR REPLACE PROCEDURE create_utilizadorescargos(_new_id_utilizador INT, _new_id_cargo INT, OUT _new_utilizador_cargo JSON)
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
--     INSERT INTO utilizadorescargos (id_utilizador, id_cargo)
--     VALUES (_new_id_utilizador, _new_id_cargo)
--     RETURNING row_to_json(utilizadorescargos) INTO _new_utilizador_cargo;
-- END;
-- $$;

-- CREATE OR REPLACE PROCEDURE update_utilizadorescargos(id_utilizador_cargo_in INT, _new_id_utilizador INT, _new_id_cargo INT, OUT _new_utilizador_cargo JSON)
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
--     UPDATE utilizadorescargos
--     SET id_utilizador = _new_id_utilizador, id_cargo = _new_id_cargo
--     WHERE id_utilizador_cargo = id_utilizador_cargo_in
--     RETURNING row_to_json(utilizadorescargos) INTO _new_utilizador_cargo;
-- END;
-- $$;

-- CREATE OR REPLACE PROCEDURE delete_utilizadorescargos(id_utilizador_cargo_in INT)
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
--     DELETE FROM utilizadorescargos
--     WHERE id_utilizador_cargo = id_utilizador_cargo_in;
-- END;
-- $$;

CREATE OR REPLACE PROCEDURE create_estadosmesas(_new_designacao VARCHAR(100), OUT _new_estado_mesa JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO estadosmesas (designacao)
    VALUES (_new_designacao)
    RETURNING row_to_json(estadosmesas) INTO _new_estado_mesa;
END;
$$;

CREATE OR REPLACE PROCEDURE update_estadosmesas(id_estado_mesa_in INT, _new_designacao VARCHAR(100), OUT _new_estado_mesa JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE estadosmesas
    SET designacao = _new_designacao
    WHERE id_estado_mesa = id_estado_mesa_in
    RETURNING row_to_json(estadosmesas) INTO _new_estado_mesa;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_estadosmesas(id_estado_mesa_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM estadosmesas
    WHERE id_estado_mesa = id_estado_mesa_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_fornecedores(_new_nome VARCHAR(100), _new_vende_ingredientes BOOLEAN, _new_vende_utensilios BOOLEAN, _new_morada VARCHAR(255), _new_email VARCHAR(255), _new_telemovel VARCHAR(50), OUT _new_fornecedor JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO fornecedores (nome, vende_ingredientes, vende_utensilios, morada, email, telemovel)
    VALUES (_new_nome, _new_vende_ingredientes, _new_vende_utensilios, _new_morada, _new_email, _new_telemovel)
    RETURNING row_to_json(fornecedores) INTO _new_fornecedor; 
END;
$$;

CREATE OR REPLACE PROCEDURE update_fornecedores(id_fornecedor_in INT, _new_nome VARCHAR(100), _new_vende_ingredientes BOOLEAN, _new_vende_utensilios BOOLEAN, _new_morada VARCHAR(255), _new_email VARCHAR(255), _new_telemovel VARCHAR(50), OUT _new_fornecedor JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE fornecedores
    SET nome = _new_nome, vende_ingredientes = _new_vende_ingredientes, vende_utensilios = _new_vende_utensilios, morada = _new_morada, email = _new_email, telemovel = _new_telemovel
    WHERE id_fornecedor = id_fornecedor_in
    RETURNING row_to_json(fornecedores) INTO _new_fornecedor;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_fornecedores(id_fornecedor_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM fornecedores
    WHERE id_fornecedor = id_fornecedor_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_carrinhos(_new_preco_total DECIMAL(10, 2), _new_data_compra TIMESTAMP, OUT _new_carrinho JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO carrinhos (preco_total, data_compra)
    VALUES (_new_preco_total, _new_data_compra)
    RETURNING row_to_json(carrinhos) INTO _new_carrinho;
END;
$$;

CREATE OR REPLACE PROCEDURE update_carrinhos(id_carrinho_in INT, _new_preco_total DECIMAL(10, 2), _new_data_compra TIMESTAMP, OUT _new_carrinho JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE carrinhos
    SET preco_total = _new_preco_total, data_compra = _new_data_compra
    WHERE id_carrinho = id_carrinho_in
    RETURNING row_to_json(carrinhos) INTO _new_carrinho;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_carrinhos(id_carrinho_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM carrinhos
    WHERE id_carrinho = id_carrinho_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_ingredientes(_new_id_fornecedor INT, _new_nome VARCHAR(255), _new_url_imagem VARCHAR(2048), _new_quantidade_stock INT, _new_unidade_medida VARCHAR(50), _new_limite_stock INT, _new_preco DECIMAL(10, 2), OUT _new_ingrediente JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO ingredientes (id_fornecedor, nome, url_imagem, quantidade_stock, unidade_medida, limite_stock, preco)
    VALUES (_new_id_fornecedor, _new_nome, _new_url_imagem, _new_quantidade_stock, _new_unidade_medida, _new_limite_stock, _new_preco)
    RETURNING row_to_json(ingredientes) INTO _new_ingrediente;
END;
$$;

CREATE OR REPLACE PROCEDURE update_ingredientes(id_ingrediente_in INT, _new_id_fornecedor INT, _new_nome VARCHAR(255), _new_url_imagem VARCHAR(2048), _new_quantidade_stock INT, _new_unidade_medida VARCHAR(50), _new_limite_stock INT, _new_preco DECIMAL(10, 2), OUT _new_ingrediente JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE ingredientes
    SET id_fornecedor = _new_id_fornecedor, nome = _new_nome, url_imagem = _new_url_imagem, quantidade_stock = _new_quantidade_stock, unidade_medida = _new_unidade_medida, limite_stock = _new_limite_stock, preco = _new_preco
    WHERE id_ingrediente = id_ingrediente_in
    RETURNING row_to_json(ingredientes) INTO _new_ingrediente;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_ingredientes(id_ingrediente_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM ingredientes
    WHERE id_ingrediente = id_ingrediente_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_ingredientescarrinhos(_new_id_carrinho INT, _new_id_ingrediente INT, _new_id_administrador INT, _new_quantidade INT, OUT _new_ingrediente_carrinho JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO ingredientescarrinhos (id_ingrediente, id_administrador, id_carrinho, quantidade)
    VALUES (_new_id_ingrediente, _new_id_administrador, _new_id_carrinho, _new_quantidade)
    RETURNING row_to_json(ingredientescarrinhos) INTO _new_ingrediente_carrinho;
END;
$$;

CREATE OR REPLACE PROCEDURE update_ingredientescarrinhos(id_ingrediente_carrinho_in INT, _new_quantidade INT, OUT _new_ingrediente_carrinho JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE ingredientescarrinhos
    SET quantidade = _new_quantidade
    WHERE id_ingrediente_carrinho = id_ingrediente_carrinho_in
    RETURNING row_to_json(ingredientescarrinhos) INTO _new_ingrediente_carrinho;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_ingredientescarrinhos(id_ingrediente_carrinho_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM ingredientescarrinhos
    WHERE id_ingrediente_carrinho = id_ingrediente_carrinho_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_utensilios(_new_id_fornecedor INT, _new_nome VARCHAR(100), _new_url_imagem VARCHAR(2048), _new_quantidade_stock INT, _new_unidade_medida VARCHAR(50), _new_limite_stock INT, _new_preco DECIMAL(10, 2), OUT _new_utensilio JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO utensilios (id_fornecedor, nome, url_imagem, quantidade_stock, unidade_medida, limite_stock, preco)
    VALUES (_new_id_fornecedor, _new_nome, _new_url_imagem, _new_quantidade_stock, _new_unidade_medida, _new_limite_stock, _new_preco)
    RETURNING row_to_json(utensilios) INTO _new_utensilio;
END;
$$;

CREATE OR REPLACE PROCEDURE update_utensilios(id_utensilio_in INT, _new_id_fornecedor INT, _new_nome VARCHAR(100), _new_url_imagem VARCHAR(2048), _new_quantidade_stock INT, _new_unidade_medida VARCHAR(50), _new_limite_stock INT, _new_preco DECIMAL(10, 2), OUT _new_utensilio JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE utensilios
    SET id_fornecedor = _new_id_fornecedor, nome = _new_nome, url_imagem = _new_url_imagem, quantidade_stock = _new_quantidade_stock, unidade_medida = _new_unidade_medida, limite_stock = _new_limite_stock, preco = _new_preco
    WHERE id_utensilio = id_utensilio_in
    RETURNING row_to_json(utensilios) INTO _new_utensilio;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_utensilios(id_utensilio_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM utensilios
    WHERE id_utensilio = id_utensilio_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_utensilioscarrinhos(_new_id_carrinho INT, _new_id_utensilio INT, _new_id_administrador INT, _new_quantidade INT, OUT _new_utensilio_carrinho JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO utensilioscarrinhos (id_utensilio, id_administrador, id_carrinho, quantidade)
    VALUES (_new_id_utensilio, _new_id_administrador, _new_id_carrinho, _new_quantidade)
    RETURNING row_to_json(utensilioscarrinhos) INTO _new_utensilio_carrinho;
END;
$$;

CREATE OR REPLACE PROCEDURE update_utensilioscarrinhos(id_utensilio_carrinho_in INT, _new_quantidade INT, OUT _new_utensilio_carrinho JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE utensilioscarrinhos
    SET quantidade = _new_quantidade
    WHERE id_utensilio_carrinho = id_utensilio_carrinho_in
    RETURNING row_to_json(utensilioscarrinhos) INTO _new_utensilio_carrinho;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_utensilioscarrinhos(id_utensilio_carrinho_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM utensilioscarrinhos
    WHERE id_utensilio_carrinho = id_utensilio_carrinho_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_receitas(_new_nome VARCHAR(100), _new_duracao INTERVAL, OUT _new_receita JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO receitas (nome, duracao)
    VALUES (_new_nome, _new_duracao)
    RETURNING row_to_json(receitas) INTO _new_receita;
END;
$$;

CREATE OR REPLACE PROCEDURE update_receitas(id_receita_in INT, _new_nome VARCHAR(100), _new_duracao INTERVAL, OUT _new_receita JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE receitas
    SET nome = _new_nome, duracao = _new_duracao
    WHERE id_receita = id_receita_in
    RETURNING row_to_json(receitas) INTO _new_receita;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_receitas(id_receita_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM receitas
    WHERE id_receita = id_receita_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_ingredientesreceitas(_new_id_receita INT, _new_id_ingrediente INT, _new_quantidade INT, OUT _new_ingrediente_receita JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO ingredientesreceitas (id_receita, id_ingrediente, quantidade)
    VALUES (_new_id_receita, _new_id_ingrediente, _new_quantidade)
    RETURNING row_to_json(ingredientesreceitas) INTO _new_ingrediente_receita;
END;
$$;

CREATE OR REPLACE PROCEDURE update_ingredientesreceitas(id_ingrediente_receita_in INT, _new_quantidade INT, OUT _new_ingrediente_receita JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE ingredientesreceitas
    SET quantidade = _new_quantidade
    WHERE id_ingrediente_receita = id_ingrediente_receita_in
    RETURNING row_to_json(ingredientesreceitas) INTO _new_ingrediente_receita;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_ingredientesreceitas(id_ingrediente_receita_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM ingredientesreceitas
    WHERE id_ingrediente_receita = id_ingrediente_receita_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_utensiliosreceitas(_new_id_receita INT, _new_id_utensilio INT, _new_quantidade INT, OUT _new_utensilio_receita JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO utensiliosreceitas (id_receita, id_utensilio, quantidade)
    VALUES (_new_id_receita, _new_id_utensilio, _new_quantidade)
    RETURNING row_to_json(utensiliosreceitas) INTO _new_utensilio_receita;
END;
$$;

CREATE OR REPLACE PROCEDURE update_utensiliosreceitas(id_utensilio_receita_in INT, _new_quantidade INT, OUT _new_utensilio_receita JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE utensiliosreceitas
    SET quantidade = _new_quantidade
    WHERE id_utensilio_receita = id_utensilio_receita_in
    RETURNING row_to_json(utensiliosreceitas) INTO _new_utensilio_receita;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_utensiliosreceitas(id_utensilio_receita_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM utensiliosreceitas
    WHERE id_utensilio_receita = id_utensilio_receita_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_instrucoes(_new_id_receita INT, _new_descricao TEXT, OUT _new_instrucao JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO instrucoes (id_receita, descricao) -- Trigger 'set_next_numero_sequencia_trigger' define o numero_sequencia antes de inserir
    VALUES (_new_id_receita, _new_descricao)
    RETURNING row_to_json(instrucoes) INTO _new_instrucao;
END;
$$;

CREATE OR REPLACE PROCEDURE update_instrucoes(id_instrucao_in INT, _new_numero_sequencia INT, _new_descricao TEXT, OUT _new_instrucao JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE instrucoes
    SET numero_sequencia = _new_numero_sequencia, descricao = _new_descricao
    WHERE id_instrucao = id_instrucao_in
    RETURNING row_to_json(instrucoes) INTO _new_instrucao;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_instrucoes(id_instrucao_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM instrucoes
    WHERE id_instrucao = id_instrucao_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_mesas(_new_id_estado_mesa INT, _new_numero INT, _new_capacidade_maxima INT, OUT _new_mesa JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO mesas (id_estado_mesa, numero, capacidade_maxima)
    VALUES (_new_id_estado_mesa, _new_numero, _new_capacidade_maxima)
    RETURNING row_to_json(mesas) INTO _new_mesa;
END;
$$;

CREATE OR REPLACE PROCEDURE update_mesas(id_mesa_in INT, _new_id_estado_mesa INT, _new_numero INT, _new_capacidade_maxima INT, OUT _new_mesa JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE mesas
    SET id_estado_mesa = _new_id_estado_mesa, numero = _new_numero, capacidade_maxima = _new_capacidade_maxima
    WHERE id_mesa = id_mesa_in
    RETURNING row_to_json(mesas) INTO _new_mesa;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_mesas(id_mesa_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM mesas
    WHERE id_mesa = id_mesa_in;
END;
$$;

-- CREATE OR REPLACE PROCEDURE create_produtos(_new_item BOOLEAN, _new_menu BOOLEAN, _new_nome VARCHAR(100), _new_url_imagem VARCHAR(2048), _new_preco DECIMAL(10, 2), OUT _new_produto JSON)
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
--     INSERT INTO produtos (item, menu, nome, url_imagem, preco)
--     VALUES (_new_item, _new_menu, _new_nome, _new_url_imagem, _new_preco)
--     RETURNING row_to_json(produtos) INTO _new_produto;
-- END;
-- $$;

-- CREATE OR REPLACE PROCEDURE update_produtos(id_produto_in INT, _new_item BOOLEAN, _new_menu BOOLEAN, _new_nome VARCHAR(100), _new_url_imagem VARCHAR(2048), _new_preco DECIMAL(10, 2), OUT _new_produto JSON)
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
--     UPDATE produtos
--     SET item = _new_item, menu = _new_menu, nome = _new_nome, url_imagem = _new_url_imagem, preco = _new_preco
--     WHERE id_produto = id_produto_in
--     RETURNING row_to_json(produtos) INTO _new_produto;
-- END;
-- $$;

-- CREATE OR REPLACE PROCEDURE delete_produtos(id_produto_in INT)
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
--     DELETE FROM produtos
--     WHERE id_produto = id_produto_in;
-- END;
-- $$;

CREATE OR REPLACE PROCEDURE create_tipos(_new_designacao VARCHAR(100), OUT _new_tipo JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO tipos (designacao)
    VALUES (_new_designacao)
    RETURNING row_to_json(tipos) INTO _new_tipo;
END;
$$;

CREATE OR REPLACE PROCEDURE update_tipos(id_tipo_in INT, _new_designacao VARCHAR(100), OUT _new_tipo JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE tipos
    SET designacao = _new_designacao
    WHERE id_tipo = id_tipo_in
    RETURNING row_to_json(tipos) INTO _new_tipo;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_tipos(id_tipo_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM tipos
    WHERE id_tipo = id_tipo_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_itens(_new_nome VARCHAR(100), _new_url_imagem VARCHAR(2048), _new_preco DECIMAL(10,2), _new_porcao_unidade_medida VARCHAR(50), _new_porcao INT, OUT _new_item JSON)
LANGUAGE plpgsql
AS $$
DECLARE _new_id_produto INT;
BEGIN
    -- Cria o produto
    INSERT INTO produtos (item, menu, nome, url_imagem, preco)
    VALUES (TRUE, FALSE, _new_nome, _new_url_imagem, _new_preco)
    RETURNING id_produto INTO _new_id_produto;

    -- Cria o item com o id do produto
    INSERT INTO itens (id_item, porcao_unidade_medida, porcao)
    VALUES (_new_id_produto, _new_porcao_unidade_medida, _new_porcao);

    SELECT row_to_json(item_completo) INTO _new_item FROM (
        SELECT * 
        FROM itens 
        JOIN produtos ON produtos.id_produto = itens.id_item 
        WHERE id_item = _new_id_produto
    ) item_completo;
END;
$$;


CREATE OR REPLACE PROCEDURE update_itens(_id_item_in INT, _new_nome VARCHAR(100), _new_url_imagem VARCHAR(2048), _new_preco DECIMAL(10,2), _new_porcao_unidade_medida VARCHAR(50), _new_porcao INT, OUT _updated_item JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Update produto
    UPDATE produtos
    SET nome = _new_nome, url_imagem = _new_url_imagem, preco = _new_preco
    WHERE id_produto = _id_item_in;

    -- Update item
    UPDATE itens
    SET porcao_unidade_medida = _new_porcao_unidade_medida, porcao = _new_porcao
    WHERE id_item = _id_item_in;

    SELECT row_to_json(item_completo) INTO _updated_item FROM (
        SELECT * 
        FROM itens 
        JOIN produtos ON produtos.id_produto = itens.id_item 
        WHERE id_item = _id_item_in
    ) item_completo;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_itens(_id_item INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM produtos WHERE id_produto = _id_item; -- Delete produto
    -- o item é apagado junto com o produto (CASCADE)
END;
$$;


CREATE OR REPLACE PROCEDURE create_itenstipos(_new_id_item INT, _new_id_tipo INT, OUT _new_item_tipo JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO itenstipos (id_item, id_tipo)
    VALUES (_new_id_item, _new_id_tipo)
    RETURNING row_to_json(itenstipos) INTO _new_item_tipo;
END;
$$;

CREATE OR REPLACE PROCEDURE update_itenstipos(id_item_tipo_in INT, _new_id_item INT, _new_id_tipo INT, OUT _new_item_tipo JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE itenstipos
    SET id_item = _new_id_item, id_tipo = _new_id_tipo
    WHERE id_item_tipo = id_item_tipo_in
    RETURNING row_to_json(itenstipos) INTO _new_item_tipo;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_itenstipos(id_item_tipo_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM itenstipos
    WHERE id_item_tipo = id_item_tipo_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_categorias(_new_designacao VARCHAR(100), OUT _new_categoria JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO categorias (designacao)
    VALUES (_new_designacao)
    RETURNING row_to_json(categorias) INTO _new_categoria;
END;
$$;

CREATE OR REPLACE PROCEDURE update_categorias(id_categoria_in INT, _new_designacao VARCHAR(100), OUT _new_categoria JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE categorias
    SET designacao = _new_designacao
    WHERE id_categoria = id_categoria_in
    RETURNING row_to_json(categorias) INTO _new_categoria;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_categorias(id_categoria_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM categorias
    WHERE id_categoria = id_categoria_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_itenscategorias(_new_id_item INT, _new_id_categoria INT, OUT _new_item_categoria JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO itenscategorias (id_item, id_categoria)
    VALUES (_new_id_item, _new_id_categoria)
    RETURNING row_to_json(itenscategorias) INTO _new_item_categoria;
END;
$$;

CREATE OR REPLACE PROCEDURE update_itenscategorias(id_item_categoria_in INT, _new_id_item INT, _new_id_categoria INT, OUT _new_item_categoria JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE itenscategorias
    SET id_item = _new_id_item, id_categoria = _new_id_categoria
    WHERE id_item_categoria = id_item_categoria_in
    RETURNING row_to_json(itenscategorias) INTO _new_item_categoria;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_itenscategorias(id_item_categoria_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM itenscategorias
    WHERE id_item_categoria = id_item_categoria_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_opcoes(_new_designacao VARCHAR(100), OUT _new_opcao JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO opcoes (designacao)
    VALUES (_new_designacao)
    RETURNING row_to_json(opcoes) INTO _new_opcao;
END;
$$;

CREATE OR REPLACE PROCEDURE update_opcoes(id_opcao_in INT, _new_designacao VARCHAR(100), OUT _new_opcao JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE opcoes
    SET designacao = _new_designacao
    WHERE id_opcao = id_opcao_in
    RETURNING row_to_json(opcoes) INTO _new_opcao;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_opcoes(id_opcao_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM opcoes
    WHERE id_opcao = id_opcao_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_itensopcoes(_new_id_item INT, _new_id_opcao INT, OUT _new_item_opcao JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO itensopcoes (id_item, id_opcao)
    VALUES (_new_id_item, _new_id_opcao)
    RETURNING row_to_json(itensopcoes) INTO _new_item_opcao;
END;
$$;

CREATE OR REPLACE PROCEDURE update_itensopcoes(id_item_opcao_in INT, _new_id_item INT, _new_id_opcao INT, OUT _new_item_opcao JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE itensopcoes
    SET id_item = _new_id_item, id_opcao = _new_id_opcao
    WHERE id_item_opcao = id_item_opcao_in
    RETURNING row_to_json(itensopcoes) INTO _new_item_opcao;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_itensopcoes(id_item_opcao_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM itensopcoes
    WHERE id_item_opcao = id_item_opcao_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_menus(_new_nome VARCHAR(100), _new_url_imagem VARCHAR(2048), _new_preco DECIMAL(10,2), OUT _new_menu JSON)
LANGUAGE plpgsql
AS $$
DECLARE _new_id_produto INT;
BEGIN
    -- Cria o produto
    INSERT INTO produtos (item, menu, nome, url_imagem, preco)
    VALUES (FALSE, TRUE, _new_nome, _new_url_imagem, _new_preco)
    RETURNING id_produto INTO _new_id_produto;

    -- Cria o menu com o id do produto
    INSERT INTO menus (id_menu)
    VALUES (_new_id_produto);

    SELECT row_to_json(menu_completo) INTO _new_menu FROM (
        SELECT * 
        FROM menus
        JOIN produtos ON produtos.id_produto = menus.id_menu
        WHERE id_menu = _new_id_produto
    ) menu_completo;
END;
$$;


CREATE OR REPLACE PROCEDURE update_menus(_id_menu INT, _new_nome VARCHAR(100), _new_url_imagem VARCHAR(2048), _new_preco DECIMAL(10,2), OUT _updated_menu JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Update produto
    UPDATE produtos
    SET nome = _new_nome, url_imagem = _new_url_imagem, preco = _new_preco
    WHERE id_produto = _id_menu;

    -- update menu
    SELECT row_to_json(menu_completo) INTO _updated_menu FROM (
        SELECT * 
        FROM menus
        JOIN produtos ON produtos.id_produto = menus.id_menu
        WHERE id_menu = _id_menu
    ) menu_completo;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_menus(_id_menu INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM produtos WHERE id_produto = _id_menu; -- delete produto
    -- o menu é apagado junto com o produto (CASCADE)
END;
$$;

CREATE OR REPLACE PROCEDURE create_itensmenus(_new_id_menu INT, _new_id_item INT, OUT _new_item_menu JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO itensmenus (id_menu, id_item)
    VALUES (_new_id_menu, _new_id_item)
    RETURNING row_to_json(itensmenus) INTO _new_item_menu;
END;
$$;

-- CREATE OR REPLACE PROCEDURE update_itensmenus(id_item_menu_in INT, _new_id_item INT, _new_id_menu INT, OUT _new_item_menu JSON)
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
--     UPDATE itensmenus
--     SET id_item = _new_id_item, id_menu = _new_id_menu
--     WHERE id_item_menu = id_item_menu_in
--     RETURNING row_to_json(itensmenus) INTO _new_item_menu;
-- END;
-- $$;

CREATE OR REPLACE PROCEDURE delete_itensmenus(id_item_menu_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM itensmenus
    WHERE id_item_menu = id_item_menu_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_diassemana(_new_designacao VARCHAR(50), OUT _new_dia_semana JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO diassemana (designacao)
    VALUES (_new_designacao)
    RETURNING row_to_json(diassemana) INTO _new_dia_semana;
END;
$$;

CREATE OR REPLACE PROCEDURE update_diassemana(id_dia_semana_in INT, _new_designacao VARCHAR(50), OUT _new_dia_semana JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE diassemana
    SET designacao = _new_designacao
    WHERE id_dia_semana = id_dia_semana_in
    RETURNING row_to_json(diassemana) INTO _new_dia_semana;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_diassemana(id_dia_semana_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM diassemana
    WHERE id_dia_semana = id_dia_semana_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_menusdiassemana(_new_id_menu INT, _new_id_dia_semana INT, _new_almoco BOOLEAN, _new_jantar BOOLEAN, OUT _new_menu_dia_semana JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO menusdiassemana (id_menu, id_dia_semana, almoco, jantar)
    VALUES (_new_id_menu, _new_id_dia_semana, _new_almoco, _new_jantar)
    RETURNING row_to_json(menusdiassemana) INTO _new_menu_dia_semana;
END;
$$;

CREATE OR REPLACE PROCEDURE update_menusdiassemana(id_menu_dia_semana_in INT, _new_almoco BOOLEAN, _new_jantar BOOLEAN, OUT _new_menu_dia_semana JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE menusdiassemana
    SET almoco = _new_almoco, jantar = _new_jantar
    WHERE id_menu_dia_semana = id_menu_dia_semana_in
    RETURNING row_to_json(menusdiassemana) INTO _new_menu_dia_semana;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_menusdiassemana(id_menu_dia_semana_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM menusdiassemana
    WHERE id_menu_dia_semana = id_menu_dia_semana_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_servicos(_new_id_garcom INT, _new_id_mesa INT, OUT _new_servico JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO servicos (id_garcom, id_mesa)
    VALUES (_new_id_garcom, _new_id_mesa)
    RETURNING row_to_json(servicos) INTO _new_servico;
END;
$$;

CREATE OR REPLACE PROCEDURE update_servicos(id_servico_in INT, _new_id_garcom INT, _new_id_mesa INT, OUT _new_servico JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE servicos
    SET id_garcom = _new_id_garcom, id_mesa = _new_id_mesa
    WHERE id_servico = id_servico_in
    RETURNING row_to_json(servicos) INTO _new_servico;
END;
$$;

-- preco e atualizdo atraves de triggers

CREATE OR REPLACE PROCEDURE concluir_servicos(id_servico_in INT, OUT _new_servico JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE servicos
    SET data_hora_fim = NOW()
    WHERE id_servico = id_servico_in
    RETURNING row_to_json(servicos) INTO _new_servico;
END;
$$;

CREATE OR REPLACE PROCEDURE create_servico_com_reserva(_new_id_reserva INT, OUT _new_servico JSON)
LANGUAGE plpgsql
AS $$
DECLARE 
    _new_id_garcom INT; 
    _new_id_mesa INT;
    _new_id_servico INT;
BEGIN
    SELECT id_garcom, id_mesa 
    INTO _new_id_garcom, _new_id_mesa 
    FROM reservas 
    WHERE id_reserva = _new_id_reserva;

    INSERT INTO servicos (id_garcom, id_mesa)
    VALUES (_new_id_garcom, _new_id_mesa)
    RETURNING id_servico, row_to_json(servicos) INTO _new_id_servico, _new_servico;

    UPDATE reservas
    SET id_servico = _new_id_servico
    WHERE id_reserva = _new_id_reserva;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_servicos(id_servico_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM servicos
    WHERE id_servico = id_servico_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_pedidos(_new_id_servico INT, OUT _new_pedido JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO pedidos (id_servico)
    VALUES (_new_id_servico)
    RETURNING row_to_json(pedidos) INTO _new_pedido;
END;
$$;

-- CREATE OR REPLACE PROCEDURE update_pedidos(id_pedido_in INT, _new_id_servico INT, OUT _new_pedido JSON)
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
--     UPDATE pedidos
--     SET id_servico = _new_id_servico
--     WHERE id_pedido = id_pedido_in
--     RETURNING row_to_json(pedidos) INTO _new_pedido;
-- END;
-- $$;

CREATE OR REPLACE PROCEDURE delete_pedidos(id_pedido_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM pedidos
    WHERE id_pedido = id_pedido_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_pedidosprodutos(_new_id_pedido INT, _new_id_produto INT, OUT _new_pedido_produto JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO pedidosprodutos (id_pedido, id_produto)
    VALUES (_new_id_pedido, _new_id_produto)
    RETURNING row_to_json(pedidosprodutos) INTO _new_pedido_produto;
END;
$$;

-- CREATE OR REPLACE PROCEDURE update_pedidosprodutos(id_pedido_produto_in INT, _new_id_pedido INT, _new_id_produto INT, OUT _new_pedido_produto JSON)
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
--     UPDATE pedidosprodutos
--     SET id_pedido = _new_id_pedido, id_produto = _new_id_produto
--     WHERE id_pedido_produto = id_pedido_produto_in
--     RETURNING row_to_json(pedidosprodutos) INTO _new_pedido_produto;
-- END;
-- $$;

CREATE OR REPLACE PROCEDURE confecionar_pedidosprodutos(id_pedido_produto_in INT, _new_id_cozinheiro INT, OUT _new_pedido_produto JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE pedidosprodutos
    SET id_cozinheiro = _new_id_cozinheiro
    WHERE id_pedido_produto = id_pedido_produto_in
    RETURNING row_to_json(pedidosprodutos) INTO _new_pedido_produto;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_pedidosprodutos(
    id_pedido_produto_in INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM pedidosprodutos
    WHERE id_pedido_produto = id_pedido_produto_in;
END;
$$;

-- CREATE OR REPLACE PROCEDURE create_pedidosprodutositensopcoes(_new_id_item_opcao INT, _new_id_pedido_produto INT, OUT _new_pedido_produto_item_opcao JSON)
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
--     INSERT INTO pedidosprodutositensopcoes (id_item_opcao, id_pedido_produto)
--     VALUES (_new_id_item_opcao, _new_id_pedido_produto)
--     RETURNING row_to_json(pedidosprodutositensopcoes) INTO _new_pedido_produto_item_opcao;
-- END;
-- $$;

-- CREATE OR REPLACE PROCEDURE update_pedidosprodutositensopcoes(id_pedido_produto_item_opcao_in INT, _new_id_item_opcao INT, _new_id_pedido_produto INT, OUT _new_pedido_produto_item_opcao JSON)
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
--     UPDATE pedidosprodutositensopcoes
--     SET id_item_opcao = _new_id_item_opcao, id_pedido_produto = _new_id_pedido_produto
--     WHERE id_pedido_produto_item_opcao = id_pedido_produto_item_opcao_in
--     RETURNING row_to_json(pedidosprodutositensopcoes) INTO _new_pedido_produto_item_opcao;
-- END;
-- $$;

-- CREATE OR REPLACE PROCEDURE delete_pedidosprodutositensopcoes(id_pedido_produto_item_opcao_in INT)
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
--     DELETE FROM pedidosprodutositensopcoes
--     WHERE id_pedido_produto_item_opcao = id_pedido_produto_item_opcao_in;
-- END;
-- $$;

CREATE OR REPLACE PROCEDURE create_reservas(_new_id_mesa INT, _new_id_estado_reserva INT, _new_quantidade_pessoas INT, _new_observacoes TEXT, _new_id_garcom INT, _new_data_hora TIMESTAMP, OUT _new_reserva JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO reservas (id_mesa, id_estado_reserva, quantidade_pessoas, id_garcom, observacoes, data_hora)
    VALUES (_new_id_mesa, _new_id_estado_reserva, _new_quantidade_pessoas, _new_id_garcom, _new_observacoes, _new_data_hora)
    RETURNING row_to_json(reservas) INTO _new_reserva;
END;
$$;

CREATE OR REPLACE PROCEDURE update_reservas(id_reserva_in INT, _new_id_mesa INT, _new_id_estado_reserva INT, _new_quantidade_pessoas INT, _new_observacoes TEXT, _new_id_garcom INT, _new_data_hora TIMESTAMP, OUT _new_reserva JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE reservas
    SET id_mesa = _new_id_mesa, id_estado_reserva = _new_id_estado_reserva, quantidade_pessoas = _new_quantidade_pessoas, observacoes = _new_observacoes, id_garcom = _new_id_garcom, data_hora = _new_data_hora
    WHERE id_reserva = id_reserva_in
    RETURNING row_to_json(reservas) INTO _new_reserva;
END;
$$;


CREATE OR REPLACE PROCEDURE cancelar_reservas(id_reserva_in INT, OUT _new_reserva JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE reservas
    SET id_estado_reserva = (
        SELECT id_estado_reserva
        FROM estadosreservas
        WHERE designacao = 'Cancelada'
    )
    WHERE id_reserva = id_reserva_in
    RETURNING row_to_json(reservas) INTO _new_reserva;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_reservas(id_reserva_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM reservas
    WHERE id_reserva = id_reserva_in;
END;
$$;