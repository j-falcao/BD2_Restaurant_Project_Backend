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

CREATE OR REPLACE PROCEDURE create_mesas(_new_capacidade_maxima INT, OUT _new_mesa JSON)
LANGUAGE plpgsql
AS $$
DECLARE _new_id_mesa INT;
BEGIN
    INSERT INTO mesas (capacidade_maxima)
    VALUES (_new_capacidade_maxima)
    RETURNING id_mesa INTO _new_id_mesa;

    SELECT row_to_json(m)
    INTO _new_mesa
    FROM mesas_view m
    WHERE m.id_mesa = _new_id_mesa;
END;
$$;

CREATE OR REPLACE PROCEDURE update_mesas(id_mesa_in INT, _new_capacidade_maxima INT, OUT _new_mesa JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE mesas
    SET capacidade_maxima = _new_capacidade_maxima
    WHERE id_mesa = id_mesa_in;

    SELECT row_to_json(m)
    INTO _new_mesa
    FROM mesas_view m
    WHERE m.id_mesa = id_mesa_in;
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

CREATE OR REPLACE PROCEDURE create_servicos(_new_id_garcom INT, _new_id_mesa INT, OUT _new_servico JSON)
LANGUAGE plpgsql
AS $$
DECLARE _new_id_servico INT;
BEGIN
    INSERT INTO servicos (id_garcom, id_mesa)
    VALUES (_new_id_garcom, _new_id_mesa)
    RETURNING id_servico INTO _new_id_servico;

    SELECT row_to_json(s)
    INTO _new_servico
    FROM servicos_view s
    WHERE s.id_servico = _new_id_servico;
END;
$$;

CREATE OR REPLACE PROCEDURE update_servicos(id_servico_in INT, _new_id_garcom INT, _new_id_mesa INT, OUT _new_servico JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE servicos
    SET id_garcom = _new_id_garcom, id_mesa = _new_id_mesa
    WHERE id_servico = id_servico_in;

    SELECT row_to_json(s)
    INTO _new_servico
    FROM servicos_view s
    WHERE s.id_servico = id_servico_in;
END;
$$;

CREATE OR REPLACE PROCEDURE concluir_servicos(id_servico_in INT, OUT _new_servico JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE servicos
    SET data_hora_fim = CURRENT_TIMESTAMP
    WHERE id_servico = id_servico_in;

    SELECT row_to_json(s)
    INTO _new_servico
    FROM servicos_view s
    WHERE s.id_servico = id_servico_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_servico_com_reserva(_new_id_reserva INT, OUT _new_servico JSON)
LANGUAGE plpgsql
AS $$
DECLARE 
    _new_id_garcom INT; 
    _new_id_mesa INT;
    _new_id_servico INT;
    _estado_reserva TEXT;
BEGIN
    -- Obter estado da reserva
    SELECT designacao INTO _estado_reserva 
    FROM reservas
    JOIN estadosreservas ON reservas.id_estado_reserva = estadosreservas.id_estado_reserva
    WHERE id_reserva = _new_id_reserva;

    -- Validar estado da reserva
    IF _estado_reserva = 'Cancelada' THEN
        RAISE EXCEPTION 'Não é possibile criar serviços para uma reserva que tenha sido cancelada';
    ELSIF _estado_reserva = 'Concluida' THEN
        RAISE EXCEPTION 'Não é possibile criar serviços para uma reserva que já esteja concluida';
    END IF;

    -- Obter dados da reserva
    SELECT id_garcom, id_mesa 
    INTO _new_id_garcom, _new_id_mesa 
    FROM reservas 
    WHERE id_reserva = _new_id_reserva;

    -- Criar servico com os dados da reserva
    INSERT INTO servicos (id_garcom, id_mesa)
    VALUES (_new_id_garcom, _new_id_mesa)
    RETURNING id_servico INTO _new_id_servico;

    -- Atualizar o estado da reserva para 'Concluida'
    UPDATE reservas
    SET id_servico = _new_id_servico, 
        id_estado_reserva = (
            SELECT id_estado_reserva 
            FROM estadosreservas 
            WHERE designacao = 'Concluida'
        )
    WHERE id_reserva = _new_id_reserva;

    -- Retornar o servico criado
    SELECT row_to_json(s)
    INTO _new_servico
    FROM servicos_view s
    WHERE s.id_servico = _new_id_servico;
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

CREATE OR REPLACE PROCEDURE delete_pedidos(id_pedido_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM pedidos
    WHERE id_pedido = id_pedido_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_pedidosprodutos(_new_id_pedido INT, _new_quantidade INT, _new_id_produto INT, OUT _new_pedido_produto JSON)
LANGUAGE plpgsql
AS $$
DECLARE _new_id_pedido_produto INT;
BEGIN
    INSERT INTO pedidosprodutos (id_pedido, id_produto, quantidade)
    VALUES (_new_id_pedido, _new_id_produto, _new_quantidade)
    RETURNING id_pedido_produto INTO _new_id_pedido_produto;

    SELECT row_to_json(pp)
    INTO _new_pedido_produto
    FROM pedidosprodutos_view pp
    WHERE pp.id_pedido_produto = _new_id_pedido_produto;
END;
$$;

CREATE OR REPLACE PROCEDURE escolher_pedidosprodutos(id_pedido_produto_in INT, _new_id_cozinheiro INT, OUT _new_pedido_produto JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE pedidosprodutos
    SET id_cozinheiro = _new_id_cozinheiro, id_estado_pedido_produto = (
        SELECT id_estado_pedido_produto
        FROM estadospedidosprodutos
        WHERE designacao = 'Preparando'
    )
    WHERE id_pedido_produto = id_pedido_produto_in;

    SELECT row_to_json(pp)
    INTO _new_pedido_produto
    FROM pedidosprodutos_view pp
    WHERE pp.id_pedido_produto = id_pedido_produto_in;
END;
$$;

CREATE OR REPLACE PROCEDURE confecionar_pedidosprodutos(id_pedido_produto_in INT, OUT _new_pedido_produto JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE pedidosprodutos
    SET id_estado_pedido_produto = (
        SELECT id_estado_pedido_produto
        FROM estadospedidosprodutos
        WHERE designacao = 'Pronto'
    )
    WHERE id_pedido_produto = id_pedido_produto_in;

    SELECT row_to_json(pp)
    INTO _new_pedido_produto
    FROM pedidosprodutos_view pp
    WHERE pp.id_pedido_produto = id_pedido_produto_in;
END;
$$;

CREATE OR REPLACE PROCEDURE update_pedidosprodutos(id_pedido_produto_in INT, _new_quantidade INT, OUT _new_pedido_produto JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE pedidosprodutos
    SET quantidade = _new_quantidade
    WHERE id_pedido_produto = id_pedido_produto_in;

    SELECT row_to_json(pp)
    INTO _new_pedido_produto    
    FROM pedidosprodutos_view pp
    WHERE pp.id_pedido_produto = id_pedido_produto_in;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_pedidosprodutos(id_pedido_produto_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM pedidosprodutos
    WHERE id_pedido_produto = id_pedido_produto_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_estadosreservas(_new_designacao VARCHAR(100), OUT _new_estado_reserva JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO estadosreservas (designacao)
    VALUES (_new_designacao)
    RETURNING row_to_json(estadosreservas) INTO _new_estado_reserva;
END;
$$;

CREATE OR REPLACE PROCEDURE update_estadosreservas(id_estado_reserva_in INT, _new_designacao VARCHAR(100), OUT _new_estado_reserva JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE estadosreservas
    SET designacao = _new_designacao
    WHERE id_estado_reserva = id_estado_reserva_in
    RETURNING row_to_json(estadosreservas) INTO _new_estado_reserva;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_estadosreservas(id_estado_reserva_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM estadosreservas
    WHERE id_estado_reserva = id_estado_reserva_in;
END;
$$;

CREATE OR REPLACE PROCEDURE create_reservas(_new_id_mesa INT, _new_quantidade_pessoas INT, _new_observacoes TEXT, _new_id_garcom INT, _new_data_hora TIMESTAMP, OUT _new_reserva JSON)
LANGUAGE plpgsql
AS $$
DECLARE _new_id_reserva INT;
BEGIN
    INSERT INTO reservas (id_mesa, quantidade_pessoas, id_garcom, observacoes, data_hora)
    VALUES (_new_id_mesa, _new_quantidade_pessoas, _new_id_garcom, _new_observacoes, _new_data_hora)
    RETURNING id_reserva INTO _new_id_reserva;
    
    SELECT row_to_json(r)
    INTO _new_reserva
    FROM reservas_view r
    WHERE r.id_reserva = _new_id_reserva;
END;
$$;

CREATE OR REPLACE PROCEDURE update_reservas(id_reserva_in INT, _new_id_mesa INT, _new_id_estado_reserva INT, _new_quantidade_pessoas INT, _new_observacoes TEXT, _new_id_garcom INT, _new_data_hora TIMESTAMP, OUT _new_reserva JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE reservas
    SET id_mesa = _new_id_mesa, id_estado_reserva = _new_id_estado_reserva, quantidade_pessoas = _new_quantidade_pessoas, observacoes = _new_observacoes, id_garcom = _new_id_garcom, data_hora = _new_data_hora
    WHERE id_reserva = id_reserva_in;

    SELECT row_to_json(r)
    INTO _new_reserva
    FROM reservas_view r
    WHERE r.id_reserva = id_reserva_in;
END;
$$;


CREATE OR REPLACE PROCEDURE cancelar_reservas(id_reserva_in INT, OUT _new_reserva JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Verificar estado da reserva
    IF EXISTS (
        SELECT 1
        FROM reservas
        WHERE id_reserva = id_reserva_in
        AND id_estado_reserva = (
            SELECT id_estado_reserva
            FROM estadosreservas
            WHERE designacao = 'Concluida'
        )   
    )
    THEN
        RAISE EXCEPTION 'Não é possivel cancelar uma reserva que já foi concluida';
    END IF;


    UPDATE reservas
    SET id_estado_reserva = (
        SELECT id_estado_reserva
        FROM estadosreservas
        WHERE designacao = 'Cancelada'
    )
    WHERE id_reserva = id_reserva_in;

    SELECT row_to_json(r)
    INTO _new_reserva
    FROM reservas_view r
    WHERE r.id_reserva = id_reserva_in;
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