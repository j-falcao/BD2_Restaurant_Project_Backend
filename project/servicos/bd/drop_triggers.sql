-- SERVICOS
DROP FUNCTION IF EXISTS atualizar_preco_servico() CASCADE;
DROP FUNCTION IF EXISTS verificar_mesa_ocupada() CASCADE;
DROP FUNCTION IF EXISTS atualizar_estado_mesa_ocupada() CASCADE;
DROP FUNCTION IF EXISTS atualizar_estado_mesa_disponivel() CASCADE;

-- PEDIDOS
DROP FUNCTION IF EXISTS verificar_servico_ativo_pedido() CASCADE;
DROP FUNCTION IF EXISTS verificar_servico_ativo_pedidoproduto() CASCADE;

-- RESERVAS
DROP FUNCTION IF EXISTS set_estado_reserva_pendente() CASCADE;
DROP FUNCTION IF EXISTS verificar_garcom_reserva() CASCADE;

-- MESAS
DROP FUNCTION IF EXISTS set_estado_mesa_disponivel() CASCADE;
DROP FUNCTION IF EXISTS verificar_capacidade_mesa() CASCADE;
DROP FUNCTION IF EXISTS set_next_numero_mesa() CASCADE;
