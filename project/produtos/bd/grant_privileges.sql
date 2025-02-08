-- ADMINISTRADOR
GRANT SELECT ON
    produtos_view
    instrucoes_view
    receitas_view
    categorias_view
    tipos_view
    opcoes_view
    itens_view
    itenscategorias_view
    itenstipos_view
    itensopcoes_view
    menus_view
    itensmenus_view
    diassemana_view
    menusdiassemana_view
TO administrador;

GRANT INSERT, UPDATE, DELETE ON
    produtos,
    instrucoes,
    receitas,
    categorias,
    tipos,
    opcoes,
    itens,
    itenscategorias,
    itenstipos,
    itensopcoes,
    menus,
    itensmenus,
    diassemana,
    menusdiassemana
TO administrador;

GRANT EXECUTE ON PROCEDURE get_categorias_by_item TO administrador;
GRANT EXECUTE ON PROCEDURE get_itens_by_categoria TO administrador;

GRANT EXECUTE ON PROCEDURE get_tipos_by_item TO administrador;
GRANT EXECUTE ON PROCEDURE get_itens_by_tipo TO administrador;

GRANT EXECUTE ON PROCEDURE get_opcoes_by_item TO administrador;
GRANT EXECUTE ON PROCEDURE get_itens_by_opcao TO administrador;

GRANT EXECUTE ON PROCEDURE get_itens_by_menu TO administrador;
GRANT EXECUTE ON PROCEDURE get_menus_by_item TO administrador;

GRANT EXECUTE ON PROCEDURE get_menus_by_diasemana TO administrador;
GRANT EXECUTE ON PROCEDURE get_diassemana_by_menu TO administrador;

GRANT EXECUTE ON PROCEDURE get_receitas_by_ingrediente TO administrador;
GRANT EXECUTE ON PROCEDURE get_receitas_by_utensilio TO administrador;

GRANT EXECUTE ON PROCEDURE create_receitas TO administrador;
GRANT EXECUTE ON PROCEDURE update_receitas TO administrador;
GRANT EXECUTE ON PROCEDURE delete_receitas TO administrador;
GRANT EXECUTE ON PROCEDURE create_ingredientesreceitas TO administrador;
GRANT EXECUTE ON PROCEDURE update_ingredientesreceitas TO administrador;
GRANT EXECUTE ON PROCEDURE delete_ingredientesreceitas TO administrador;
GRANT EXECUTE ON PROCEDURE create_utensiliosreceitas TO administrador;
GRANT EXECUTE ON PROCEDURE update_utensiliosreceitas TO administrador;
GRANT EXECUTE ON PROCEDURE delete_utensiliosreceitas TO administrador;
GRANT EXECUTE ON PROCEDURE create_instrucoes TO administrador;
GRANT EXECUTE ON PROCEDURE update_instrucoes TO administrador;
GRANT EXECUTE ON PROCEDURE delete_instrucoes TO administrador;
GRANT EXECUTE ON PROCEDURE create_tipos TO administrador;
GRANT EXECUTE ON PROCEDURE update_tipos TO administrador;
GRANT EXECUTE ON PROCEDURE delete_tipos TO administrador;
GRANT EXECUTE ON PROCEDURE create_itens TO administrador;
GRANT EXECUTE ON PROCEDURE update_itens TO administrador;
GRANT EXECUTE ON PROCEDURE delete_itens TO administrador;
GRANT EXECUTE ON PROCEDURE create_itenstipos TO administrador;
GRANT EXECUTE ON PROCEDURE update_itenstipos TO administrador;
GRANT EXECUTE ON PROCEDURE delete_itenstipos TO administrador;
GRANT EXECUTE ON PROCEDURE create_categorias TO administrador;
GRANT EXECUTE ON PROCEDURE update_categorias TO administrador;
GRANT EXECUTE ON PROCEDURE delete_categorias TO administrador;
GRANT EXECUTE ON PROCEDURE create_itenscategorias TO administrador;
GRANT EXECUTE ON PROCEDURE update_itenscategorias TO administrador;
GRANT EXECUTE ON PROCEDURE delete_itenscategorias TO administrador;
GRANT EXECUTE ON PROCEDURE create_opcoes TO administrador;
GRANT EXECUTE ON PROCEDURE update_opcoes TO administrador;
GRANT EXECUTE ON PROCEDURE delete_opcoes TO administrador;
GRANT EXECUTE ON PROCEDURE create_itensopcoes TO administrador;
GRANT EXECUTE ON PROCEDURE update_itensopcoes TO administrador;
GRANT EXECUTE ON PROCEDURE delete_itensopcoes TO administrador;
GRANT EXECUTE ON PROCEDURE create_menus TO administrador;
GRANT EXECUTE ON PROCEDURE update_menus TO administrador;
GRANT EXECUTE ON PROCEDURE delete_menus TO administrador;
GRANT EXECUTE ON PROCEDURE create_itensmenus TO administrador;
GRANT EXECUTE ON PROCEDURE update_itensmenus TO administrador;
GRANT EXECUTE ON PROCEDURE delete_itensmenus TO administrador;
GRANT EXECUTE ON PROCEDURE create_diassemana TO administrador;
GRANT EXECUTE ON PROCEDURE update_diassemana TO administrador;
GRANT EXECUTE ON PROCEDURE delete_diassemana TO administrador;
GRANT EXECUTE ON PROCEDURE create_menusdiassemana TO administrador;
GRANT EXECUTE ON PROCEDURE update_menusdiassemana TO administrador;
GRANT EXECUTE ON PROCEDURE delete_menusdiassemana TO administrador;

-- COZINHEIRO
GRANT SELECT ON
    produtos_view
    instrucoes_view
    receitas_view
    categorias_view
    tipos_view
    opcoes_view
    itens_view
    itenscategorias_view
    itenstipos_view
    itensopcoes_view
    menus_view
    itensmenus_view
    diassemana_view
    menusdiassemana_view
TO cozinheiro;

GRANT INSERT, UPDATE, DELETE ON
    instrucoes,
    utensiliosreceitas,
    ingredientesreceitas
TO cozinheiro;

GRANT UPDATE ON
    receitas
TO cozinheiro;

GRANT EXECUTE ON PROCEDURE get_categorias_by_item TO administrador;
GRANT EXECUTE ON PROCEDURE get_itens_by_categoria TO administrador;

GRANT EXECUTE ON PROCEDURE get_tipos_by_item TO administrador;
GRANT EXECUTE ON PROCEDURE get_itens_by_tipo TO administrador;

GRANT EXECUTE ON PROCEDURE get_opcoes_by_item TO administrador;
GRANT EXECUTE ON PROCEDURE get_itens_by_opcao TO administrador;

GRANT EXECUTE ON PROCEDURE get_itens_by_menu TO administrador;
GRANT EXECUTE ON PROCEDURE get_menus_by_item TO administrador;

GRANT EXECUTE ON PROCEDURE get_menus_by_diasemana TO administrador;
GRANT EXECUTE ON PROCEDURE get_diassemana_by_menu TO administrador;

GRANT EXECUTE ON PROCEDURE get_receitas_by_ingrediente TO cozinheiro;
GRANT EXECUTE ON PROCEDURE get_receitas_by_utensilio TO cozinheiro;

GRANT EXECUTE ON PROCEDURE update_receitas TO cozinheiro;
GRANT EXECUTE ON PROCEDURE create_ingredientesreceitas TO cozinheiro;
GRANT EXECUTE ON PROCEDURE update_ingredientesreceitas TO cozinheiro;
GRANT EXECUTE ON PROCEDURE delete_ingredientesreceitas TO cozinheiro;
GRANT EXECUTE ON PROCEDURE create_utensiliosreceitas TO cozinheiro;
GRANT EXECUTE ON PROCEDURE update_utensiliosreceitas TO cozinheiro;
GRANT EXECUTE ON PROCEDURE delete_utensiliosreceitas TO cozinheiro;
GRANT EXECUTE ON PROCEDURE create_instrucoes TO cozinheiro;
GRANT EXECUTE ON PROCEDURE update_instrucoes TO cozinheiro;
GRANT EXECUTE ON PROCEDURE delete_instrucoes TO cozinheiro;