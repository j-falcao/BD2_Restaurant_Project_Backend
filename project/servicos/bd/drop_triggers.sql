-- SERVICOS
DROP FUNCTION IF EXISTS atualizar_preco_servico() CASCADE;
DROP FUNCTION IF EXISTS verificar_estadomesa_ocupada() CASCADE;
DROP FUNCTION IF EXISTS atualizar_estadomesa_ocupada() CASCADE;
DROP FUNCTION IF EXISTS atualizar_estadomesa_disponivel() CASCADE;
DROP FUNCTION IF EXISTS atualizar_estadoreserva_estadomesa() CASCADE;

-- PEDIDOS
DROP FUNCTION IF EXISTS verificar_servico_ativo_pedido() CASCADE;
DROP FUNCTION IF EXISTS verificar_servico_ativo_pedidoproduto() CASCADE;
DROP FUNCTION IF EXISTS verificar_stock_pedido() CASCADE;
DROP FUNCTION IF EXISTS reduzir_stock_apos_preparacao() CASCADE;

-- RESERVAS
DROP FUNCTION IF EXISTS atualizar_estadomesa_reservada() CASCADE;
DROP FUNCTION IF EXISTS auto_set_estadoreserva_pendente() CASCADE;
DROP FUNCTION IF EXISTS verificar_utilizador_reserva() CASCADE;
DROP FUNCTION IF EXISTS verificar_capacidade_mesa() CASCADE;

-- MESAS
DROP FUNCTION IF EXISTS auto_set_estadomesa_disponivel() CASCADE;
DROP FUNCTION IF EXISTS auto_set_numero_mesa() CASCADE;