CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_updated_at_cargos
BEFORE UPDATE ON cargos
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_utilizadores
BEFORE UPDATE ON utilizadores
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_utilizadorescargos
BEFORE UPDATE ON utilizadorescargos
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_estadosmesas
BEFORE UPDATE ON estadosmesas
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_fornecedores
BEFORE UPDATE ON fornecedores
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_carrinhos
BEFORE UPDATE ON carrinhos
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_ingredientes
BEFORE UPDATE ON ingredientes
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_ingredientescarrinhos
BEFORE UPDATE ON ingredientescarrinhos
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_utensilios
BEFORE UPDATE ON utensilios
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_utensilioscarrinhos
BEFORE UPDATE ON utensilioscarrinhos
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_receitas
BEFORE UPDATE ON receitas
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_ingredientesreceitas
BEFORE UPDATE ON ingredientesreceitas
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_utensiliosreceitas
BEFORE UPDATE ON utensiliosreceitas
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_instrucoes
BEFORE UPDATE ON instrucoes
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_mesas
BEFORE UPDATE ON mesas
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_produtos
BEFORE UPDATE ON produtos
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_tipos
BEFORE UPDATE ON tipos
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_itens
BEFORE UPDATE ON itens
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_itenstipos
BEFORE UPDATE ON itenstipos
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_categorias
BEFORE UPDATE ON categorias
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_itenscategorias
BEFORE UPDATE ON itenscategorias
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_opcoes
BEFORE UPDATE ON opcoes
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_itensopcoes
BEFORE UPDATE ON itensopcoes
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_menus
BEFORE UPDATE ON menus
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_itensmenus
BEFORE UPDATE ON itensmenus
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_diassemana
BEFORE UPDATE ON diassemana
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_menusdiassemana
BEFORE UPDATE ON menusdiassemana
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_servicos
BEFORE UPDATE ON servicos
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_pedidos
BEFORE UPDATE ON pedidos
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_pedidosprodutos
BEFORE UPDATE ON pedidosprodutos
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

-- CREATE TRIGGER set_updated_at_pedidosprodutositensopcoes
-- BEFORE UPDATE ON pedidosprodutositensopcoes
-- FOR EACH ROW
-- EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at_reservas
BEFORE UPDATE ON reservas
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();



-- Carrinhos
-- Atualizar carrinho ao atualizar a adicinar ou remover um ingrediente ou utensilio
CREATE OR REPLACE FUNCTION update_preco_carrinho_by_content()
RETURNS TRIGGER AS $$
DECLARE 
    novo_preco DECIMAL(10, 2);
BEGIN
    novo_preco := COALESCE((
        SELECT SUM(item.preco * carrinho.quantidade)
        FROM (
            SELECT id_ingrediente AS id_item, preco FROM ingredientes
            UNION ALL
            SELECT id_utensilio AS id_item, preco FROM utensilios
        ) item
        INNER JOIN (
            SELECT id_ingrediente AS id_item, quantidade, id_carrinho FROM ingredientescarrinhos
            UNION ALL
            SELECT id_utensilio AS id_item, quantidade, id_carrinho FROM utensilioscarrinhos
        ) carrinho ON item.id_item = carrinho.id_item
        WHERE carrinho.id_carrinho = COALESCE(NEW.id_carrinho, OLD.id_carrinho)
    ), 0);

    UPDATE carrinhos
    SET preco_total = novo_preco
    WHERE id_carrinho = COALESCE(NEW.id_carrinho, OLD.id_carrinho);

    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

-- Atualizar carrinho atual ao atualizar o preco de um ingrediente ou utensilio presentes nesse carrinho
CREATE OR REPLACE FUNCTION update_preco_carrinho_by_preco()
RETURNS TRIGGER AS $$
DECLARE 
    id_carrinho_alvo INTEGER;
    novo_preco DECIMAL(10, 2);
BEGIN
    SELECT id_carrinho 
    INTO id_carrinho_alvo
    FROM carrinhos 
    WHERE data_compra IS NULL 
    ORDER BY id_carrinho DESC 
    LIMIT 1;

    IF id_carrinho_alvo IS NULL THEN
        RETURN NULL;
    END IF;

    novo_preco := COALESCE((
        SELECT SUM(item.preco * carrinho.quantidade)
        FROM (
            SELECT id_ingrediente AS id_item, preco FROM ingredientes
            UNION ALL
            SELECT id_utensilio AS id_item, preco FROM utensilios
        ) item
        INNER JOIN (
            SELECT id_ingrediente AS id_item, quantidade, id_carrinho FROM ingredientescarrinhos
            UNION ALL
            SELECT id_utensilio AS id_item, quantidade, id_carrinho FROM utensilioscarrinhos
        ) carrinho ON item.id_item = carrinho.id_item
        WHERE carrinho.id_carrinho = id_carrinho_alvo
    ), 0);

    UPDATE carrinhos
    SET preco_total = novo_preco
    WHERE id_carrinho = id_carrinho_alvo;

    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_preco_carrinho_ingredientescarrinhos
AFTER INSERT OR UPDATE OR DELETE ON ingredientescarrinhos
FOR EACH ROW
EXECUTE FUNCTION update_preco_carrinho_by_content();

CREATE TRIGGER update_preco_carrinho_utensilioscarrinhos
AFTER INSERT OR UPDATE OR DELETE ON utensilioscarrinhos
FOR EACH ROW
EXECUTE FUNCTION update_preco_carrinho_by_content();

CREATE TRIGGER update_preco_carrinho_ingredientes
AFTER UPDATE OF preco ON ingredientes
FOR EACH ROW
EXECUTE FUNCTION update_preco_carrinho_by_preco();

CREATE TRIGGER update_preco_carrinho_utensilios
AFTER UPDATE OF preco ON utensilios
FOR EACH ROW
EXECUTE FUNCTION update_preco_carrinho_by_preco();



-- Auto create carrinho
CREATE OR REPLACE FUNCTION auto_create_carrinho()
RETURNS TRIGGER AS $$
BEGIN
    -- Se apagarmos o carrinho atual ou atualizarmos o campo data_compra do carrinho atual, então criar um novo carrinho
    IF (TG_OP = 'DELETE' AND OLD.id_carrinho = ((SELECT MAX(id_carrinho) FROM carrinhos))) OR (TG_OP = 'UPDATE' AND NEW.data_compra != OLD.data_compra) THEN
        INSERT INTO carrinhos DEFAULT VALUES;
    END IF;

    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER auto_create_carrinho_trigger
BEFORE DELETE OR UPDATE ON carrinhos
FOR EACH ROW
EXECUTE FUNCTION auto_create_carrinho();


-- Instrucoes
CREATE OR REPLACE FUNCTION set_next_numero_sequencia()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.numero_sequencia IS NULL THEN
        SELECT COALESCE(MAX(numero_sequencia), 0) + 1
        INTO NEW.numero_sequencia
        FROM instrucoes
        WHERE id_receita = NEW.id_receita;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_next_numero_sequencia_trigger
BEFORE INSERT OR UPDATE ON instrucoes
FOR EACH ROW
EXECUTE FUNCTION set_next_numero_sequencia();




-- -- Refresh related materialized views
-- CREATE OR REPLACE FUNCTION refresh_carrinho_atual_related_views()
-- RETURNS TRIGGER AS $$
-- BEGIN
--     -- Refresh only if the current cart is updated
--     IF (TG_OP IN ('INSERT', 'UPDATE', 'DELETE')) AND NEW.id_carrinho = (SELECT MAX(id_carrinho) FROM carrinhos) THEN
--         REFRESH MATERIALIZED VIEW CONCURRENTLY carrinho_atual_view;
--         REFRESH MATERIALIZED VIEW CONCURRENTLY ingredientes_carrinho_atual_view;
--         REFRESH MATERIALIZED VIEW CONCURRENTLY utensilios_carrinho_atual_view;
--     END IF;

--     RETURN NULL;
-- END;
-- $$ LANGUAGE plpgsql;

-- CREATE TRIGGER refresh_carrinho_atual_related_views_trigger_ingredientescarrinhos
-- AFTER INSERT OR UPDATE OR DELETE ON ingredientescarrinhos
-- FOR EACH ROW
-- EXECUTE FUNCTION refresh_carrinho_atual_related_views();

-- CREATE TRIGGER refresh_carrinho_atual_related_views_trigger_utensilioscarrinhos
-- AFTER INSERT OR UPDATE OR DELETE ON utensilioscarrinhos
-- FOR EACH ROW
-- EXECUTE FUNCTION refresh_carrinho_atual_related_views();

-- CREATE TRIGGER refresh_carrinho_atual_related_views_trigger_carrinhos
-- AFTER INSERT OR UPDATE ON carrinhos
-- FOR EACH ROW
-- EXECUTE FUNCTION refresh_carrinho_atual_related_views();




-- Servicos
-- CREATE OR REPLACE FUNCTION set_preco_servico()
-- RETURNS TRIGGER AS $$
-- BEGIN
    



