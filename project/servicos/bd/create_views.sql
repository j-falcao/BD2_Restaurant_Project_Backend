CREATE OR REPLACE VIEW estadosmesas_view AS 
SELECT * FROM estadosmesas;

CREATE OR REPLACE VIEW mesas_view AS 
SELECT mesas.*, estadosmesas.designacao FROM mesas
JOIN estadosmesas ON mesas.id_estado_mesa = estadosmesas.id_estado_mesa;

CREATE OR REPLACE VIEW mesas_disponiveis_view AS 
SELECT mesas.*, estadosmesas.designacao FROM mesas
JOIN estadosmesas ON mesas.id_estado_mesa = estadosmesas.id_estado_mesa
WHERE designacao = 'Disponivel';

CREATE OR REPLACE VIEW mesas_ocupadas_view AS 
SELECT mesas.*, estadosmesas.designacao FROM mesas
JOIN estadosmesas ON mesas.id_estado_mesa = estadosmesas.id_estado_mesa
WHERE designacao = 'Ocupada';

CREATE OR REPLACE VIEW mesas_reservadas_view AS 
SELECT mesas.*, estadosmesas.designacao FROM mesas
JOIN estadosmesas ON mesas.id_estado_mesa = estadosmesas.id_estado_mesa
WHERE designacao = 'Reservada';


CREATE OR REPLACE VIEW estadosreservas_view AS 
SELECT * FROM estadosreservas;

CREATE OR REPLACE VIEW reservas_view AS 
SELECT 
    reservas.*, 
    estadosreservas.designacao AS estado
FROM reservas
JOIN estadosreservas ON reservas.id_estado_reserva = estadosreservas.id_estado_reserva;

CREATE OR REPLACE VIEW reservas_confirmadas_view AS 
SELECT reservas.*, estadosreservas.designacao FROM reservas
JOIN estadosreservas ON reservas.id_estado_reserva = estadosreservas.id_estado_reserva
WHERE designacao = 'Confirmada';

CREATE OR REPLACE VIEW reservas_canceladas_view AS 
SELECT reservas.*, estadosreservas.designacao FROM reservas
JOIN estadosreservas ON reservas.id_estado_reserva = estadosreservas.id_estado_reserva
WHERE designacao = 'Cancelada';

CREATE OR REPLACE VIEW reservas_concluidas_view AS 
SELECT reservas.*, estadosreservas.designacao FROM reservas
JOIN estadosreservas ON reservas.id_estado_reserva = estadosreservas.id_estado_reserva
WHERE designacao = 'Concluida';

CREATE OR REPLACE PROCEDURE get_reservas_by_data(_data_inicio_in DATE, _data_fim_in DATE, OUT resultado JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(reservas)) INTO resultado
    FROM reservas
    WHERE data_hora BETWEEN _data_inicio_in AND _data_fim_in;
END;
$$;

CREATE OR REPLACE VIEW pedidos_view AS
SELECT * FROM pedidos;

CREATE OR REPLACE VIEW estadospedidosprodutos_view AS
SELECT * FROM estadospedidosprodutos;

CREATE OR REPLACE VIEW pedidosprodutos_view AS
SELECT 
    pedidosprodutos.*,
    estadospedidosprodutos.designacao AS estado,
    produtos.nome AS nome_produto,
    produtos.url_imagem AS url_imagem_produto,
    produtos.preco,
    utilizadores.first_name || ' ' || utilizadores.last_name AS nome_cozinheiro,
    utilizadores.url_imagem as url_imagem_cozinheiro
FROM pedidosprodutos
JOIN estadospedidosprodutos ON estadospedidosprodutos.id_estado_pedido_produto = pedidosprodutos.id_estado_pedido_produto
JOIN produtos ON produtos.id_produto = pedidosprodutos.id_produto
LEFT JOIN utilizadores ON utilizadores.id = pedidosprodutos.id_cozinheiro;

CREATE OR REPLACE VIEW servicos_view AS
SELECT 
    servicos.*, 
    utilizadores.first_name || ' ' || utilizadores.last_name AS nome_garcom, 
    utilizadores.url_imagem as url_imagem_garcom,
    mesas.numero AS numero_mesa
FROM servicos
JOIN utilizadores ON servicos.id_garcom = utilizadores.id
JOIN mesas ON servicos.id_mesa = mesas.id_mesa;

CREATE OR REPLACE FUNCTION get_servicos_com_pedidos(_id_servico_in INT)
RETURNS JSON
LANGUAGE plpgsql
AS $$
DECLARE
    servico_json JSON;
BEGIN
    WITH pedidos_data AS (
        SELECT 
            p.id_pedido,
            COALESCE(array_agg(
                json_build_object(
                    'id_pedido_produto', pp.id_pedido_produto,
                    'id_produto', pp.id_produto,
                    'nome_produto', pp.nome_produto,
                    'url_imagem_produto', pp.url_imagem_produto,
                    'preco', pp.preco,
                    'quantidade', pp.quantidade,
                    'estado', pp.estado,
                    'nome_cozinheiro', pp.nome_cozinheiro,
                    'url_imagem_cozinheiro', pp.url_imagem_cozinheiro
                )
            ) FILTER (WHERE pp.id_pedido_produto IS NOT NULL), '{}') AS pedidosprodutos
        FROM pedidos p
        LEFT JOIN pedidosprodutos_view pp ON p.id_pedido = pp.id_pedido
        WHERE p.id_servico = _id_servico_in
        GROUP BY p.id_pedido
    ),
    servico_data AS (
        SELECT
            sv.id_servico,
            sv.id_garcom,
            sv.nome_garcom,
            sv.url_imagem_garcom,
            sv.id_mesa,
            sv.created_at AS servico_created_at,
            COALESCE(array_agg(
                json_build_object(
                    'id_pedido', pd.id_pedido,
                    'pedidosprodutos', pd.pedidosprodutos
                )
            ) FILTER (WHERE pd.id_pedido IS NOT NULL), '{}') AS pedidos
        FROM servicos_view sv
        LEFT JOIN pedidos_data pd ON sv.id_servico = _id_servico_in
        WHERE sv.id_servico = _id_servico_in
        GROUP BY sv.id_servico, sv.id_garcom, sv.nome_garcom, sv.url_imagem_garcom, sv.id_mesa, sv.created_at
    )
    SELECT row_to_json(sd) INTO servico_json
    FROM servico_data sd;

    RETURN servico_json;
END;
$$;


CREATE OR REPLACE PROCEDURE get_servicos_by_data(_data_inicio_in DATE, _data_fim_in DATE, OUT resultado JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(servicos_view)) INTO resultado
    FROM servicos_view
    WHERE created_at BETWEEN _data_inicio_in AND _data_fim_in;
END;
$$;