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

CREATE OR REPLACE PROCEDURE comprar_carrinho_atual_ingredientes(OUT _new_carrinho JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE carrinhos AS c
    SET data_compra = CURRENT_TIMESTAMP
    FROM tiposcarrinhos AS t
    WHERE c.data_compra IS NULL
    AND c.id_tipo_carrinho = t.id_tipo_carrinho -- join
    AND t.designacao = 'Ingredientes'
    RETURNING row_to_json(c) INTO _new_carrinho;
END;
$$;

CREATE OR REPLACE PROCEDURE comprar_carrinho_atual_utensilios(OUT _new_carrinho JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE carrinhos AS c
    SET data_compra = CURRENT_TIMESTAMP
    FROM tiposcarrinhos AS t
    WHERE c.data_compra IS NULL
    AND c.id_tipo_carrinho = t.id_tipo_carrinho -- join
    AND t.designacao = 'Utensilios'
    RETURNING row_to_json(c) INTO _new_carrinho;
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

CREATE OR REPLACE PROCEDURE create_ingredientescarrinhos_atual(_new_id_ingrediente INT, _new_id_administrador INT, _new_quantidade INT, OUT _new_ingrediente_carrinho JSON)
LANGUAGE plpgsql
AS $$
DECLARE _id_carrinho_atual INT;
BEGIN
    SELECT id_carrinho INTO _id_carrinho_atual FROM carrinhos WHERE data_compra IS NULL AND id_tipo_carrinho = (SELECT id_tipo_carrinho FROM tiposcarrinhos WHERE designacao = 'Ingredientes');

    INSERT INTO ingredientescarrinhos (id_ingrediente, id_administrador, id_carrinho, quantidade)
    VALUES (_new_id_ingrediente, _new_id_administrador, _id_carrinho_atual, _new_quantidade)
    RETURNING row_to_json(ingredientescarrinhos) INTO _new_ingrediente_carrinho;
END;
$$;

CREATE OR REPLACE PROCEDURE update_ingredientescarrinhos_atual(id_ingrediente_carrinho_in INT, _new_quantidade INT, OUT _new_ingrediente_carrinho JSON)
LANGUAGE plpgsql
AS $$
DECLARE 
    _id_carrinho INT;
    _id_carrinho_atual INT;
BEGIN
    SELECT id_carrinho 
    INTO _id_carrinho 
    FROM carrinhos 
    WHERE id_carrinho = (
        SELECT id_carrinho 
        FROM ingredientescarrinhos 
        WHERE id_ingrediente_carrinho = id_ingrediente_carrinho_in
    );

    SELECT id_carrinho INTO _id_carrinho_atual FROM carrinhos WHERE data_compra IS NULL AND id_tipo_carrinho = (SELECT id_tipo_carrinho FROM tiposcarrinhos WHERE designacao = 'Ingredientes');

    IF _id_carrinho != _id_carrinho_atual THEN
        RAISE EXCEPTION 'Não é possível atualizar um carrinho inativo';
    END IF;

    UPDATE ingredientescarrinhos
    SET quantidade = _new_quantidade
    WHERE id_ingrediente_carrinho = id_ingrediente_carrinho_in
    RETURNING row_to_json(ingredientescarrinhos) INTO _new_ingrediente_carrinho;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_ingredientescarrinhos_atual(id_ingrediente_carrinho_in INT)
LANGUAGE plpgsql
AS $$
DECLARE 
    _id_carrinho INT;
    _id_carrinho_atual INT;
BEGIN
    SELECT id_carrinho 
    INTO _id_carrinho 
    FROM carrinhos 
    WHERE id_carrinho = (
        SELECT id_carrinho 
        FROM ingredientescarrinhos 
        WHERE id_ingrediente_carrinho = id_ingrediente_carrinho_in
    );

    SELECT id_carrinho INTO _id_carrinho_atual FROM carrinhos WHERE data_compra IS NULL AND id_tipo_carrinho = (SELECT id_tipo_carrinho FROM tiposcarrinhos WHERE designacao = 'Ingredientes');

    IF _id_carrinho != _id_carrinho_atual THEN
        RAISE EXCEPTION 'Não é possível atualizar um carrinho inativo';
    END IF;

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

CREATE OR REPLACE PROCEDURE create_utensilioscarrinhos_atual(_new_id_utensilio INT, _new_id_administrador INT, _new_quantidade INT, OUT _new_utensilio_carrinho JSON)
LANGUAGE plpgsql
AS $$
DECLARE _id_carrinho_atual INT;
BEGIN
    SELECT id_carrinho INTO _id_carrinho_atual FROM carrinhos WHERE data_compra IS NULL AND id_tipo_carrinho = (SELECT id_tipo_carrinho FROM tiposcarrinhos WHERE designacao = 'Utensilios');

    INSERT INTO utensilioscarrinhos (id_utensilio, id_administrador, id_carrinho, quantidade)
    VALUES (_new_id_utensilio, _new_id_administrador, _id_carrinho_atual, _new_quantidade)
    RETURNING row_to_json(utensilioscarrinhos) INTO _new_utensilio_carrinho;
END;
$$;

CREATE OR REPLACE PROCEDURE update_utensilioscarrinhos_atual(id_utensilio_carrinho_in INT, _new_quantidade INT, OUT _new_utensilio_carrinho JSON)
LANGUAGE plpgsql
AS $$
DECLARE 
    _id_carrinho INT;
    _id_carrinho_atual INT;
BEGIN
    SELECT id_carrinho 
    INTO _id_carrinho 
    FROM carrinhos 
    WHERE id_carrinho = (
        SELECT id_carrinho 
        FROM utensilioscarrinhos 
        WHERE id_utensilio_carrinho = id_utensilio_carrinho_in
    );

    SELECT id_carrinho INTO _id_carrinho_atual FROM carrinhos WHERE data_compra IS NULL AND id_tipo_carrinho = (SELECT id_tipo_carrinho FROM tiposcarrinhos WHERE designacao = 'Utensilios');

    IF _id_carrinho != _id_carrinho_atual THEN
        RAISE EXCEPTION 'Não é possível atualizar um carrinho inativo';
    END IF;

    UPDATE utensilioscarrinhos
    SET quantidade = _new_quantidade
    WHERE id_utensilio_carrinho = id_utensilio_carrinho_in
    RETURNING row_to_json(utensilioscarrinhos) INTO _new_utensilio_carrinho;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_utensilioscarrinhos_atual(id_utensilio_carrinho_in INT)
LANGUAGE plpgsql
AS $$
DECLARE 
    _id_carrinho INT;
    _id_carrinho_atual INT;
BEGIN
    SELECT id_carrinho 
    INTO _id_carrinho 
    FROM carrinhos 
    WHERE id_carrinho = (
        SELECT id_carrinho 
        FROM utensilioscarrinhos 
        WHERE id_utensilio_carrinho = id_utensilio_carrinho_in
    );

    SELECT id_carrinho INTO _id_carrinho_atual FROM carrinhos WHERE data_compra IS NULL AND id_tipo_carrinho = (SELECT id_tipo_carrinho FROM tiposcarrinhos WHERE designacao = 'Utensilios');

    IF _id_carrinho != _id_carrinho_atual THEN
        RAISE EXCEPTION 'Não é possível atualizar um carrinho inativo';
    END IF;
    
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