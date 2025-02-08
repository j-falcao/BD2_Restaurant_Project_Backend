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
TO administrador;

GRANT INSERT, UPDATE, DELETE ON
    fornecedores,
    utensilios,
    ingredientes,
    carrinhos,
    ingredientescarrinhos,
    utensilioscarrinhos,
TO administrador;

GRANT EXECUTE ON PROCEDURE get_ingredientes_by_fornecedor TO administrador;
GRANT EXECUTE ON PROCEDURE get_utensilios_by_fornecedor TO administrador;

GRANT EXECUTE ON PROCEDURE get_utensilios_by_receita TO administrador;
GRANT EXECUTE ON PROCEDURE get_ingredientes_by_receita TO administrador;

GRANT EXECUTE ON PROCEDURE comprar_carrinho_atual_ingredientes TO administrador;
GRANT EXECUTE ON PROCEDURE comprar_carrinho_atual_utensilios TO administrador;

GRANT EXECUTE ON PROCEDURE create_fornecedores TO administrador;
GRANT EXECUTE ON PROCEDURE update_fornecedores TO administrador;
GRANT EXECUTE ON PROCEDURE delete_fornecedores TO administrador;
GRANT EXECUTE ON PROCEDURE create_carrinhos TO administrador;
GRANT EXECUTE ON PROCEDURE comprar_carrinho_atual_ingredientes TO administrador;
GRANT EXECUTE ON PROCEDURE comprar_carrinho_atual_utensilios TO administrador;
GRANT EXECUTE ON PROCEDURE delete_carrinhos TO administrador;
GRANT EXECUTE ON PROCEDURE create_ingredientes TO administrador;
GRANT EXECUTE ON PROCEDURE update_ingredientes TO administrador;
GRANT EXECUTE ON PROCEDURE delete_ingredientes TO administrador;
GRANT EXECUTE ON PROCEDURE create_ingredientescarrinhos_atual TO administrador;
GRANT EXECUTE ON PROCEDURE update_ingredientescarrinhos_atual TO administrador;
GRANT EXECUTE ON PROCEDURE delete_ingredientescarrinhos_atual TO administrador;
GRANT EXECUTE ON PROCEDURE create_utensilios TO administrador;
GRANT EXECUTE ON PROCEDURE update_utensilios TO administrador;
GRANT EXECUTE ON PROCEDURE delete_utensilios TO administrador;
GRANT EXECUTE ON PROCEDURE create_utensilioscarrinhos_atual TO administrador;
GRANT EXECUTE ON PROCEDURE update_utensilioscarrinhos_atual TO administrador;
GRANT EXECUTE ON PROCEDURE delete_utensilioscarrinhos_atual TO administrador;


-- COZINHEIRO
GRANT SELECT ON
    utensilios_view,
    ingredientes_view,
TO cozinheiro;

GRANT EXECUTE ON PROCEDURE get_utensilios_by_receita TO cozinheiro;
GRANT EXECUTE ON PROCEDURE get_ingredientes_by_receita TO cozinheiro;

-- GARÇOM
GRANT SELECT ON
    utensilios_view,
    ingredientes_view
TO garcom;
