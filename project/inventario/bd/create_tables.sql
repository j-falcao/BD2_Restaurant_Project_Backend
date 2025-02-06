
CREATE TABLE IF NOT EXISTS fornecedores (
	id_fornecedor SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	vende_ingredientes BOOLEAN DEFAULT FALSE NOT NULL,
	vende_utensilios BOOLEAN DEFAULT FALSE NOT NULL,
	morada VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL,
	telemovel VARCHAR(50) NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tipos_carrinhos ( -- Tipos: Ingredientes, Utensilios
	id_tipo_carrinho SERIAL PRIMARY KEY,
	designacao VARCHAR(100) NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS carrinhos (
	id_carrinho SERIAL PRIMARY KEY,
	id_tipo_carrinho INT REFERENCES tipos_carrinhos(id_tipo_carrinho) ON DELETE CASCADE,
	preco_total DECIMAL(10, 2) NOT NULL DEFAULT 0,
	data_compra TIMESTAMP,
	qtd_artigos INT NOT NULL DEFAULT 0,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ingredientes (
	id_ingrediente SERIAL PRIMARY KEY,
	id_fornecedor INT REFERENCES fornecedores(id_fornecedor) ON DELETE CASCADE,
	nome VARCHAR(255) NOT NULL,
	url_imagem VARCHAR(2048),
	quantidade_stock INT NOT NULL DEFAULT 0,
	unidade_medida VARCHAR(50) NOT NULL,
	limite_stock INT,
	preco DECIMAL(10, 2) NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ingredientescarrinhos (
	id_ingrediente_carrinho SERIAL PRIMARY KEY,
	id_ingrediente INT REFERENCES ingredientes(id_ingrediente) ON DELETE CASCADE,
	id_administrador INT REFERENCES utilizadores(id) ON DELETE CASCADE,
	id_carrinho INT REFERENCES carrinhos(id_carrinho) ON DELETE CASCADE,
	quantidade INT NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT unique_ingrediente_carrinho UNIQUE (id_ingrediente, id_administrador, id_carrinho)
);

CREATE TABLE IF NOT EXISTS utensilios (
	id_utensilio SERIAL PRIMARY KEY,
	id_fornecedor INT REFERENCES fornecedores(id_fornecedor) ON DELETE CASCADE,
	nome VARCHAR(100) NOT NULL,
	url_imagem VARCHAR(2048),
	quantidade_stock INT NOT NULL DEFAULT 0,
	unidade_medida VARCHAR(50) NOT NULL,
	limite_stock INT,
	preco DECIMAL(10, 2) NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS utensilioscarrinhos (
	id_utensilio_carrinho SERIAL PRIMARY KEY,
	id_utensilio INT REFERENCES utensilios(id_utensilio) ON DELETE CASCADE,
	id_administrador INT REFERENCES utilizadores(id) ON DELETE CASCADE,
	id_carrinho INT REFERENCES carrinhos(id_carrinho) ON DELETE CASCADE,
	quantidade INT NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT unique_utensilio_carrinho UNIQUE (id_utensilio, id_administrador, id_carrinho)
);

CREATE TABLE IF NOT EXISTS receitas (
	id_receita SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	duracao INTERVAL NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ingredientesreceitas (
	id_ingrediente_receita SERIAL PRIMARY KEY,
	id_ingrediente INT REFERENCES ingredientes(id_ingrediente) ON DELETE CASCADE,
	id_receita INT REFERENCES receitas(id_receita) ON DELETE CASCADE,
	quantidade INT NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS utensiliosreceitas (
	id_utensilio_receita SERIAL PRIMARY KEY,
	id_utensilio INT REFERENCES utensilios(id_utensilio) ON DELETE CASCADE,
	id_receita INT REFERENCES receitas(id_receita) ON DELETE CASCADE,
	quantidade INT NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS instrucoes (
	id_instrucao SERIAL PRIMARY KEY,
	id_receita INT REFERENCES receitas(id_receita) ON DELETE CASCADE,
	numero_sequencia INT NOT NULL,
	descricao TEXT NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT unique_instrucao UNIQUE (id_receita, numero_sequencia)
);