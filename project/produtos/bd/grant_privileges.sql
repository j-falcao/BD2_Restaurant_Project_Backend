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
