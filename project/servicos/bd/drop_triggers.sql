-- SERVICOS
DROP TRIGGER IF EXISTS atualizar_preco_servico_trigger ON pedidosprodutos;
DROP TRIGGER IF EXISTS verificar_mesa_ocupada_trigger ON servicos;
DROP TRIGGER IF EXISTS atualizar_estado_mesa_ocupada_trigger ON servicos;
DROP TRIGGER IF EXISTS atualizar_estado_mesa_disponivel_trigger ON servicos;

-- PEDIDOS
DROP TRIGGER IF EXISTS verificar_servico_ativo_pedido_trigger ON pedidos;
DROP TRIGGER IF EXISTS verificar_servico_ativo_pedidoproduto_trigger ON pedidoprodutos;

-- RESERVAS
DROP TRIGGER IF EXISTS verificar_garcom_reserva_trigger ON reservas;

-- MESAS
DROP TRIGGER IF EXISTS verificar_capacidade_mesa_trigger ON mesas;
DROP TRIGGER IF EXISTS set_next_numero_mesa_trigger ON reservas;
