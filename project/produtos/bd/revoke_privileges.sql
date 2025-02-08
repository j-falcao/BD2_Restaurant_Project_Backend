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

REVOKE EXECUTE ON PROCEDURE create_receitas FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_receitas FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_receitas FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_ingredientesreceitas FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_ingredientesreceitas FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_ingredientesreceitas FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_utensiliosreceitas FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_utensiliosreceitas FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_utensiliosreceitas FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_instrucoes FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_instrucoes FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_instrucoes FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_tipos FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_tipos FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_tipos FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_itens FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_itens FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_itens FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_itenstipos FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_itenstipos FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_itenstipos FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_categorias FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_categorias FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_categorias FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_itenscategorias FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_itenscategorias FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_itenscategorias FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_opcoes FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_opcoes FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_opcoes FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_itensopcoes FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_itensopcoes FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_itensopcoes FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_menus FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_menus FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_menus FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_itensmenus FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_itensmenus FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_itensmenus FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_diassemana FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_diassemana FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_diassemana FROM administrador;
REVOKE EXECUTE ON PROCEDURE create_menusdiassemana FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_menusdiassemana FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_menusdiassemana FROM administrador;


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

REVOKE EXECUTE ON PROCEDURE update_receitas FROM cozinheiro;
REVOKE EXECUTE ON PROCEDURE create_ingredientesreceitas FROM cozinheiro;
REVOKE EXECUTE ON PROCEDURE update_ingredientesreceitas FROM cozinheiro;
REVOKE EXECUTE ON PROCEDURE delete_ingredientesreceitas FROM cozinheiro;
REVOKE EXECUTE ON PROCEDURE create_utensiliosreceitas FROM cozinheiro;
REVOKE EXECUTE ON PROCEDURE update_utensiliosreceitas FROM cozinheiro;
REVOKE EXECUTE ON PROCEDURE delete_utensiliosreceitas FROM cozinheiro;
REVOKE EXECUTE ON PROCEDURE create_instrucoes FROM cozinheiro;
REVOKE EXECUTE ON PROCEDURE update_instrucoes FROM cozinheiro;
REVOKE EXECUTE ON PROCEDURE delete_instrucoes FROM cozinheiro;
