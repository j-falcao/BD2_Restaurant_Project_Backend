-- ADMINISTRADOR
REVOKE EXECUTE ON PROCEDURE get_categorias_by_item FROM administrador;
REVOKE EXECUTE ON PROCEDURE get_itens_by_categoria FROM administrador;

REVOKE EXECUTE ON PROCEDURE get_tipos_by_item FROM administrador;
REVOKE EXECUTE ON PROCEDURE get_itens_by_tipo FROM administrador;

REVOKE EXECUTE ON PROCEDURE get_opcoes_by_item FROM administrador;
REVOKE EXECUTE ON PROCEDURE get_itens_by_opcao FROM administrador;

REVOKE EXECUTE ON PROCEDURE get_itens_by_menu FROM administrador;
REVOKE EXECUTE ON PROCEDURE get_menus_by_item FROM administrador;

REVOKE EXECUTE ON PROCEDURE get_menus_by_diasemana FROM administrador;
REVOKE EXECUTE ON PROCEDURE get_diassemana_by_menu FROM administrador;

REVOKE EXECUTE ON PROCEDURE get_receitas_by_ingrediente FROM administrador;
REVOKE EXECUTE ON PROCEDURE get_receitas_by_utensilio FROM administrador;

-- COZINHEIRO

REVOKE EXECUTE ON PROCEDURE get_categorias_by_item FROM cozinheiro;
REVOKE EXECUTE ON PROCEDURE get_itens_by_categoria FROM cozinheiro;

REVOKE EXECUTE ON PROCEDURE get_tipos_by_item FROM cozinheiro;
REVOKE EXECUTE ON PROCEDURE get_itens_by_tipo FROM cozinheiro;

REVOKE EXECUTE ON PROCEDURE get_opcoes_by_item FROM cozinheiro;
REVOKE EXECUTE ON PROCEDURE get_itens_by_opcao FROM cozinheiro;

REVOKE EXECUTE ON PROCEDURE get_itens_by_menu FROM cozinheiro;
REVOKE EXECUTE ON PROCEDURE get_menus_by_item FROM cozinheiro;

REVOKE EXECUTE ON PROCEDURE get_menus_by_diasemana FROM cozinheiro;
REVOKE EXECUTE ON PROCEDURE get_diassemana_by_menu FROM cozinheiro;

REVOKE EXECUTE ON PROCEDURE get_receitas_by_ingrediente FROM cozinheiro;
REVOKE EXECUTE ON PROCEDURE get_receitas_by_utensilio FROM cozinheiro;
