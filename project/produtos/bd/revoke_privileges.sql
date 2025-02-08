-- ADMINISTRADOR
REVOKE EXECUTE ON PROCEDURE get_receitas_by_ingrediente FROM administrador;
REVOKE EXECUTE ON PROCEDURE get_receitas_by_utensilio FROM administrador;

-- COZINHEIRO

REVOKE EXECUTE ON PROCEDURE get_receitas_by_ingrediente FROM cozinheiro;
REVOKE EXECUTE ON PROCEDURE get_receitas_by_utensilio FROM cozinheiro;
