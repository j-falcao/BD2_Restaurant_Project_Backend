-- ADMINISTRADOR
REVOKE EXECUTE ON PROCEDURE create_pedidos FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_estadosmesas FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_estadosmesas FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_estadosmesas FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_mesas FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_mesas FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_mesas FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_servicos FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_servicos FROM administrador;
REVOKE EXECUTE ON PROCEDURE concluir_servicos FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_servico_com_reserva FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_servicos FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_pedidos FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_pedidos FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_pedidosprodutos FROM administrador;
REVOKE EXECUTE ON PROCEDURE confecionar_pedidosprodutos FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_pedidosprodutos FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_estadosreservas FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_estadosreservas FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_estadosreservas FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_reservas FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_reservas FROM administrador;
REVOKE EXECUTE ON PROCEDURE cancelar_reservas FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_reservas FROM administrador;

-- COZINHEIRO
REVOKE EXECUTE ON PROCEDURE confecionar_pedidosprodutos FROM cozinheiro;

-- GARCOM
REVOKE EXECUTE ON PROCEDURE create_reservas FROM garcom;
REVOKE EXECUTE ON PROCEDURE update_reservas FROM garcom;
REVOKE EXECUTE ON PROCEDURE delete_reservas FROM garcom;
REVOKE EXECUTE ON PROCEDURE create_servicos FROM garcom;
REVOKE EXECUTE ON PROCEDURE create_servico_com_reserva FROM garcom;
REVOKE EXECUTE ON PROCEDURE concluir_servicos FROM garcom;
REVOKE EXECUTE ON PROCEDURE update_servicos FROM garcom;
REVOKE EXECUTE ON PROCEDURE delete_servicos FROM garcom;
REVOKE EXECUTE ON PROCEDURE create_pedidos FROM garcom;
REVOKE EXECUTE ON PROCEDURE delete_pedidos FROM garcom;
REVOKE EXECUTE ON PROCEDURE create_pedidosprodutos FROM garcom;
REVOKE EXECUTE ON PROCEDURE delete_pedidosprodutos FROM garcom;