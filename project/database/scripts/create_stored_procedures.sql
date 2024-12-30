CREATE OR REPLACE PROCEDURE create_cargos(_new_designacao VARCHAR(100))
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO cargos (designacao)
    VALUES (_new_designacao);
END;
$$;

CREATE OR REPLACE PROCEDURE update_cargos(id_cargo_in INT, _new_designacao VARCHAR(100))
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE cargos
    SET designacao = _new_designacao
    WHERE id_cargo = id_cargo_in;
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


CREATE OR REPLACE PROCEDURE create_utilizadores(_new_username VARCHAR(50), _new_first_name VARCHAR(100), _new_last_name VARCHAR(100), _new_is_superuser BOOLEAN, _new_url_imagem VARCHAR(2048), _new_password VARCHAR(255), OUT _id INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO utilizadores (username, first_name, last_name, is_superuser, url_imagem, password)
    VALUES (_new_username, _new_first_name, _new_last_name, _new_is_superuser, _new_url_imagem, _new_password)
    RETURNING id INTO _id;
END;
$$;


CREATE OR REPLACE PROCEDURE update_utilizadores(id_in INT, _new_first_name VARCHAR(100), _new_last_name VARCHAR(100), _new_is_superuser BOOLEAN, _new_username VARCHAR(50), _new_url_imagem VARCHAR(2048), _new_password VARCHAR(255), OUT _id INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE utilizadores
    SET first_name = _new_first_name, last_name = _new_last_name, is_superuser = _new_is_superuser, username = _new_username, url_imagem = _new_url_imagem, password = _new_password
    WHERE id = id_in
    RETURNING id INTO _id;
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

CREATE OR REPLACE PROCEDURE create_utilizadorescargos(_new_id_utilizador INT, _new_id_cargo INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO utilizadorescargos (id_utilizador, id_cargo)
    VALUES (_new_id_utilizador, _new_id_cargo);
END;
$$;

CREATE OR REPLACE PROCEDURE update_utilizadorescargos(id_utilizador_cargo_in INT, _new_id_utilizador INT, _new_id_cargo INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE utilizadorescargos
    SET id_utilizador = _new_id_utilizador, id_cargo = _new_id_cargo
    WHERE id_utilizador_cargo = id_utilizador_cargo_in;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_utilizadorescargos(id_utilizador_cargo_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM utilizadorescargos
    WHERE id_utilizador_cargo = id_utilizador_cargo_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_estadosmesas(_new_designacao VARCHAR(100))
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO estadosmesas (designacao)
    VALUES (_new_designacao);
END;
$$;

CREATE OR REPLACE PROCEDURE update_estadosmesas(id_estado_mesa_in INT, _new_designacao VARCHAR(100))
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE estadosmesas
    SET designacao = _new_designacao
    WHERE id_estado_mesa = id_estado_mesa_in;
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

CREATE OR REPLACE PROCEDURE create_fornecedores(_new_nome VARCHAR(100), _new_vende_ingredientes BOOLEAN, _new_vende_utensilios BOOLEAN, _new_morada VARCHAR(255), _new_email VARCHAR(255), _new_telemovel VARCHAR(50))
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO fornecedores (nome, vende_ingredientes, vende_utensilios, morada, email, telemovel)
    VALUES (_new_nome, _new_vende_ingredientes, _new_vende_utensilios, _new_morada, _new_email, _new_telemovel);
END;
$$;

CREATE OR REPLACE PROCEDURE update_fornecedores(id_fornecedor_in INT, _new_nome VARCHAR(100), _new_vende_ingredientes BOOLEAN, _new_vende_utensilios BOOLEAN, _new_morada VARCHAR(255), _new_email VARCHAR(255), _new_telemovel VARCHAR(50))
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE fornecedores
    SET nome = _new_nome, vende_ingredientes = _new_vende_ingredientes, vende_utensilios = _new_vende_utensilios, morada = _new_morada, email = _new_email, telemovel = _new_telemovel
    WHERE id_fornecedor = id_fornecedor_in;
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

CREATE OR REPLACE PROCEDURE create_carrinhos(_new_preco_total DECIMAL(10, 2), _new_data_compra TIMESTAMP)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO carrinhos (preco_total, data_compra)
    VALUES (_new_preco_total, _new_data_compra);
END;
$$;

CREATE OR REPLACE PROCEDURE update_carrinhos(id_carrinho_in INT, _new_preco_total DECIMAL(10, 2), _new_data_compra TIMESTAMP)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE carrinhos
    SET preco_total = _new_preco_total, data_compra = _new_data_compra
    WHERE id_carrinho = id_carrinho_in;
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

CREATE OR REPLACE PROCEDURE create_ingredientes(_new_id_fornecedor INT, _new_nome VARCHAR(255), _new_url_imagem VARCHAR(2048), _new_quantidade_stock INT, _new_unidade_medida VARCHAR(50), _new_limite_stock INT, _new_preco DECIMAL(10, 2))
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO ingredientes (id_fornecedor, nome, url_imagem, quantidade_stock, unidade_medida, limite_stock, preco)
    VALUES (_new_id_fornecedor, _new_nome, _new_url_imagem, _new_quantidade_stock, _new_unidade_medida, _new_limite_stock, _new_preco);
END;
$$;

CREATE OR REPLACE PROCEDURE update_ingredientes(id_ingrediente_in INT, _new_id_fornecedor INT, _new_nome VARCHAR(255), _new_url_imagem VARCHAR(2048), _new_quantidade_stock INT, _new_unidade_medida VARCHAR(50), _new_limite_stock INT, _new_preco DECIMAL(10, 2))
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE ingredientes
    SET id_fornecedor = _new_id_fornecedor, nome = _new_nome, url_imagem = _new_url_imagem, quantidade_stock = _new_quantidade_stock, unidade_medida = _new_unidade_medida, limite_stock = _new_limite_stock, preco = _new_preco
    WHERE id_ingrediente = id_ingrediente_in;
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

CREATE OR REPLACE PROCEDURE create_ingredientescarrinhos(_new_id_ingrediente INT, _new_id_administrador INT, _new_id_carrinho INT, _new_quantidade INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO ingredientescarrinhos (id_ingrediente, id_administrador, id_carrinho, quantidade)
    VALUES (_new_id_ingrediente, _new_id_administrador, _new_id_carrinho, _new_quantidade);
END;
$$;

CREATE OR REPLACE PROCEDURE update_ingredientescarrinhos(id_ingrediente_carrinho_in INT, _new_id_ingrediente INT, _new_id_administrador INT, _new_id_carrinho INT, _new_quantidade INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE ingredientescarrinhos
    SET id_ingrediente = _new_id_ingrediente, id_administrador = _new_id_administrador, id_carrinho = _new_id_carrinho, quantidade = _new_quantidade
    WHERE id_ingrediente_carrinho = id_ingrediente_carrinho_in;
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

CREATE OR REPLACE PROCEDURE create_utensilios(_new_id_fornecedor INT, _new_nome VARCHAR(100), _new_url_imagem VARCHAR(2048), _new_quantidade_stock INT, _new_limite_stock INT, _new_preco DECIMAL(10, 2))
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO utensilios (id_fornecedor, nome, url_imagem, quantidade_stock, limite_stock, preco)
    VALUES (_new_id_fornecedor, _new_nome, _new_url_imagem, _new_quantidade_stock, _new_limite_stock, _new_preco);
END;
$$;

CREATE OR REPLACE PROCEDURE update_utensilios(id_utensilio_in INT, _new_id_fornecedor INT, _new_nome VARCHAR(100), _new_url_imagem VARCHAR(2048), _new_quantidade_stock INT, _new_limite_stock INT, _new_preco DECIMAL(10, 2))
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE utensilios
    SET id_fornecedor = _new_id_fornecedor, nome = _new_nome, url_imagem = _new_url_imagem, quantidade_stock = _new_quantidade_stock, limite_stock = _new_limite_stock, preco = _new_preco
    WHERE id_utensilio = id_utensilio_in;
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

CREATE OR REPLACE PROCEDURE create_utensilioscarrinhos(_new_id_utensilio INT, _new_id_administrador INT, _new_id_carrinho INT, _new_quantidade INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO utensilioscarrinhos (id_utensilio, id_administrador, id_carrinho, quantidade)
    VALUES (_new_id_utensilio, _new_id_administrador, _new_id_carrinho, _new_quantidade);
END;
$$;

CREATE OR REPLACE PROCEDURE update_utensilioscarrinhos(id_utensilio_carrinho_in INT, _new_id_utensilio INT, _new_id_administrador INT, _new_id_carrinho INT, _new_quantidade INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE utensilioscarrinhos
    SET id_utensilio = _new_id_utensilio, id_administrador = _new_id_administrador, id_carrinho = _new_id_carrinho, quantidade = _new_quantidade
    WHERE id_utensilio_carrinho = id_utensilio_carrinho_in;
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

CREATE OR REPLACE PROCEDURE create_receitas(_new_nome VARCHAR(100), _new_duracao INTERVAL)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO receitas (nome, duracao)
    VALUES (_new_nome, _new_duracao);
END;
$$;

CREATE OR REPLACE PROCEDURE update_receitas(id_receita_in INT, _new_nome VARCHAR(100), _new_duracao INTERVAL)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE receitas
    SET nome = _new_nome, duracao = _new_duracao
    WHERE id_receita = id_receita_in;
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

CREATE OR REPLACE PROCEDURE create_ingredientesreceitas(_new_id_ingrediente INT, _new_id_receita INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO ingredientesreceitas (id_ingrediente, id_receita)
    VALUES (_new_id_ingrediente, _new_id_receita);
END;
$$;

CREATE OR REPLACE PROCEDURE update_ingredientesreceitas(id_ingrediente_receita_in INT, _new_id_ingrediente INT, _new_id_receita INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE ingredientesreceitas
    SET id_ingrediente = _new_id_ingrediente, id_receita = _new_id_receita
    WHERE id_ingrediente_receita = id_ingrediente_receita_in;
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

CREATE OR REPLACE PROCEDURE create_utensiliosreceitas(_new_id_utensilio INT, _new_id_receita INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO utensiliosreceitas (id_utensilio, id_receita)
    VALUES (_new_id_utensilio, _new_id_receita);
END;
$$;

CREATE OR REPLACE PROCEDURE update_utensiliosreceitas(id_utensilio_receita_in INT, _new_id_utensilio INT, _new_id_receita INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE utensiliosreceitas
    SET id_utensilio = _new_id_utensilio, id_receita = _new_id_receita
    WHERE id_utensilio_receita = id_utensilio_receita_in;
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

CREATE OR REPLACE PROCEDURE create_instrucoes(_new_id_receita INT, _new_numero_sequencia INT, _new_descricao TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO instrucoes (id_receita, numero_sequencia, descricao)
    VALUES (_new_id_receita, _new_numero_sequencia, _new_descricao);
END;
$$;

CREATE OR REPLACE PROCEDURE update_instrucoes(id_instrucao_in INT, _new_id_receita INT, _new_numero_sequencia INT, _new_descricao TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE instrucoes
    SET id_receita = _new_id_receita, numero_sequencia = _new_numero_sequencia, descricao = _new_descricao
    WHERE id_instrucao = id_instrucao_in;
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

CREATE OR REPLACE PROCEDURE create_instrucoesingredientes(_new_id_instrucao INT, _new_id_ingrediente INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO instrucoesingredientes (id_instrucao, id_ingrediente)
    VALUES (_new_id_instrucao, _new_id_ingrediente);
END;
$$;

CREATE OR REPLACE PROCEDURE update_instrucoesingredientes(id_instrucao_ingrediente_in INT, _new_id_instrucao INT, _new_id_ingrediente INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE instrucoesingredientes
    SET id_instrucao = _new_id_instrucao, id_ingrediente = _new_id_ingrediente
    WHERE id_instrucao_ingrediente = id_instrucao_ingrediente_in;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_instrucoesingredientes(id_instrucao_ingrediente_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM instrucoesingredientes
    WHERE id_instrucao_ingrediente = id_instrucao_ingrediente_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_instrucoesutensilios(_new_id_instrucao INT, _new_id_utensilio INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO instrucoesutensilios (id_instrucao,  id_utensilio)
    VALUES (_new_id_instrucao, _new_id_utensilio);
END;
$$;

CREATE OR REPLACE PROCEDURE update_instrucoesutensilios(id_instrucao_utensilio_in INT, _new_id_instrucao INT, _new_id_utensilio INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE instrucoesutensilios
    SET id_instrucao = _new_id_instrucao, id_utensilio = _new_id_utensilio
    WHERE id_instrucao_utensilio = id_instrucao_utensilio_in;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_instrucoesutensilios(id_instrucao_utensilio_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM instrucoesutensilios
    WHERE id_instrucao_utensilio = id_instrucao_utensilio_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_mesas(_new_id_estado_mesa INT, _new_numero INT, _new_capacidade_maxima INT, _new_quantidade_clientes INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO mesas (id_estado_mesa, numero, capacidade_maxima, quantidade_clientes)
    VALUES (_new_id_estado_mesa, _new_numero, _new_capacidade_maxima, _new_quantidade_clientes);
END;
$$;

CREATE OR REPLACE PROCEDURE update_mesas(id_mesa_in INT, _new_id_estado_mesa INT, _new_numero INT, _new_capacidade_maxima INT, _new_quantidade_clientes INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE mesas
    SET id_estado_mesa = _new_id_estado_mesa, numero = _new_numero, capacidade_maxima = _new_capacidade_maxima, quantidade_clientes = _new_quantidade_clientes
    WHERE id_mesa = id_mesa_in;
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

CREATE OR REPLACE PROCEDURE create_produtos(_new_item BOOLEAN, _new_menu BOOLEAN, _new_nome VARCHAR(100), _new_url_imagem VARCHAR(2048), _new_preco DECIMAL(10, 2))
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO produtos (item, menu, nome, url_imagem, preco)
    VALUES (_new_item, _new_menu, _new_nome, _new_url_imagem, _new_preco);
END;
$$;

CREATE OR REPLACE PROCEDURE update_produtos(id_produto_in INT, _new_item BOOLEAN, _new_menu BOOLEAN, _new_nome VARCHAR(100), _new_url_imagem VARCHAR(2048), _new_preco DECIMAL(10, 2))
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE produtos
    SET item = _new_item, menu = _new_menu, nome = _new_nome, url_imagem = _new_url_imagem, preco = _new_preco
    WHERE id_produto = id_produto_in;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_produtos(id_produto_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM produtos
    WHERE id_produto = id_produto_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_tipos(_new_designacao VARCHAR(100))
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO tipos (designacao)
    VALUES (_new_designacao);
END;
$$;

CREATE OR REPLACE PROCEDURE update_tipos(id_tipo_in INT, _new_designacao VARCHAR(100))
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE tipos
    SET designacao = _new_designacao
    WHERE id_tipo = id_tipo_in;
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

CREATE OR REPLACE PROCEDURE create_itens(_new_id_item INT, _new_porcao_unidade_medida VARCHAR(50), _new_porcao INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO itens (id_item, porcao_unidade_medida, porcao)
    VALUES (_new_id_item, _new_porcao_unidade_medida, _new_porcao);
END;
$$;

CREATE OR REPLACE PROCEDURE update_itens(id_item_in INT, _new_porcao_unidade_medida VARCHAR(50), _new_porcao INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE itens
    SET porcao_unidade_medida = _new_porcao_unidade_medida, porcao = _new_porcao
    WHERE id_item = id_item_in;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_itens(id_item_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM itens
    WHERE id_item = id_item_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_itenstipos(_new_id_item INT, _new_id_tipo INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO itenstipos (id_item, id_tipo)
    VALUES (_new_id_item, _new_id_tipo);
END;
$$;

CREATE OR REPLACE PROCEDURE update_itenstipos(id_item_tipo_in INT, _new_id_item INT, _new_id_tipo INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE itenstipos
    SET id_item = _new_id_item, id_tipo = _new_id_tipo
    WHERE id_item_tipo = id_item_tipo_in;
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

CREATE OR REPLACE PROCEDURE create_categorias(_new_designacao VARCHAR(100))
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO categorias (designacao)
    VALUES (_new_designacao);
END;
$$;

CREATE OR REPLACE PROCEDURE update_categorias(id_categoria_in INT, _new_designacao VARCHAR(100))
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE categorias
    SET designacao = _new_designacao
    WHERE id_categoria = id_categoria_in;
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

CREATE OR REPLACE PROCEDURE create_itenscategorias(_new_id_item INT, _new_id_categoria INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO itenscategorias (id_item, id_categoria)
    VALUES (_new_id_item, _new_id_categoria);
END;
$$;

CREATE OR REPLACE PROCEDURE update_itenscategorias(id_item_categoria_in INT, _new_id_item INT, _new_id_categoria INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE itenscategorias
    SET id_item = _new_id_item, id_categoria = _new_id_categoria
    WHERE id_item_categoria = id_item_categoria_in;
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

CREATE OR REPLACE PROCEDURE create_opcoes(_new_designacao VARCHAR(100))
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO opcoes (designacao)
    VALUES (_new_designacao);
END;
$$;

CREATE OR REPLACE PROCEDURE update_opcoes(id_opcao_in INT, _new_designacao VARCHAR(100))
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE opcoes
    SET designacao = _new_designacao
    WHERE id_opcao = id_opcao_in;
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

CREATE OR REPLACE PROCEDURE create_itensopcoes(_new_id_item INT, _new_id_opcao INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO itensopcoes (id_item, id_opcao)
    VALUES (_new_id_item, _new_id_opcao);
END;
$$;

CREATE OR REPLACE PROCEDURE update_itensopcoes(id_item_opcao_in INT, _new_id_item INT, _new_id_opcao INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE itensopcoes
    SET id_item = _new_id_item, id_opcao = _new_id_opcao
    WHERE id_item_opcao = id_item_opcao_in;
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

CREATE OR REPLACE PROCEDURE create_menus(_new_id_menu INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO menus (id_menu)
    VALUES (_new_id_menu);
END;
$$;

CREATE OR REPLACE PROCEDURE update_menus(id_menu_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    --UPDATE menus
    --SET created_at = _new_created_at, updated_at = _new_updated_at
    --WHERE id_menu = id_menu_in;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_menus(id_menu_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM menus
    WHERE id_menu = id_menu_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_itensmenus(_new_id_item INT, _new_id_menu INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO itensmenus (id_item, id_menu)
    VALUES (_new_id_item, _new_id_menu);
END;
$$;

CREATE OR REPLACE PROCEDURE update_itensmenus(id_item_menu_in INT, _new_id_item INT, _new_id_menu INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE itensmenus
    SET id_item = _new_id_item, id_menu = _new_id_menu
    WHERE id_item_menu = id_item_menu_in;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_itensmenus(id_item_menu_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM itensmenus
    WHERE id_item_menu = id_item_menu_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_diassemana(_new_designacao VARCHAR(50))
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO diassemana (designacao)
    VALUES (_new_designacao);
END;
$$;

CREATE OR REPLACE PROCEDURE update_diassemana(id_dia_semana_in INT, _new_designacao VARCHAR(50))
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE diassemana
    SET designacao = _new_designacao
    WHERE id_dia_semana = id_dia_semana_in;
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

CREATE OR REPLACE PROCEDURE create_menusdiassemana(_new_id_menu INT, _new_id_dia_semana INT, _new_almoco BOOLEAN, _new_jantar BOOLEAN)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO menusdiassemana (id_menu, id_dia_semana, almoco, jantar)
    VALUES (_new_id_menu, _new_id_dia_semana, _new_almoco, _new_jantar);
END;
$$;

CREATE OR REPLACE PROCEDURE update_menusdiassemana(id_menu_dia_semana_in INT, _new_id_menu INT, _new_id_dia_semana INT, _new_almoco BOOLEAN, _new_jantar BOOLEAN)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE menusdiassemana
    SET id_menu = _new_id_menu, id_dia_semana = _new_id_dia_semana, almoco = _new_almoco, jantar = _new_jantar
    WHERE id_menu_dia_semana = id_menu_dia_semana_in;
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

CREATE OR REPLACE PROCEDURE create_servicos(_new_id_garcom INT, _new_id_mesa INT, _new_data_hora_inicio TIMESTAMP, _new_data_hora_fim TIMESTAMP, _new_preco_total DECIMAL(10, 2))
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO servicos (id_garcom, id_mesa, data_hora_inicio, data_hora_fim, preco_total)
    VALUES (_new_id_garcom, _new_id_mesa, _new_data_hora_inicio, _new_data_hora_fim, _new_preco_total);
END;
$$;

CREATE OR REPLACE PROCEDURE update_servicos(id_servico_in INT, _new_id_garcom INT, _new_id_mesa INT, _new_data_hora_inicio TIMESTAMP, _new_data_hora_fim TIMESTAMP, _new_preco_total DECIMAL(10, 2))
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE servicos
    SET id_garcom = _new_id_garcom, id_mesa = _new_id_mesa, data_hora_inicio = _new_data_hora_inicio, data_hora_fim = _new_data_hora_fim, preco_total = _new_preco_total
    WHERE id_servico = id_servico_in;
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

CREATE OR REPLACE PROCEDURE create_pedidos(_new_id_servico INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO pedidos (id_servico)
    VALUES (_new_id_servico);
END;
$$;

CREATE OR REPLACE PROCEDURE update_pedidos(id_pedido_in INT, _new_id_servico INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE pedidos
    SET id_servico = _new_id_servico
    WHERE id_pedido = id_pedido_in;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_pedidos(id_pedido_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM pedidos
    WHERE id_pedido = id_pedido_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_pedidosprodutos(_new_id_pedido INT, _new_id_produto INT, _new_id_cozinheiro INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO pedidosprodutos (id_pedido, id_produto, id_cozinheiro)
    VALUES (_new_id_pedido, _new_id_produto, _new_id_cozinheiro);
END;
$$;

CREATE OR REPLACE PROCEDURE update_pedidosprodutos(id_pedido_produto_in INT, _new_id_pedido INT, _new_id_produto INT, _new_id_cozinheiro INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE pedidosprodutos
    SET id_pedido = _new_id_pedido, id_produto = _new_id_produto, id_cozinheiro = _new_id_cozinheiro
    WHERE id_pedido_produto = id_pedido_produto_in;
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

CREATE OR REPLACE PROCEDURE create_pedidosprodutositensopcoes(_new_id_item_opcao INT, _new_id_pedido_produto INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO pedidosprodutositensopcoes (id_item_opcao, id_pedido_produto)
    VALUES (_new_id_item_opcao, _new_id_pedido_produto);
END;
$$;

CREATE OR REPLACE PROCEDURE update_pedidosprodutositensopcoes(id_pedido_produto_item_opcao_in INT, _new_id_item_opcao INT, _new_id_pedido_produto INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE pedidosprodutositensopcoes
    SET id_item_opcao = _new_id_item_opcao, id_pedido_produto = _new_id_pedido_produto
    WHERE id_pedido_produto_item_opcao = id_pedido_produto_item_opcao_in;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_pedidosprodutositensopcoes(id_pedido_produto_item_opcao_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM pedidosprodutositensopcoes
    WHERE id_pedido_produto_item_opcao = id_pedido_produto_item_opcao_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_reservas(_new_id_mesa INT, _new_data_hora TIMESTAMP, _new_minutos_antes INT, _new_minutos_depois INT, _new_id_servico INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO reservas (id_mesa, data_hora, minutos_antes, minutos_depois, id_servico)
    VALUES (_new_id_mesa, _new_data_hora, _new_minutos_antes, _new_minutos_depois, _new_id_servico);
END;
$$;

CREATE OR REPLACE PROCEDURE update_reservas(id_reserva_in INT, _new_id_mesa INT, _new_data_hora TIMESTAMP, _new_minutos_antes INT, _new_minutos_depois INT, _new_id_servico INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE reservas
    SET id_mesa = _new_id_mesa, data_hora = _new_data_hora, minutos_antes = _new_minutos_antes, minutos_depois = _new_minutos_depois, id_servico = _new_id_servico
    WHERE id_reserva = id_reserva_in;
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