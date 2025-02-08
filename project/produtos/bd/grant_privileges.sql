-- ADMINISTRADOR
GRANT EXECUTE ON PROCEDURE get_receitas_by_ingrediente TO administrador;
GRANT EXECUTE ON PROCEDURE get_receitas_by_utensilio TO administrador;

-- COZINHEIRO
GRANT EXECUTE ON PROCEDURE get_receitas_by_ingrediente TO cozinheiro;
GRANT EXECUTE ON PROCEDURE get_receitas_by_utensilio TO cozinheiro;
