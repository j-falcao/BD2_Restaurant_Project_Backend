INSERT INTO Turno(designacao, hora_inicio, hora_fim) VALUES 
    ('Almoço', '10:00:00', '16:00:00'),
    ('Jantar', '18:00:00', '24:00:00');

INSERT INTO EstadoMesa(designacao) VALUES
    ('Aberta'),
    ('Ocupada'),
    ('Reservada'),
    ('Fechada');

-- Insert INTO Utilizador(id_turno, primeiro_nome, ultimo_nome, data_nascimento)


INSERT INTO Fornecedor(nome, ingredientes, utensilios, morada, email, telefone) VALUES
    ('Fornecedor 1', true, false, 'Morada 1', 'E2GwU@example.com', '123456789'),
    ('Fornecedor 2', false, true, 'Morada 2', 'pCjvI@example.com', '987654321'),
    ('Fornecedor 3', true, false, 'Morada 3', 'J5xNp@example.com', '555555555'),
    ('Fornecedor 4', false, true, 'Morada 4', 'dMn9Z@example.com', '444444444'),
    ('Fornecedor 5', true, false, 'Morada 5', 'H7gUy@example.com', '333333333'),
    ('Fornecedor 6', false, true, 'Morada 6', 'K5HsZ@example.com', '222222222'),
    ('Fornecedor 7', true, false, 'Morada 7', 'nVW9d@example.com', '111111111'),
    ('Fornecedor 8', false, true, 'Morada 8', '8mCt3@example.com', '999999999'),
    ('Fornecedor 9', true, false, 'Morada 9', 'K5HsZ@example.com', '888888888'),
    ('Fornecedor 10', false, true, 'Morada 10', 'K5HsZ@example.com', '777777777');

INSERT INTO Carrinho(preco_total, data_compra) VALUES
    (438.55, CURRENT_TIMESTAMP),
    (567.90, CURRENT_TIMESTAMP),
    (461, CURRENT_TIMESTAMP),
    (446, CURRENT_TIMESTAMP),
    (793.45, CURRENT_TIMESTAMP),
    (438.55, CURRENT_TIMESTAMP),
    (567.90, CURRENT_TIMESTAMP),
    (461, CURRENT_TIMESTAMP),
    (446, CURRENT_TIMESTAMP),
    (793.45, CURRENT_TIMESTAMP);


INSERT INTO Ingrediente(id_fornecedor, nome, url_imagem, quantidade_stock, unidade_medida, limite_stock, preco) VALUES
    (1, 'Ingrediente 1', 'https://example.com/ingrediente1.jpg', 10, 'unidade', 100, 10.99),
    (2, 'Ingrediente 2', 'https://example.com/ingrediente2.jpg', 5, 'unidade', 50, 15.99),
    (3, 'Ingrediente 3', 'https://example.com/ingrediente3.jpg', 20, 'unidade', 200, 8.99),
    (4, 'Ingrediente 4', 'https://example.com/ingrediente4.jpg', 15, 'unidade', 75, 12.99),
    (5, 'Ingrediente 5', 'https://example.com/ingrediente5.jpg', 25, 'unidade', 250, 7.99),
    (6, 'Ingrediente 6', 'https://example.com/ingrediente6.jpg', 30, 'unidade', 300, 9.99),
    (7, 'Ingrediente 7', 'https://example.com/ingrediente7.jpg', 35, 'unidade', 350, 11.99),
    (8, 'Ingrediente 8', 'https://example.com/ingrediente8.jpg', 40, 'unidade', 400, 14.99),
    (9, 'Ingrediente 9', 'https://example.com/ingrediente9.jpg', 45, 'unidade', 450, 6.99),
    (10, 'Ingrediente 10', 'https://example.com/ingrediente10.jpg', 50, 'unidade', 500, 16.99);


-- INSERT INTO IngredienteCarrinho(id_ingrediente, id_administrador, id_carrinho, quantidade) VALUES -- TESTE: id_administrador tem de pertenecer a um utilizador que esteja no grupo dos administradores 


INSERT INTO Utensilio(nome, url_imagem, quantidade_stock, limite_stock, preco, id_fornecedor) VALUES
    ('Utensilio 1', 'https://example.com/utensilio1.jpg', 10, 100, 10.99, 1),
    ('Utensilio 2', 'https://example.com/utensilio2.jpg', 5, 50, 15.99, 2),
    ('Utensilio 3', 'https://example.com/utensilio3.jpg', 20, 200, 8.99, 3),
    ('Utensilio 4', 'https://example.com/utensilio4.jpg', 15, 75, 12.99, 4),
    ('Utensilio 5', 'https://example.com/utensilio5.jpg', 25, 250, 7.99, 5),
    ('Utensilio 6', 'https://example.com/utensilio6.jpg', 30, 300, 9.99, 6),
    ('Utensilio 7', 'https://example.com/utensilio7.jpg', 12, 60, 14.99, 7),
    ('Utensilio 8', 'https://example.com/utensilio8.jpg', 8, 40, 11.99, 8),
    ('Utensilio 9', 'https://example.com/utensilio9.jpg', 18, 180, 6.99, 9),
    ('Utensilio 10', 'https://example.com/utensilio10.jpg', 6, 30, 16.99, 10);


-- INSERT INTO UtensilioCarrinho(id_utensilio, id_administrador, id_carrinho, quantidade) VALUES -- TESTE: id_administrador tem de pertenecer a um utilizador que esteja no grupo dos administradores 


INSERT INTO Receita(nome, duracao) VALUES
    ('Receita 1', '01:00:00'),
    ('Receita 2', '02:00:00'),
    ('Receita 3', '03:00:00'),
    ('Receita 4', '04:00:00'),
    ('Receita 5', '05:00:00'),
    ('Receita 6', '06:00:00'),
    ('Receita 7', '07:00:00'),
    ('Receita 8', '08:00:00'),
    ('Receita 9', '09:00:00'),
    ('Receita 10', '10:00:00');


INSERT INTO IngredienteReceita(id_ingrediente, id_receita) VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10);


INSERT INTO UtensilioReceita(id_utensilio, id_receita) VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10);


INSERT INTO Instrucao(id_receita, numero_sequencia, descricao) VALUES
    (1, 1, 'Misturar os ovos com a farinha'),
    (1, 2, 'Adicionar o açúcar'),
    (1, 3, 'Adicionar o leite'),
    (1, 4, 'Adicionar o fermento'),
    (1, 5, 'Levar ao fogo'),
    (2, 1, 'Pré-aquecer o forno'),
    (2, 2, 'Temperar a carne'),
    (2, 3, 'Preparar a travessa de forno'),
    (2, 4, 'Levar ao forno');


INSERT INTO Mesa(id_estado_mesa, numero, capacidade_maxima, quantidade_clientes) VALUES
    (1, 1, 2, 0),
    (1, 2, 2, 0),
    (1, 3, 4, 0),
    (1, 4, 4, 0),
    (1, 5, 8, 0),
    (1, 6, 8, 0),
    (1, 7, 4, 0),
    (1, 8, 4, 0),
    (1, 9, 2, 0),
    (1, 10, 2, 0);


INSERT INTO Produto(item, menu, nome, url_imagem, preco) VALUES
    (TRUE, FALSE, 'Pão', 'https://example.com/pao.jpg', 0.5),
    (TRUE, FALSE, 'Café', 'https://example.com/cafe.jpg', 1.0),
    (TRUE, FALSE, 'Bolo', 'https://example.com/bolo.jpg', 2.0),
    (TRUE, FALSE, 'Sumo de laranja natural', 'https://example.com/refrigerante.jpg', 1.5),
    (TRUE, FALSE, 'Cerveja', 'https://example.com/cerveja.jpg', 2.5),
    (TRUE, FALSE, 'Coca-cola', 'https://example.com/coca-cola.jpg', 2.0),
    (TRUE, FALSE, 'Batata frita', 'https://example.com/batata-frita.jpg', 5),
    (TRUE, FALSE, 'Sandes', 'https://example.com/sanduiche_bebida_cafe.jpg', 3),
    (TRUE, FALSE, 'Hamburguer', 'https://example.com/hamburguer.jpg', 4.5),
    (FALSE, TRUE, 'Sandes com sumo de laranja natural e café', 'https://example.com/sanduiche_bebida_cafe.jpg', 5.5),
    (FALSE, TRUE, 'Hamburguer com batata frita e coca-cola', 'https://example.com/hamburguer_batata_cola.jpg', 8.5);


INSERT INTO Tipo (designacao) VALUES
    ('Entrada'),
    ('Bebida'),
    ('Acompanhamento'),
    ('Prato principal'),
    ('Sobremesa'),
    ('Salada');


INSERT INTO Item(id_item, id_tipo, porcao_unidade_medida, porcao) VALUES
    (1, 1, 'unidade', 1),
    (2, 2, 'ml', 30),
    (3, 5, 'fatia', 1),
    (4, 2, 'ml', 250),
    (5, 2, 'ml', 250),
    (6, 2, 'ml', 330),
    (7, 3, 'gr', 200),
    (8, 4, 'unidade', 1),
    (9, 4, 'unidade', 1);

    
INSERT INTO ItemTipo(id_item, id_tipo) VALUES
    (1, 1),
    (2, 2),
    (2, 5),
    (4, 2),
    (5, 2),
    (6, 2),
    (7, 2),
    (8, 4),
    (9, 4);


INSERT INTO Categoria(designacao) VALUES
    ('Vegan'),
    ('Sem glutem'),
    ('Sem lactose'),
    ('Cafeína'),
    ('Picante'),
    ('Alcoólico'),
    ('Cítrico'),
    ('Energético');


INSERT INTO ItemCategoria(id_item, id_categoria) VALUES
    (2, 1),
    (2, 2),
    (2, 3),
    (5, 6),
    (6, 5),
    (7, 2),
    (7, 7),
    (8, 1),
    (9, 3);


INSERT INTO Opcao(designacao) VALUES
    ('Sem gelo'),
    ('Com gelo'),
    ('Mal passado'),
    ('Médio passado'),
    ('Bem passado'),
    ('Sem sal'),
    ('Com sal'),
    ('Sem molhos'),
    ('Cem molhos');


INSERT INTO ItemOpcao(id_item, id_opcao) VALUES
    (2, 1),
    (2, 2),
    (5, 1),
    (5, 2),
    (6, 1),
    (6, 2),
    (7, 1),
    (7, 2),
    (8, 6),
    (8, 7),
    (9, 8),
    (9, 9);


INSERT INTO Menu(id_menu) VALUES
    (10),
    (11);

INSERT INTO ItemMenu(id_item, id_menu) VALUES
    (8, 10),
    (2, 10),
    (4, 10),
    (9, 11),
    (7, 11),
    (6, 11);


INSERT INTO DiaSemana(designacao) VALUES
    ('Domingo'),
    ('Segunda-feira'),
    ('Terça-feira'),
    ('Quarta-feira'),
    ('Quinta-feira'),
    ('Sexta-feira'),
    ('Sabado');


INSERT INTO MenuDiaSemana(id_menu, id_dia_semana, almoco, jantar) VALUES
    (10, 1, FALSE, FALSE),
    (10, 2, FALSE, FALSE),
    (10, 3, FALSE, FALSE),
    (10, 4, FALSE, FALSE),
    (11, 6, FALSE, FALSE),
    (11, 7, FALSE, FALSE);


-- INSERT INTO Servico(id_garcom, id_mesa, data_hora_inicio, data_hora_fim) VALUES

-- INSERT INTO Pedido(id_servico) VALUES

-- INSERT INTO PedidoProduto(id_pedido, id_produto, id_cozinheiro) VALUES

-- INSERT INTO PedidoProdutoItemOpcao(id_item_opcao, id_pedido_produto) VALUES -- TESTE: Para que se possa criar um registo nesta tabela é necessário que o valor da coluna id_opcao da tabela ItemOpcao, na linha: (PK - id_item_opcao da tabela PedidoProdutoItemOpcao) pertença ao grupo dos ids das opcoes do item com ID igual ao id_produto da tabela PedidoProduto, na linha: (PK - id_pedido_produto da tabela PedidoProdutoItemOpcao). Pala além disso, o dito produto tem do ser um item e não um menu

-- INSERT INTO Reserva(id_mesa, data_hora, minutos_antes, minutos_depois, id_servico) VALUES
