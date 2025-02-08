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