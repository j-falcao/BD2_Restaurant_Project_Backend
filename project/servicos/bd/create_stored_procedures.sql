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