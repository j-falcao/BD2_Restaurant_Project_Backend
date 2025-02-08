-- ADMINISTRADOR
GRANT SELECT ON
    fornecedores_view,
    tiposcarrinhos_view,
    utensilios_view,
    ingredientes_view,
    carrinhos_view,
    ingredientescarrinhos_view,
    utensilioscarrinhos_view,
    carrinho_atual_ingredientes_view,
    carrinho_atual_utensilios_view,
    utensilioscarrinho_atual_view,
    ingredientescarrinho_atual_view,
    instrucoes_view,
    receitas_view
TO administrador;

GRANT INSERT, UPDATE, DELETE ON
    fornecedores,
    utensilios,
    ingredientes,
    carrinhos,
    ingredientescarrinhos,
    utensilioscarrinhos,
    instrucoes,
    receitas,
    ingredientesreceitas,
    utensiliosreceitas
TO administrador;

GRANT EXECUTE ON PROCEDURE get_ingredientes_by_fornecedor TO administrador;
GRANT EXECUTE ON PROCEDURE get_utensilios_by_fornecedor TO administrador;

GRANT EXECUTE ON PROCEDURE comprar_carrinho_atual_ingredientes TO administrador;
GRANT EXECUTE ON PROCEDURE comprar_carrinho_atual_utensilios TO administrador;


-- COZINHEIRO
GRANT SELECT ON
    utensilios_view,
    ingredientes_view,
    tiposcarrinhos_view,
    carrinho_atual_ingredientes_view,
    carrinho_atual_utensilios_view,
    utensilioscarrinho_atual_view,
    ingredientescarrinho_atual_view,
    instrucoes_view,
    receitas_view
TO cozinheiro;

GRANT INSERT, UPDATE, DELETE ON
    instrucoes,
    utensiliosreceitas,
    ingredientesreceitas
TO cozinheiro;

GRANT UPDATE ON
    receitas
TO cozinheiro;

GRANT EXECUTE ON PROCEDURE get_utensilios_by_receita TO cozinheiro;
GRANT EXECUTE ON PROCEDURE get_ingredientes_by_receita TO cozinheiro;

GRANT EXECUTE ON PROCEDURE get_receitas_by_ingrediente TO cozinheiro;
GRANT EXECUTE ON PROCEDURE get_receitas_by_utensilio TO cozinheiro;

-- GARÇOM
GRANT SELECT ON
    utensilios_view,
    ingredientes_view
TO garcom;
