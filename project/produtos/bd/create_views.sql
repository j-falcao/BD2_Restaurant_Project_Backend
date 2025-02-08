CREATE OR REPLACE VIEW produtos_view AS
SELECT * FROM produtos;

CREATE OR REPLACE VIEW categorias_view AS
SELECT * FROM categorias;

CREATE OR REPLACE VIEW tipos_view AS
SELECT * FROM tipos;

CREATE OR REPLACE VIEW opcoes_view AS
SELECT * FROM opcoes;

CREATE OR REPLACE VIEW itens_view AS
SELECT itens.*, produtos.nome, produtos.url_imagem, produtos.preco FROM itens
JOIN produtos ON itens.id_item = produtos.id_produto;

CREATE OR REPLACE VIEW itenscategorias_view AS
SELECT * FROM itenscategorias;

CREATE OR REPLACE VIEW itenstipos_view AS
SELECT * FROM itenstipos;

CREATE OR REPLACE VIEW itensopcoes_view AS
SELECT * FROM itensopcoes;

CREATE OR REPLACE VIEW menus_view AS
SELECT menus.*, produtos.nome, produtos.url_imagem, produtos.preco FROM menus
JOIN produtos ON menus.id_menu = produtos.id_produto;

CREATE OR REPLACE VIEW itensmenus_view AS
SELECT * FROM itensmenus;

CREATE OR REPLACE VIEW diassemana_view AS
SELECT * FROM diassemana;

CREATE OR REPLACE VIEW menusdiassemana_view AS
SELECT * FROM menusdiassemana;

CREATE OR REPLACE PROCEDURE get_categorias_by_item(_id_item_in INT, OUT resultado JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(categorias)) INTO resultado
    FROM categorias
    JOIN itenscategorias ic ON categorias.id_categoria = ic.id_categoria
    WHERE ic.id_item = _id_item_in;
END;
$$;

CREATE OR REPLACE PROCEDURE get_itens_by_categoria(_id_categoria_in INT, OUT resultado JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(itens)) INTO resultado
    FROM (
        SELECT itens.*, produtos.nome, produtos.url_imagem, produtos.preco  FROM itens
        JOIN produtos ON itens.id_item = produtos.id_produto
    ) itens
    JOIN itenscategorias ic ON itens.id_item = ic.id_item
    WHERE ic.id_categoria = _id_categoria_in;
END;
$$;

CREATE OR REPLACE PROCEDURE get_tipos_by_item(_id_item_in INT, OUT resultado JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(tipos)) INTO resultado
    FROM tipos
    JOIN itenstipos it ON tipos.id_tipo = it.id_tipo
    WHERE it.id_item = _id_item_in;
END;
$$;

CREATE OR REPLACE PROCEDURE get_itens_by_tipo(_id_tipo_in INT, OUT resultado JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(itens)) INTO resultado
    FROM (
        SELECT itens.*, produtos.nome, produtos.url_imagem, produtos.preco FROM itens
        JOIN produtos ON itens.id_item = produtos.id_produto
    ) itens
    JOIN itenstipos it ON itens.id_item = it.id_item
    WHERE it.id_tipo = _id_tipo_in;
END;
$$;

CREATE OR REPLACE PROCEDURE get_opcoes_by_item(_id_item_in INT, OUT resultado JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(opcoes)) INTO resultado
    FROM opcoes
    JOIN itensopcoes io ON opcoes.id_opcao = io.id_opcao
    WHERE io.id_item = _id_item_in;
END;
$$;

CREATE OR REPLACE PROCEDURE get_itens_by_opcao(_id_opcao_in INT, OUT resultado JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(itens)) INTO resultado
    FROM (
        SELECT itens.*, produtos.nome, produtos.url_imagem, produtos.preco FROM itens
        JOIN produtos ON itens.id_item = produtos.id_produto
    ) itens
    JOIN itensopcoes io ON itens.id_item = io.id_item
    WHERE io.id_opcao = _id_opcao_in;
END;
$$;

CREATE OR REPLACE PROCEDURE get_menus_by_item(_id_item_in INT, OUT resultado JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(menus)) INTO resultado
    FROM (
        SELECT menus.*, produtos.nome, produtos.url_imagem, produtos.preco FROM menus
        JOIN produtos ON menus.id_menu = produtos.id_produto
    ) menus
    JOIN itensmenus im ON menus.id_menu = im.id_menu
    WHERE im.id_item = _id_item_in;
END;
$$;

CREATE OR REPLACE PROCEDURE get_itens_by_menu(_id_menu_in INT, OUT resultado JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(itens)) INTO resultado
    FROM (
        SELECT itens.*, produtos.nome, produtos.url_imagem, produtos.preco FROM itens
        JOIN produtos ON itens.id_item = produtos.id_produto
    ) itens
    JOIN itensmenus im ON itens.id_item = im.id_item
    WHERE im.id_menu = _id_menu_in;
END;
$$;

CREATE OR REPLACE PROCEDURE get_menus_by_diasemana(_id_dia_semana INT, OUT resultado JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(menus)) INTO resultado
    FROM (
        SELECT menus.*, produtos.nome, produtos.url_imagem, produtos.preco FROM menus
        JOIN produtos ON menus.id_menu = produtos.id_produto
    ) menus
    JOIN menusdiassemana ON menus.id_menu = menusdiassemana.id_menu
    WHERE menusdiassemana.id_dia_semana = _id_dia_semana;
END;
$$;

CREATE OR REPLACE PROCEDURE get_diassemana_by_menu(_id_menu INT, OUT resultado JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(diassemana)) INTO resultado
    FROM diassemana
    JOIN menusdiassemana ON diassemana.id_dia_semana = menusdiassemana.id_dia_semana
    WHERE menusdiassemana.id_menu = _id_menu;
END;
$$;

