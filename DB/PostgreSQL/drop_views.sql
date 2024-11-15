-- Drop complex views first
DROP VIEW IF EXISTS pedidosprodutositensopcoes_view CASCADE;
DROP VIEW IF EXISTS pedidosprodutos_view CASCADE;
DROP VIEW IF EXISTS pedidos_view CASCADE;

DROP VIEW IF EXISTS utensiliosreceitas_view CASCADE;
DROP VIEW IF EXISTS ingredientesreceitas_view CASCADE;
DROP VIEW IF EXISTS receitas_view CASCADE;

DROP VIEW IF EXISTS utensilioscarrinhos_view CASCADE;
DROP VIEW IF EXISTS ingredientescarrinhos_view CASCADE;
DROP VIEW IF EXISTS carrinhos_view CASCADE;

DROP VIEW IF EXISTS utensilios_view CASCADE;
DROP VIEW IF EXISTS ingredientes_view CASCADE;
DROP VIEW IF EXISTS fornecedores_view CASCADE;

DROP VIEW IF EXISTS itemmenu_view CASCADE;
DROP VIEW IF EXISTS menu_view CASCADE;
DROP VIEW IF EXISTS itemopcao_view CASCADE;
DROP VIEW IF EXISTS itemtipo_view CASCADE;
DROP VIEW IF EXISTS itemcategoria_view CASCADE;
DROP VIEW IF EXISTS item_view CASCADE;

DROP VIEW IF EXISTS opcao_view CASCADE;
DROP VIEW IF EXISTS tipo_view CASCADE;
DROP VIEW IF EXISTS categoria_view CASCADE;
DROP VIEW IF EXISTS produto_view CASCADE;

DROP VIEW IF EXISTS mesas_view CASCADE;
DROP VIEW IF EXISTS reservas_view CASCADE;
DROP VIEW IF EXISTS servicos_view CASCADE;

DROP VIEW IF EXISTS instrucoes_view CASCADE;
DROP VIEW IF EXISTS estadosmesas_view CASCADE;
DROP VIEW IF EXISTS utilizadores_view CASCADE;
