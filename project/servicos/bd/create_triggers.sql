-- SERVICOS
-- Atualizar o preco_total do servico ao adicionar ou remover um pedido
CREATE OR REPLACE FUNCTION atualizar_preco_servico() RETURNS TRIGGER AS $$
DECLARE 
    _id_pedido INT;
BEGIN
    -- Handle INSERT and DELETE by ensuring we always reference the correct row
    IF TG_OP = 'INSERT' THEN
        _id_pedido = NEW.id_pedido;
    ELSE
        _id_pedido = OLD.id_pedido;
    END IF;

    UPDATE servicos
    SET preco_total = (
        SELECT COALESCE(SUM(produtos.preco * pedidosprodutos.quantidade), 0) 
        FROM pedidosprodutos 
        JOIN produtos ON pedidosprodutos.id_produto = produtos.id_produto
        WHERE pedidosprodutos.id_pedido = _id_pedido
    )
    WHERE id_servico = (
        SELECT id_servico FROM pedidos WHERE id_pedido = _id_pedido
    );

    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER atualizar_preco_servico_trigger
AFTER INSERT OR DELETE ON pedidosprodutos
FOR EACH ROW EXECUTE FUNCTION atualizar_preco_servico();

-- Impedir a criação de serviços para mesas ocupadas
CREATE OR REPLACE FUNCTION verificar_estadomesa_ocupada() RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM mesas
        JOIN estadosmesas ON mesas.id_estado_mesa = estadosmesas.id_estado_mesa
        WHERE id_mesa = NEW.id_mesa AND designacao = 'Ocupada'
    ) THEN
        RAISE EXCEPTION 'Não é possível criar serviços para mesas ocupadas';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_estadomesa_ocupada_trigger
BEFORE INSERT ON servicos
FOR EACH ROW EXECUTE FUNCTION verificar_estadomesa_ocupada();

-- Atualizar o estado da mesa para 'Ocupada' após a criação de um serviço
CREATE OR REPLACE FUNCTION atualizar_estadomesa_ocupada() RETURNS TRIGGER AS $$
BEGIN
    UPDATE mesas 
    SET id_estado_mesa = (SELECT id_estado_mesa FROM estadosmesas WHERE designacao = 'Ocupada') 
    WHERE id_mesa = NEW.id_mesa;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER atualizar_estadomesa_ocupada_trigger
AFTER INSERT ON servicos
FOR EACH ROW EXECUTE FUNCTION atualizar_estadomesa_ocupada();

-- Atualizar o estado da mesa para 'Disponivel' quando o serviço é concluido
CREATE OR REPLACE FUNCTION atualizar_estadomesa_disponivel() RETURNS TRIGGER AS $$
BEGIN
    UPDATE mesas 
    SET id_estado_mesa = (SELECT id_estado_mesa FROM estadosmesas WHERE designacao = 'Disponivel')
    WHERE id_mesa = NEW.id_mesa;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER atualizar_estadomesa_disponivel_trigger
AFTER UPDATE OF data_hora_fim ON servicos
FOR EACH ROW WHEN (NEW.data_hora_fim IS NOT NULL)
EXECUTE FUNCTION atualizar_estadomesa_disponivel();

CREATE OR REPLACE FUNCTION atualizar_estadoreserva_estadomesa() RETURNS TRIGGER AS $$
BEGIN
    -- Se existir uma reserva para este servico, atualizar o estado da reserva para 'Confirmada' e atualizar o estado da mesa para 'Reservada'
    IF EXISTS (
        SELECT 1 FROM reservas WHERE id_servico = OLD.id_servico
    ) THEN
        -- Atualizar o estado da reserva para 'Confirmada'
        UPDATE reservas 
        SET id_estado_reserva = (SELECT id_estado_reserva FROM estadosreservas WHERE designacao = 'Confirmada') 
        WHERE id_servico = OLD.id_servico;

        -- Atualizar o estado da mesa para 'Reservada'
        UPDATE mesas 
        SET id_estado_mesa = (SELECT id_estado_mesa FROM estadosmesas WHERE designacao = 'Reservada') 
        WHERE id_mesa = (SELECT id_mesa FROM reservas WHERE id_servico = OLD.id_servico);

    -- Caso contrário, atualizar o estado da mesa para 'Disponivel'
    ELSE 
        UPDATE mesas 
        SET id_estado_mesa = (SELECT id_estado_mesa FROM estadosmesas WHERE designacao = 'Disponivel') 
        WHERE id_mesa = OLD.id_mesa;
    END IF;

    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER atualizar_estadoreserva_estadomesa_trigger
BEFORE DELETE ON servicos
FOR EACH ROW EXECUTE FUNCTION atualizar_estadoreserva_estadomesa();


-- PEDIDOS
-- Impedir a criação de pedidos para serviços inativos
CREATE OR REPLACE FUNCTION verificar_servico_ativo_pedido() RETURNS TRIGGER AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM servicos 
        WHERE id_servico = NEW.id_servico 
        AND created_at <= CURRENT_TIMESTAMP 
        AND (data_hora_fim IS NULL OR data_hora_fim >= CURRENT_TIMESTAMP )
    ) THEN
        RAISE EXCEPTION 'Não é possível criar pedido para um serviço inativo';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_servico_ativo_pedido_trigger
BEFORE INSERT OR UPDATE ON pedidos
FOR EACH ROW EXECUTE FUNCTION verificar_servico_ativo_pedido();

-- PEDIDO PRODUTOS
-- Impedir a criação de pedidosprodutos para serviços inativos
CREATE OR REPLACE FUNCTION verificar_servico_ativo_pedidoproduto() RETURNS TRIGGER AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM servicos 
        WHERE id_servico = (SELECT id_servico FROM pedidos WHERE id_pedido = NEW.id_pedido) 
        AND created_at <= CURRENT_TIMESTAMP  
        AND (data_hora_fim IS NULL OR data_hora_fim >= CURRENT_TIMESTAMP )
    ) THEN
        RAISE EXCEPTION 'Não é possível adicionar produtos a um pedido de serviço inativo';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_servico_ativo_pedidoproduto_trigger
BEFORE INSERT OR UPDATE ON pedidosprodutos
FOR EACH ROW EXECUTE FUNCTION verificar_servico_ativo_pedidoproduto();

-- Trigger para impedir a criacao de pedido_produtos se nao houver ingredientes ou utensilios suficientes
CREATE OR REPLACE FUNCTION verificar_stock_pedido()
RETURNS TRIGGER AS $$
BEGIN
    -- Verifica ingredientes
    IF EXISTS (
        SELECT 1
        FROM ingredientesreceitas ir
        JOIN receitas r ON ir.id_receita = r.id_receita
        JOIN produtos p ON p.id_produto = r.id_produto
        WHERE p.id_produto = NEW.id_produto
        AND ir.quantidade * NEW.quantidade > (SELECT quantidade_stock FROM ingredientes WHERE id_ingrediente = ir.id_ingrediente)
    ) THEN
        RAISE EXCEPTION 'Stock insuficiente para ingredientes do produto %', NEW.id_produto;
    END IF;
    
    -- Verifica utensilios
    IF EXISTS (
        SELECT 1
        FROM utensiliosreceitas ur
        JOIN receitas r ON ur.id_receita = r.id_receita
        JOIN produtos p ON p.id_produto = r.id_produto
        WHERE p.id_produto = NEW.id_produto
        AND ur.quantidade > (SELECT quantidade_stock FROM utensilios WHERE id_utensilio = ur.id_utensilio)
    ) THEN
        RAISE EXCEPTION 'Stock insuficiente para utensílios do produto %', NEW.id_produto;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_stock_pedido_trigger
BEFORE INSERT ON pedidosprodutos
FOR EACH ROW
EXECUTE FUNCTION verificar_stock_pedido();

-- Trigger para reduzir o stock quando um pedido_produto for preparado
CREATE OR REPLACE FUNCTION reduzir_stock_apos_preparacao()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.id_estado_pedido_produto = (SELECT id_estado_pedido_produto FROM estadospedidosprodutos WHERE designacao = 'Pronto') THEN
        -- Reduz o stock dos ingredientes
        UPDATE ingredientes
        SET quantidade_stock = quantidade_stock - (ir.quantidade * NEW.quantidade)
        FROM ingredientesreceitas ir, receitas r, produtos p
        WHERE p.id_produto = NEW.id_produto
        AND r.id_produto = p.id_produto
        AND ir.id_receita = r.id_receita
        AND ingredientes.id_ingrediente = ir.id_ingrediente;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER reduzir_stock_apos_preparacao_trigger
AFTER UPDATE OF id_estado_pedido_produto ON pedidosprodutos
FOR EACH ROW EXECUTE FUNCTION reduzir_stock_apos_preparacao();

CREATE OR REPLACE FUNCTION auto_set_estadopedidoproduto_pendente() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.id_cozinheiro IS NULL THEN
        SELECT id_estado_pedido_produto INTO NEW.id_estado_pedido_produto
        FROM estadospedidosprodutos 
        WHERE designacao = 'Pendente';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER auto_set_estadopedidoproduto_pendente_trigger
BEFORE INSERT ON pedidosprodutos
FOR EACH ROW EXECUTE FUNCTION auto_set_estadopedidoproduto_pendente();

CREATE OR REPLACE FUNCTION verificar_estadopedidoproduto() RETURNS TRIGGER AS $$
DECLARE
    _id_estado_pedido_produto_pendente INT;
    _id_estado_pedido_produto_preparando INT;
    _id_estado_pedido_produto_pronto INT;
BEGIN
    SELECT id_estado_pedido_produto INTO _id_estado_pedido_produto_pendente
    FROM estadospedidosprodutos 
    WHERE designacao = 'Pendente';
    
    SELECT id_estado_pedido_produto INTO _id_estado_pedido_produto_preparando
    FROM estadospedidosprodutos 
    WHERE designacao = 'Preparando';
    
    SELECT id_estado_pedido_produto INTO _id_estado_pedido_produto_pronto
    FROM estadospedidosprodutos 
    WHERE designacao = 'Pronto';

    IF NEW.id_estado_pedido_produto = _id_estado_pedido_produto_preparando
    AND OLD.id_estado_pedido_produto != _id_estado_pedido_produto_pendente
    THEN
        RAISE EXCEPTION 'O estado do pedido produto deve ser pendente';
    END IF;

    IF NEW.id_estado_pedido_produto = _id_estado_pedido_produto_pronto
    AND OLD.id_estado_pedido_produto != _id_estado_pedido_produto_preparando
    THEN
        RAISE EXCEPTION 'O estado do pedido produto deve ser preparando';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_estadopedidoproduto_trigger
BEFORE UPDATE OF id_estado_pedido_produto ON pedidosprodutos
FOR EACH ROW EXECUTE FUNCTION verificar_estadopedidoproduto();


-- RESERVAS
CREATE OR REPLACE FUNCTION atualizar_estadomesa_reservada() RETURNS TRIGGER AS $$
BEGIN
    UPDATE mesas 
    SET id_estado_mesa = (SELECT id_estado_mesa FROM estadosmesas WHERE designacao = 'Reservada') 
    WHERE id_mesa = NEW.id_mesa;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER atualizar_estadomesa_reservada_trigger
AFTER INSERT ON reservas
FOR EACH ROW EXECUTE FUNCTION atualizar_estadomesa_reservada();

CREATE OR REPLACE FUNCTION verificar_capacidade_mesa() RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT capacidade_maxima FROM mesas WHERE id_mesa = NEW.id_mesa) < NEW.quantidade_pessoas THEN
        RAISE EXCEPTION 'Capacidade máxima da mesa insuficiente para a reserva';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_capacidade_mesa_trigger
BEFORE INSERT OR UPDATE ON reservas
FOR EACH ROW EXECUTE FUNCTION verificar_capacidade_mesa();

CREATE OR REPLACE FUNCTION verificar_utilizador_reserva() RETURNS TRIGGER AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM utilizadores 
        WHERE id = NEW.id_garcom 
        AND id_cargo IN (SELECT id_cargo FROM cargos WHERE designacao = 'Garcom' OR designacao = 'Administrador')
    ) THEN
        RAISE EXCEPTION 'O utilizador não é nem um Garçom nem um Administrador, por isso nao pode criar uma reserva';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_utilizador_reserva_trigger
BEFORE INSERT OR UPDATE ON reservas
FOR EACH ROW EXECUTE FUNCTION verificar_utilizador_reserva();

CREATE OR REPLACE FUNCTION auto_set_estadoreserva_confirmada()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.id_estado_reserva IS NULL THEN
        SELECT id_estado_reserva INTO NEW.id_estado_reserva
        FROM estadosreservas 
        WHERE designacao = 'Confirmada';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER auto_set_estadoreserva_confirmada_trigger
BEFORE INSERT ON reservas
FOR EACH ROW EXECUTE FUNCTION auto_set_estadoreserva_confirmada();

CREATE OR REPLACE FUNCTION verificar_data_hora_reserva() 
RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM reservas 
        WHERE id_mesa = NEW.id_mesa 
        AND NEW.data_hora < data_hora + INTERVAL '1 hour'  -- Começa antes do fim da reserva existente
        AND NEW.data_hora + INTERVAL '1 hour' > data_hora  -- Termina depois do início da reserva existente
        AND id_reserva != NEW.id_reserva
        AND id_estado_reserva != (SELECT id_estado_reserva FROM estadosreservas WHERE designacao = 'Cancelada')
    ) THEN
        RAISE EXCEPTION 'Uma reserva não pode se sobrepor a outra';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_data_hora_reserva_trigger
BEFORE INSERT OR UPDATE OF data_hora ON reservas
FOR EACH ROW 
EXECUTE FUNCTION verificar_data_hora_reserva();


-- MESAS
CREATE OR REPLACE FUNCTION auto_set_estadomesa_disponivel() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.id_estado_mesa IS NULL THEN
        SELECT id_estado_mesa INTO NEW.id_estado_mesa
        FROM estadosmesas 
        WHERE designacao = 'Disponivel';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER auto_set_estadomesa_disponivel_trigger
BEFORE INSERT ON mesas
FOR EACH ROW EXECUTE FUNCTION auto_set_estadomesa_disponivel();


CREATE OR REPLACE FUNCTION auto_set_numero_mesa() RETURNS TRIGGER AS $$
DECLARE
    max_numero INT;
BEGIN
    SELECT COALESCE(MAX(numero), 0) + 1 INTO max_numero FROM mesas;
    NEW.numero = max_numero;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER auto_set_numero_mesa_trigger
BEFORE INSERT ON mesas
FOR EACH ROW EXECUTE FUNCTION auto_set_numero_mesa();