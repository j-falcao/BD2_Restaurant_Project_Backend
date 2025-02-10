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
    estadosreservas.designacao, 
    utilizadores.id AS id_garcom_reserva,  
    utilizadores.first_name || ' ' || utilizadores.last_name AS nome_garcom_reserva, 
    utilizadores.url_imagem AS url_imagem_garcom_reserva 
FROM reservas
JOIN estadosreservas ON reservas.id_estado_reserva = estadosreservas.id_estado_reserva
JOIN utilizadores ON reservas.id_garcom = utilizadores.id;

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
    WHERE data_reserva BETWEEN _data_inicio_in AND _data_fim_in;
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
    utilizadores.id AS id_cozinheiro_pedidoproduto, 
    utilizadores.first_name || ' ' || utilizadores.last_name AS nome_cozinheiro_pedidoproduto, 
    utilizadores.url_imagem AS url_imagem_cozinheiro_pedidoproduto
FROM pedidosprodutos
JOIN estadospedidosprodutos ON pedidosprodutos.id_estado_pedido_produto = estadospedidosprodutos.id_estado_pedido_produto
FULL OUTER JOIN utilizadores ON pedidosprodutos.id_cozinheiro = utilizadores.id;

CREATE OR REPLACE VIEW servicos_view AS
SELECT 
    servicos.*, 
    utilizadores.id AS id_garcom_servico,
    utilizadores.first_name || ' ' || utilizadores.last_name AS nome_garcom_servico, 
    utilizadores.url_imagem AS url_imagem_garcom_servico,
    mesas.numero AS mesa_numero
FROM servicos
JOIN utilizadores ON servicos.id_garcom = utilizadores.id
JOIN mesas ON servicos.id_mesa = mesas.id_mesa;

CREATE OR REPLACE FUNCTION get_servicos_com_pedidos(_id_servico_in INT)
RETURNS JSONB
LANGUAGE plpgsql
AS $$
DECLARE
    servico_json JSONB;
BEGIN
    WITH pedidos_data AS (
        SELECT 
            p.id_pedido,
            COALESCE(jsonb_agg(
                jsonb_build_object(
                    'id_pedido_produto', pp.id_pedido_produto,
                    'id_produto', pp.id_produto,
                    'quantidade', pp.quantidade,
                    'estado', pp.estado,
                    'nome_cozinheiro_pedidoproduto', pp.nome_cozinheiro_pedidoproduto,
                    'url_imagem_cozinheiro_pedidoproduto', pp.url_imagem_cozinheiro_pedidoproduto
                )
            ) FILTER (WHERE pp.id_pedido_produto IS NOT NULL), '[]'::jsonb) AS pedidosprodutos
        FROM pedidos p
        LEFT JOIN pedidosprodutos_view pp ON p.id_pedido = pp.id_pedido
        WHERE p.id_servico = _id_servico_in
        GROUP BY p.id_pedido
    ),
    servico_data AS (
        SELECT 
            s.id_servico,
            s.id_garcom,
            u.first_name || ' ' || u.last_name AS nome_garcom_servico,
            u.url_imagem AS url_imagem_garcom_servico,
            s.id_mesa,
            m.numero AS mesa_numero,
            s.created_at AS servico_created_at,
            COALESCE(jsonb_agg(
                jsonb_build_object(
                    'id_pedido', pd.id_pedido,
                    'pedidosprodutos', pd.pedidosprodutos
                )
            ) FILTER (WHERE pd.id_pedido IS NOT NULL), '[]'::jsonb) AS pedidos
        FROM servicos s
        JOIN utilizadores u ON s.id_garcom = u.id
        JOIN mesas m ON s.id_mesa = m.id_mesa
        LEFT JOIN pedidos_data pd ON s.id_servico = _id_servico_in
        WHERE s.id_servico = _id_servico_in
        GROUP BY s.id_servico, u.first_name, u.last_name, u.url_imagem, m.numero, s.created_at
    )
    SELECT jsonb_build_object(
        'id_servico', sd.id_servico,
        'id_garcom', sd.id_garcom,
        'nome_garcom_servico', sd.nome_garcom_servico,
        'url_imagem_garcom_servico', sd.url_imagem_garcom_servico,
        'id_mesa', sd.id_mesa,
        'mesa_numero', sd.mesa_numero,
        'servico_created_at', sd.servico_created_at,
        'pedidos', sd.pedidos
    ) INTO servico_json
    FROM servico_data sd;

    RETURN servico_json;
END;
$$;




CREATE OR REPLACE PROCEDURE get_servicos_by_data(_data_inicio_in DATE, _data_fim_in DATE, OUT resultado JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(servicos)) INTO resultado
    FROM servicos_view
    WHERE created_at BETWEEN _data_inicio_in AND _data_fim_in;
END;
$$;