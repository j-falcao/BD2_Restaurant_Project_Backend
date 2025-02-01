-- carrinhos
CREATE UNIQUE INDEX idx_carrinhos_id_carrinho ON carrinhos(id_carrinho);
CREATE INDEX idx_carrinhos_data_compra ON carrinhos(id_carrinho) WHERE data_compra IS NOT NULL;
-- CREATE INDEX idx_ingredientes_preco ON ingredientes(preco);
-- CREATE INDEX idx_utensilios_preco ON utensilios(preco);
