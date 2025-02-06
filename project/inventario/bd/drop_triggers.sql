-- CARRINHOS
DROP TRIGGER IF EXISTS update_preco_carrinho_ingredientescarrinhos_trigger ON ingredientescarrinhos;
DROP TRIGGER IF EXISTS update_preco_carrinho_utensilioscarrinhos_trigger ON utensilioscarrinhos;
DROP TRIGGER IF EXISTS update_preco_carrinho_ingredientes_trigger ON ingredientes;
DROP TRIGGER IF EXISTS update_preco_carrinho_utensilios_trigger ON utensilios;
DROP TRIGGER IF EXISTS auto_create_carrinho_trigger ON carrinhos;

-- INSTRUCOES
DROP TRIGGER IF EXISTS set_next_numero_sequencia_trigger ON instrucoes;