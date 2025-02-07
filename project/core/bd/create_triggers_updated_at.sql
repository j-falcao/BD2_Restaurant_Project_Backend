CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_updated_at_cargos
BEFORE UPDATE ON cargos
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_utilizadores
BEFORE UPDATE ON utilizadores
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_estadosmesas
BEFORE UPDATE ON estadosmesas
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_fornecedores
BEFORE UPDATE ON fornecedores
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_carrinhos
BEFORE UPDATE ON carrinhos
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_ingredientes
BEFORE UPDATE ON ingredientes
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_ingredientescarrinhos
BEFORE UPDATE ON ingredientescarrinhos
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_utensilios
BEFORE UPDATE ON utensilios
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_utensilioscarrinhos
BEFORE UPDATE ON utensilioscarrinhos
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_receitas
BEFORE UPDATE ON receitas
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_ingredientesreceitas
BEFORE UPDATE ON ingredientesreceitas
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_utensiliosreceitas
BEFORE UPDATE ON utensiliosreceitas
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_instrucoes
BEFORE UPDATE ON instrucoes
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_mesas
BEFORE UPDATE ON mesas
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_produtos
BEFORE UPDATE ON produtos
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_tipos
BEFORE UPDATE ON tipos
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_itens
BEFORE UPDATE ON itens
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_itenstipos
BEFORE UPDATE ON itenstipos
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_categorias
BEFORE UPDATE ON categorias
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_itenscategorias
BEFORE UPDATE ON itenscategorias
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_opcoes
BEFORE UPDATE ON opcoes
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_itensopcoes
BEFORE UPDATE ON itensopcoes
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_menus
BEFORE UPDATE ON menus
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_itensmenus
BEFORE UPDATE ON itensmenus
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_diassemana
BEFORE UPDATE ON diassemana
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_menusdiassemana
BEFORE UPDATE ON menusdiassemana
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_servicos
BEFORE UPDATE ON servicos
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_pedidos
BEFORE UPDATE ON pedidos
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_pedidosprodutos
BEFORE UPDATE ON pedidosprodutos
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER set_updated_at_reservas
BEFORE UPDATE ON reservas
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();