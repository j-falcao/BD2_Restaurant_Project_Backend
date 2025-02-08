-- ADMINISTRADOR
REVOKE EXECUTE ON PROCEDURE get_ingredientes_by_fornecedor FROM administrador;
REVOKE EXECUTE ON PROCEDURE get_utensilios_by_fornecedor FROM administrador;

REVOKE EXECUTE ON PROCEDURE get_utensilios_by_receita FROM administrador;
REVOKE EXECUTE ON PROCEDURE get_ingredientes_by_receita FROM administrador;

REVOKE EXECUTE ON PROCEDURE comprar_carrinho_atual_ingredientes FROM administrador;
REVOKE EXECUTE ON PROCEDURE comprar_carrinho_atual_utensilios FROM administrador;

REVOKE EXECUTE ON PROCEDURE create_fornecedores FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_fornecedores FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_fornecedores FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_carrinhos FROM administrador;
REVOKE EXECUTE ON PROCEDURE comprar_carrinho_atual_ingredientes FROM administrador;
REVOKE EXECUTE ON PROCEDURE comprar_carrinho_atual_utensilios FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_carrinhos FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_ingredientes FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_ingredientes FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_ingredientes FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_ingredientescarrinhos_atual FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_ingredientescarrinhos_atual FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_ingredientescarrinhos_atual FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_utensilios FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_utensilios FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_utensilios FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_utensilioscarrinhos_atual FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_utensilioscarrinhos_atual FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_utensilioscarrinhos_atual FROM administrador;


-- COZINHEIRO
REVOKE EXECUTE ON PROCEDURE get_utensilios_by_receita FROM cozinheiro;
REVOKE EXECUTE ON PROCEDURE get_ingredientes_by_receita FROM cozinheiro;