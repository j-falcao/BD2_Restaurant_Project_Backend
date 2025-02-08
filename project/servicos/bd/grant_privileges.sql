-- ADMINISTRADOR
GRANT SELECT ON
    estadosmesas_view,
    mesas_view,
    mesas_disponiveis_view,
    mesas_ocupadas_view,
    mesas_reservadas_view,
    estadosreservas_view,
    reservas_view,
    servicos_view,
    pedidos_view,
    pedidosprodutos_view
TO administrador;

GRANT INSERT, UPDATE, DELETE ON
    mesas,
    reservas,
    servicos,
    pedidos,
    pedidosprodutos
TO administrador;

GRANT EXECUTE ON PROCEDURE create_pedidos TO administrador;
GRANT EXECUTE ON PROCEDURE create_estadosmesas TO administrador;
GRANT EXECUTE ON PROCEDURE update_estadosmesas TO administrador;
GRANT EXECUTE ON PROCEDURE delete_estadosmesas TO administrador;
GRANT EXECUTE ON PROCEDURE create_mesas TO administrador;
GRANT EXECUTE ON PROCEDURE update_mesas TO administrador;
GRANT EXECUTE ON PROCEDURE delete_mesas TO administrador;
GRANT EXECUTE ON PROCEDURE create_servicos TO administrador;
GRANT EXECUTE ON PROCEDURE update_servicos TO administrador;
GRANT EXECUTE ON PROCEDURE concluir_servicos TO administrador;
GRANT EXECUTE ON PROCEDURE create_servico_com_reserva TO administrador;
GRANT EXECUTE ON PROCEDURE delete_servicos TO administrador;
GRANT EXECUTE ON PROCEDURE create_pedidos TO administrador;
GRANT EXECUTE ON PROCEDURE delete_pedidos TO administrador;
GRANT EXECUTE ON PROCEDURE create_pedidosprodutos TO administrador;
GRANT EXECUTE ON PROCEDURE confecionar_pedidosprodutos TO administrador;
GRANT EXECUTE ON PROCEDURE delete_pedidosprodutos TO administrador;
GRANT EXECUTE ON PROCEDURE create_estadosreservas TO administrador;
GRANT EXECUTE ON PROCEDURE update_estadosreservas TO administrador;
GRANT EXECUTE ON PROCEDURE delete_estadosreservas TO administrador;
GRANT EXECUTE ON PROCEDURE create_reservas TO administrador;
GRANT EXECUTE ON PROCEDURE update_reservas TO administrador;
GRANT EXECUTE ON PROCEDURE cancelar_reservas TO administrador;
GRANT EXECUTE ON PROCEDURE delete_reservas TO administrador;


-- COZINHEIRO
GRANT SELECT ON
    pedidos_view,
    pedidosprodutos_view
TO cozinheiro;

GRANT UPDATE ON
    pedidosprodutos
TO cozinheiro;

GRANT EXECUTE ON PROCEDURE confecionar_pedidosprodutos TO cozinheiro;

-- GARCOM
GRANT SELECT ON
    estadosmesas_view,
    mesas_view,
    mesas_disponiveis_view,
    mesas_ocupadas_view,
    mesas_reservadas_view,
    estadosreservas_view,
    reservas_view,
    servicos_view,
    pedidos_view,
    pedidosprodutos_view
TO garcom;

GRANT INSERT, DELETE ON
    reservas,
    servicos,
    pedidos,
    pedidosprodutos
TO garcom;

GRANT UPDATE ON
    reservas,
    servicos
TO garcom;

GRANT EXECUTE ON PROCEDURE create_reservas TO garcom;
GRANT EXECUTE ON PROCEDURE update_reservas TO garcom;
GRANT EXECUTE ON PROCEDURE delete_reservas TO garcom;
GRANT EXECUTE ON PROCEDURE create_servicos TO garcom;
GRANT EXECUTE ON PROCEDURE create_servico_com_reserva TO garcom;
GRANT EXECUTE ON PROCEDURE concluir_servicos TO garcom;
GRANT EXECUTE ON PROCEDURE update_servicos TO garcom;
GRANT EXECUTE ON PROCEDURE delete_servicos TO garcom;
GRANT EXECUTE ON PROCEDURE create_pedidos TO garcom;
GRANT EXECUTE ON PROCEDURE delete_pedidos TO garcom;
GRANT EXECUTE ON PROCEDURE create_pedidosprodutos TO garcom;
GRANT EXECUTE ON PROCEDURE delete_pedidosprodutos TO garcom;