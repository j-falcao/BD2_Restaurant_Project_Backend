-- Carrinho View
CREATE OR REPLACE VIEW carrinhos_view AS
SELECT 
    c.id_carrinho,
    c.preco_total,
    c.data_compra,
    c.created_at,
    c.updated_at
FROM carrinho c
JOIN ingredientecarrinho ic ON ic.id_carrinho = c.id_carrinho
JOIN utilizador u1 ON u1.id = ic.id_administrador
JOIN utensiliocarrinho uc ON uc.id_carrinho = c.id_carrinho
JOIN utilizador u2 ON u2.id = uc.id_administrador;

-- Fornecedor View
CREATE OR REPLACE VIEW fornecedores_view AS
SELECT 
    f.id_fornecedor,
    f.nome,
    f.vende_ingredientes,
    f.vende_utensilios,
    f.morada,
    f.email,
    f.telefone,
    f.created_at,
    f.updated_at
FROM fornecedor f
JOIN ingrediente i ON i.id_fornecedor = f.id_fornecedor
JOIN utensilio u ON u.id_fornecedor = f.id_fornecedor;

-- Ingrediente View
CREATE OR REPLACE VIEW ingredientes_view AS
SELECT 
    i.id_ingrediente,
    i.nome,
    i.url_imagem,
    i.quantidade_stock,
    i.unidade_medida,
    i.limite_stock,
    i.preco,
    i.id_fornecedor,
    i.created_at,
    i.updated_at
FROM ingrediente i
JOIN fornecedor f ON i.id_fornecedor = f.id_fornecedor;

-- IngredienteCarrinho View
CREATE OR REPLACE VIEW ingredientescarrinhos_view AS
SELECT 
    ic.id_ingrediente_carrinho,
    ic.id_ingrediente,
    i.nome AS ingrediente_nome,
    ic.id_administrador,
    ic.id_carrinho,
    ic.quantidade,
    ic.created_at,
    ic.updated_at
FROM ingredientecarrinho ic
JOIN ingrediente i ON ic.id_ingrediente = i.id_ingrediente;

-- Utensilio View
CREATE OR REPLACE VIEW utensilios_view AS
SELECT 
    id_utensilio,
    nome,
    url_imagem,
    quantidade_stock,
    limite_stock,
    preco,
    id_fornecedor,
    created_at,
    updated_at
FROM utensilio;

-- UtensilioCarrinho View
CREATE OR REPLACE VIEW utensilioscarrinhos_view AS
SELECT 
    uc.id_utensilio_carrinho,
    uc.id_utensilio,
    u.nome AS utensilio_nome,
    uc.id_administrador,
    uc.id_carrinho,
    uc.quantidade,
    uc.created_at,
    uc.updated_at
FROM utensiliocarrinho uc
JOIN utensilio u ON uc.id_utensilio = u.id_utensilio;

-- Receita View
CREATE OR REPLACE VIEW receitas_view AS
SELECT 
    r.id_receita,
    r.nome,
    r.duracao,
	i.id_ingrediente,
	i.nome AS nome_ingrediente,
	i.url_imagem AS imagem_ingrediente,
	u.id_utensilio,
	u.nome AS nome_utensilio,
	u.url_imagem AS imagem_utensilio,
	ins.numero_sequencia,
	ins.descricao,
    r.created_at,
    r.updated_at
FROM receita r
JOIN ingredientereceita ir ON ir.id_receita = r.id_receita
JOIN ingrediente i ON i.id_ingrediente = ir.id_ingrediente
JOIN utensilioreceita ur ON ur.id_receita = r.id_receita
JOIN utensilio u ON u.id_utensilio = ur.id_utensilio
JOIN instrucao ins ON ins.id_receita = r.id_receita;


-- Instruções View
CREATE OR REPLACE VIEW instrucoes_view AS
SELECT
	id_instrucao,
	id_receita,
	numero_sequencia,
	descricao,
	created_at,
	updated_at
FROM instrucao;


-- UtensilioReceita View
CREATE OR REPLACE VIEW utensiliosreceitas_view AS
SELECT
	id_utensilio_receita,
	id_utensilio,
	id_receita,
	created_at,
	updated_at
FROM utensilioreceita;


-- IngredientesReceitas View
CREATE OR REPLACE VIEW ingredientesreceitas_view AS
SELECT
	id_ingrediente_receita,
	id_ingrediente,
	id_receita,
	created_at,
	updated_at
FROM ingredientereceita;