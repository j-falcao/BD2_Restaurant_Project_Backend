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
SELECT reservas.*, estadosreservas.designacao FROM reservas
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

CREATE OR REPLACE PROCEDURE get_reservas_by_mesa(_id_mesa_in INT, OUT resultado JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(reservas)) INTO resultado
    FROM reservas
    WHERE id_mesa = _id_mesa_in;
END;
$$;

CREATE OR REPLACE PROCEDURE get_reservas_by_garcom(_id_garcom_in INT, OUT resultado JSON)  
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(reservas)) INTO resultado
    FROM reservas
    WHERE id_garcom = _id_garcom_in;
END;
$$;

CREATE OR REPLACE PROCEDURE get_reservas_by_date(_data_inicio_in DATE, _data_fim_in DATE, OUT resultado JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(reservas)) INTO resultado
    FROM reservas
    WHERE data_reserva BETWEEN _data_inicio_in AND _data_fim_in;
END;
$$;

CREATE OR REPLACE VIEW servicos_view AS 
SELECT * FROM servicos;

CREATE OR REPLACE VIEW pedidos_view AS 
SELECT * FROM pedidos;

CREATE OR REPLACE VIEW pedidosprodutos_view AS 
SELECT * FROM pedidosprodutos;