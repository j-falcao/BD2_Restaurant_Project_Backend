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
        SELECT COALESCE(SUM(produtos.preco), 0) 
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
CREATE OR REPLACE FUNCTION verificar_mesa_ocupada() RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM servicos WHERE id_mesa = NEW.id_mesa AND data_hora_fim IS NULL
    ) THEN
        RAISE EXCEPTION 'Esta mesa já está ocupada por outro serviço.';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_mesa_ocupada_trigger
BEFORE INSERT ON servicos
FOR EACH ROW EXECUTE FUNCTION verificar_mesa_ocupada();

-- Atualizar o estado da mesa para 'Ocupada' após a criação de um serviço
CREATE OR REPLACE FUNCTION atualizar_estado_mesa_ocupada() RETURNS TRIGGER AS $$
BEGIN
    UPDATE mesas 
    SET id_estado_mesa = (SELECT id_estado_mesa FROM estadosmesas WHERE designacao = 'Ocupada') 
    WHERE id_mesa = NEW.id_mesa;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER atualizar_estado_mesa_ocupada_trigger
AFTER INSERT ON servicos
FOR EACH ROW EXECUTE FUNCTION atualizar_estado_mesa_ocupada();

-- Atualizar o estado da mesa para 'Disponivel' quando o serviço é finalizado
CREATE OR REPLACE FUNCTION atualizar_estado_mesa_disponivel() RETURNS TRIGGER AS $$
BEGIN
    UPDATE mesas 
    SET id_estado_mesa = (SELECT id_estado_mesa FROM estadosmesas WHERE designacao = 'Disponivel')
    WHERE id_mesa = NEW.id_mesa;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER atualizar_estado_mesa_disponivel_trigger
AFTER UPDATE OF data_hora_fim ON servicos
FOR EACH ROW WHEN (NEW.data_hora_fim IS NOT NULL)
EXECUTE FUNCTION atualizar_estado_mesa_disponivel();


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


-- RESERVAS
CREATE OR REPLACE FUNCTION set_estado_reserva_pendente()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.id_estado_reserva IS NULL THEN
        SELECT id_estado_reserva INTO NEW.id_estado_reserva
        FROM estadosreservas 
        WHERE designacao = 'Pendente';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_estado_reserva_pendente_trigger
BEFORE INSERT ON reservas
FOR EACH ROW
EXECUTE FUNCTION set_estado_reserva_pendente();

CREATE OR REPLACE FUNCTION verificar_garcom_reserva() RETURNS TRIGGER AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM utilizadores 
        WHERE id = NEW.id_garcom 
        AND id_cargo = (SELECT id_cargo FROM cargos WHERE designacao = 'Garcom')
    ) THEN
        RAISE EXCEPTION 'O utilizador não é um garçom';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_garcom_reserva_trigger
BEFORE INSERT OR UPDATE ON reservas
FOR EACH ROW EXECUTE FUNCTION verificar_garcom_reserva();


-- MESAS
CREATE OR REPLACE FUNCTION set_estado_mesa_disponivel() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.id_estado_mesa IS NULL THEN
        SELECT id_estado_mesa INTO NEW.id_estado_mesa
        FROM estadosmesas 
        WHERE designacao = 'Disponivel';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_estado_mesa_disponivel_trigger
BEFORE INSERT ON mesas
FOR EACH ROW    
EXECUTE FUNCTION set_estado_mesa_disponivel();

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


CREATE OR REPLACE FUNCTION set_next_numero_mesa() RETURNS TRIGGER AS $$
DECLARE
    max_numero INT;
BEGIN
    SELECT COALESCE(MAX(numero), 0) + 1 INTO max_numero FROM mesas;
    NEW.numero = max_numero;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_next_numero_mesa_trigger
BEFORE INSERT ON mesas
FOR EACH ROW EXECUTE FUNCTION set_next_numero_mesa();