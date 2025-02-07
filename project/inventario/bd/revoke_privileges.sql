-- ADMINISTRADOR
REVOKE EXECUTE ON PROCEDURE get_ingredientes_by_fornecedor FROM administrador;
REVOKE EXECUTE ON PROCEDURE get_utensilios_by_fornecedor FROM administrador;

REVOKE EXECUTE ON PROCEDURE get_utensilios_by_receita FROM administrador;
REVOKE EXECUTE ON PROCEDURE get_ingredientes_by_receita FROM administrador;

REVOKE EXECUTE ON PROCEDURE get_receitas_by_ingrediente FROM administrador;
REVOKE EXECUTE ON PROCEDURE get_receitas_by_utensilio FROM administrador;


-- COZINHEIRO
REVOKE EXECUTE ON PROCEDURE get_utensilios_by_receita FROM cozinheiro;
REVOKE EXECUTE ON PROCEDURE get_ingredientes_by_receita FROM cozinheiro;

REVOKE EXECUTE ON PROCEDURE get_receitas_by_ingrediente FROM cozinheiro;
REVOKE EXECUTE ON PROCEDURE get_receitas_by_utensilio FROM cozinheiro;
