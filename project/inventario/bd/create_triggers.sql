-- CARRINHOS
-- Atualizar o stock ao finalizar compra carrinho
CREATE OR REPLACE FUNCTION update_quantidade_stock_on_compra_carrinho() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.data_compra IS NULL THEN
        RETURN NULL;
    END IF;

    IF NEW.id_tipo_carrinho = (SELECT id_tipo_carrinho FROM tiposcarrinhos WHERE designacao = 'Ingredientes') THEN
        UPDATE ingredientes
        SET quantidade_stock = quantidade_stock + (
            SELECT COALESCE(SUM(quantidade), 0)
            FROM ingredientescarrinhos
            WHERE id_carrinho = NEW.id_carrinho
            AND id_ingrediente = ingredientes.id_ingrediente
        )
        WHERE id_ingrediente IN (
            SELECT id_ingrediente
            FROM ingredientescarrinhos
            WHERE id_carrinho = NEW.id_carrinho
        );
    ELSE
        UPDATE utensilios
        SET quantidade_stock = quantidade_stock + (
            SELECT COALESCE(SUM(quantidade), 0)
            FROM utensilioscarrinhos
            WHERE id_carrinho = NEW.id_carrinho
            AND id_utensilio = utensilios.id_utensilio
        )
        WHERE id_utensilio IN (
            SELECT id_utensilio
            FROM utensilioscarrinhos
            WHERE id_carrinho = NEW.id_carrinho
        );
    END IF;

    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_quantidade_stock_on_compra_carrinho_trigger
AFTER UPDATE OF data_compra ON carrinhos
FOR EACH ROW
EXECUTE FUNCTION update_quantidade_stock_on_compra_carrinho();


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
        JOIN (
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
        JOIN (
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

CREATE TRIGGER update_preco_carrinho_ingredientescarrinhos_trigger
AFTER INSERT OR UPDATE OR DELETE ON ingredientescarrinhos
FOR EACH ROW
EXECUTE FUNCTION update_preco_carrinho_by_content();

CREATE TRIGGER update_preco_carrinho_utensilioscarrinhos_trigger
AFTER INSERT OR UPDATE OR DELETE ON utensilioscarrinhos
FOR EACH ROW
EXECUTE FUNCTION update_preco_carrinho_by_content();

CREATE TRIGGER update_preco_carrinho_ingredientes_trigger
AFTER UPDATE OF preco ON ingredientes
FOR EACH ROW
EXECUTE FUNCTION update_preco_carrinho_by_preco();

CREATE TRIGGER update_preco_carrinho_utensilios_trigger
AFTER UPDATE OF preco ON utensilios
FOR EACH ROW
EXECUTE FUNCTION update_preco_carrinho_by_preco();

-- Auto create carrinho
-- Se apagarmos o carrinho atual ou atualizarmos o campo data_compra do carrinho atual, então criar um novo carrinho
CREATE OR REPLACE FUNCTION auto_create_carrinho()
RETURNS TRIGGER AS $$
DECLARE _id_carrinho INT;
BEGIN
    INSERT INTO carrinhos(id_tipo_carrinho) 
    VALUES (OLD.id_tipo_carrinho);

    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER auto_create_carrinho_trigger_delete
AFTER DELETE ON carrinhos
FOR EACH ROW
EXECUTE FUNCTION auto_create_carrinho();

CREATE TRIGGER auto_create_carrinho_trigger_comprar
BEFORE UPDATE OF data_compra ON carrinhos
FOR EACH ROW
EXECUTE FUNCTION auto_create_carrinho();



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