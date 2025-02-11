CREATE TABLE IF NOT EXISTS estadosmesas (
	id_estado_mesa SERIAL PRIMARY KEY,
	designacao VARCHAR(100) NOT NULL UNIQUE CHECK (designacao IN ('Disponivel', 'Ocupada', 'Reservada')),
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS mesas (
	id_mesa SERIAL PRIMARY KEY,
	id_estado_mesa INT REFERENCES estadosmesas(id_estado_mesa) ON DELETE CASCADE,
	capacidade_maxima INT NOT NULL CHECK (capacidade_maxima > 0),
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS servicos (
	id_servico SERIAL PRIMARY KEY,
	id_garcom INT REFERENCES utilizadores(id) ON DELETE CASCADE,
	id_mesa INT REFERENCES mesas(id_mesa) ON DELETE CASCADE, -- trigger para impedir a criação de serviços se mesa estiver ocupada
	data_hora_fim TIMESTAMP,
	preco_total DECIMAL(10, 2) NOT NULL DEFAULT 0 CHECK (preco_total >= 0),
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS pedidos ( -- trigger para impedir a criação de pedidos para serviços inativos
	id_pedido SERIAL PRIMARY KEY,
	id_servico INT REFERENCES servicos(id_servico) ON DELETE CASCADE,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS estadospedidosprodutos (
	id_estado_pedido_produto SERIAL PRIMARY KEY,
	designacao VARCHAR(100) NOT NULL UNIQUE CHECK (designacao IN ('Pendente', 'Preparando', 'Pronto')),
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS pedidosprodutos ( -- trigger para impedir a criação de pedidosprodutos para serviços inativos
	id_pedido_produto SERIAL PRIMARY KEY,
	id_pedido INT NOT NULL REFERENCES pedidos(id_pedido) ON DELETE CASCADE,
	id_produto INT NOT NULL REFERENCES produtos(id_produto) ON DELETE CASCADE,
	id_estado_pedido_produto INT NOT NULL REFERENCES estadospedidosprodutos(id_estado_pedido_produto) ON DELETE CASCADE,
	quantidade INT NOT NULL CHECK (quantidade > 0),
	id_cozinheiro INT REFERENCES utilizadores(id) ON DELETE CASCADE, -- podem existir pedidos que estejam a aguardar cozinheiro, então o cozinheiro pode ser nulo
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS estadosreservas (
	id_estado_reserva SERIAL PRIMARY KEY,
	designacao VARCHAR(100) NOT NULL UNIQUE CHECK (designacao IN ('Confirmada', 'Concluida', 'Cancelada')),
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS reservas (
    id_reserva SERIAL PRIMARY KEY,
    id_mesa INT REFERENCES mesas(id_mesa) ON DELETE CASCADE,
    id_estado_reserva INT REFERENCES estadosreservas(id_estado_reserva) ON DELETE CASCADE,
    quantidade_pessoas INT NOT NULL CHECK (quantidade_pessoas > 0),
    id_garcom INT NOT NULL REFERENCES utilizadores(id) ON DELETE CASCADE, -- garçom que fez a reserva
    data_hora TIMESTAMP NOT NULL CHECK (data_hora > CURRENT_TIMESTAMP + INTERVAL '1 hour'),
    observacoes TEXT,
    id_servico INT REFERENCES servicos(id_servico) ON DELETE SET NULL, -- serviço associado à reserva, se houver
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
