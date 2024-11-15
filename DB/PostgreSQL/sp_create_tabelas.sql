CREATE OR REPLACE PROCEDURE create_tabelas() 
LANGUAGE plpgsql
AS $$
BEGIN
    CREATE TABLE IF NOT EXISTS EstadoMesa (
        id_estado_mesa SERIAL PRIMARY KEY,
        designacao VARCHAR(20) NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );


    /* CREATE TABLE IF NOT EXISTS Utilizador (
        id SERIAL PRIMARY KEY,
        turno_almoco BOOLEAN NOT NULL,
        turno_jantar BOOLEAN NOT NULL,
        data_nascimento DATE,
        genero VARCHAR(10) NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    */

    CREATE TABLE IF NOT EXISTS Fornecedor (
        id_fornecedor SERIAL PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        vende_ingredientes BOOLEAN DEFAULT FALSE NOT NULL,
        vende_utensilios BOOLEAN DEFAULT FALSE NOT NULL,
        morada VARCHAR(255) NOT NULL,
        email VARCHAR(254) NOT NULL,
        telefone VARCHAR(20) NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS Carrinho (
        id_carrinho SERIAL PRIMARY KEY,
        preco_total DECIMAL(10, 2) NOT NULL DEFAULT 0,
        data_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS Ingrediente (
        id_ingrediente SERIAL PRIMARY KEY,
        id_fornecedor INT REFERENCES Fornecedor(id_fornecedor) ON DELETE CASCADE,
        nome VARCHAR(255) NOT NULL,
        url_imagem VARCHAR(2048),
        quantidade_stock INT NOT NULL DEFAULT 0,
        unidade_medida VARCHAR(50) NOT NULL,
        limite_stock INT,
        preco DECIMAL(10, 2),
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS IngredienteCarrinho (
        id_ingrediente_carrinho SERIAL PRIMARY KEY,
        id_ingrediente INT REFERENCES Ingrediente(id_ingrediente) ON DELETE CASCADE,
        id_administrador INT REFERENCES Utilizador(id) ON DELETE CASCADE,
        id_carrinho INT REFERENCES Carrinho(id_carrinho) ON DELETE CASCADE,
        quantidade INT NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS Utensilio (
        id_utensilio SERIAL PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        url_imagem VARCHAR(2048),
        quantidade_stock INT NOT NULL DEFAULT 0,
        limite_stock INT,
        preco DECIMAL(10, 2) NOT NULL,
        id_fornecedor INT REFERENCES Fornecedor(id_fornecedor) ON DELETE CASCADE,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP

    );

    CREATE TABLE IF NOT EXISTS UtensilioCarrinho (
        id_utensilio_carrinho SERIAL PRIMARY KEY,
        id_utensilio INT REFERENCES Utensilio(id_utensilio) ON DELETE CASCADE,
        id_administrador INT REFERENCES Utilizador(id) ON DELETE CASCADE,
        id_carrinho INT REFERENCES Carrinho(id_carrinho) ON DELETE CASCADE,
        quantidade INT NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS Receita (
        id_receita SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        duracao INTERVAL NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS IngredienteReceita (
        id_ingrediente_receita SERIAL PRIMARY KEY,
        id_ingrediente INT REFERENCES Ingrediente(id_ingrediente) ON DELETE CASCADE,
        id_receita INT REFERENCES Receita(id_receita) ON DELETE CASCADE,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS UtensilioReceita (
        id_utensilio_receita SERIAL PRIMARY KEY,
        id_utensilio INT REFERENCES Utensilio(id_utensilio) ON DELETE CASCADE,
        id_receita INT REFERENCES Receita(id_receita) ON DELETE CASCADE,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS Instrucao (
        id_instrucao SERIAL PRIMARY KEY,
        id_receita INT REFERENCES Receita(id_receita) ON DELETE CASCADE,
        numero_sequencia INT,
        descricao TEXT NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS Mesa (
        id_mesa SERIAL PRIMARY KEY,
        id_estado_mesa INT REFERENCES EstadoMesa(id_estado_mesa) ON DELETE CASCADE,
        numero INT NOT NULL,
        capacidade_maxima INT NOT NULL,
        quantidade_clientes INT NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS Produto (
        id_produto SERIAL PRIMARY KEY,
        item BOOLEAN DEFAULT FALSE,
        menu BOOLEAN DEFAULT FALSE,
        nome VARCHAR(100) NOT NULL,
        url_imagem VARCHAR(2048),
        preco DECIMAL(10, 2) NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS Tipo (
        id_tipo SERIAL PRIMARY KEY,
        designacao VARCHAR(50) NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS Item (
        id_item INT PRIMARY KEY REFERENCES Produto(id_produto) ON DELETE CASCADE,
        id_tipo INT REFERENCES Tipo(id_tipo) ON DELETE CASCADE,
        porcao_unidade_medida VARCHAR(50) NOT NULL,
        porcao INT NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS ItemTipo (
        id_item_tipo SERIAL PRIMARY KEY,
        id_item INT REFERENCES Item(id_item) ON DELETE CASCADE,
        id_tipo INT REFERENCES Tipo(id_tipo) ON DELETE CASCADE,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS Categoria (
        id_categoria SERIAL PRIMARY KEY,
        designacao VARCHAR(50) NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS ItemCategoria (
        id_item_categoria SERIAL PRIMARY KEY,
        id_item INT REFERENCES Item(id_item) ON DELETE CASCADE,
        id_categoria INT REFERENCES Categoria(id_categoria) ON DELETE CASCADE,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS Opcao (
        id_opcao SERIAL PRIMARY KEY,
        designacao VARCHAR(100) NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS ItemOpcao (
        id_item_opcao SERIAL PRIMARY KEY,
        id_item INT REFERENCES Item(id_item) ON DELETE CASCADE,
        id_opcao INT REFERENCES Opcao(id_opcao) ON DELETE CASCADE,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS Menu (
        id_menu INT PRIMARY KEY REFERENCES Produto(id_produto) ON DELETE CASCADE,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS ItemMenu (
        id_item_menu SERIAL PRIMARY KEY,
        id_item INT REFERENCES Item(id_item) ON DELETE CASCADE,
        id_menu INT REFERENCES Menu(id_menu) ON DELETE CASCADE,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS DiaSemana (
        id_dia_semana SERIAL PRIMARY KEY,
        designacao VARCHAR(50) NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP

    );

    CREATE TABLE IF NOT EXISTS MenuDiaSemana (
        id_menu_dia_semana SERIAL PRIMARY KEY,
        id_menu INT REFERENCES Menu(id_menu) ON DELETE CASCADE,
        id_dia_semana INT REFERENCES DiaSemana(id_dia_semana) ON DELETE CASCADE,
        almoco BOOLEAN DEFAULT FALSE,
        jantar BOOLEAN DEFAULT FALSE,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP

    );

    CREATE TABLE IF NOT EXISTS Servico (
        id_servico SERIAL PRIMARY KEY,
        id_garcom INT REFERENCES Utilizador(id) ON DELETE CASCADE,
        id_mesa INT REFERENCES Mesa(id_mesa) ON DELETE CASCADE,
        data_hora_inicio TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        data_hora_fim TIMESTAMP,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS Pedido (
        id_pedido SERIAL PRIMARY KEY,
        id_servico INT REFERENCES Servico(id_servico) ON DELETE CASCADE,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS PedidoProduto (
        id_pedido_produto SERIAL PRIMARY KEY,
        id_pedido INT REFERENCES Pedido(id_pedido) ON DELETE CASCADE,
        id_produto INT REFERENCES Produto(id_produto) ON DELETE CASCADE,
        id_cozinheiro INT REFERENCES Utilizador(id) ON DELETE CASCADE,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS PedidoProdutoItemOpcao (
        id_pedido_produto_item_opcao SERIAL PRIMARY KEY,
        id_item_opcao INT REFERENCES ItemOpcao(id_item_opcao) ON DELETE CASCADE,
        id_pedido_produto INT REFERENCES PedidoProduto(id_pedido_produto) ON DELETE CASCADE,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS Reserva (
        id_reserva SERIAL PRIMARY KEY,
        id_mesa INT REFERENCES Mesa(id_mesa) ON DELETE CASCADE,
        data_hora TIMESTAMP NOT NULL,
        minutos_antes INTERVAL NOT NULL CHECK (minutos_antes >= '0 minutes' AND minutos_antes <= '120 minutes'),
        minutos_depois INTERVAL NOT NULL CHECK (minutos_depois >= '0 minutes' AND minutos_depois <= '120 minutes'),
        id_servico INT REFERENCES Servico(id_servico) ON DELETE CASCADE,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
END;
$$;