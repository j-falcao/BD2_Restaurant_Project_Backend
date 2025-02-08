-- ADMINISTRADOR
REVOKE EXECUTE ON PROCEDURE get_ingredientes_by_fornecedor FROM administrador;
REVOKE EXECUTE ON PROCEDURE get_utensilios_by_fornecedor FROM administrador;

REVOKE EXECUTE ON PROCEDURE get_utensilios_by_receita FROM administrador;
REVOKE EXECUTE ON PROCEDURE get_ingredientes_by_receita FROM administrador;

REVOKE EXECUTE ON PROCEDURE comprar_carrinho_atual_ingredientes FROM administrador;
REVOKE EXECUTE ON PROCEDURE comprar_carrinho_atual_utensilios FROM administrador;


-- COZINHEIRO
REVOKE EXECUTE ON PROCEDURE get_utensilios_by_receita FROM cozinheiro;
REVOKE EXECUTE ON PROCEDURE get_ingredientes_by_receita FROM cozinheiro;