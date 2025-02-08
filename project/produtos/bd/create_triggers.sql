-- INSTRUCOES
CREATE OR REPLACE FUNCTION set_next_numero_sequencia()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.numero_sequencia IS NULL THEN
        SELECT COALESCE(MAX(numero_sequencia), 0) + 1
        INTO NEW.numero_sequencia
        FROM instrucoes
        WHERE id_receita = NEW.id_receita;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_next_numero_sequencia_trigger
BEFORE INSERT OR UPDATE ON instrucoes
FOR EACH ROW
EXECUTE FUNCTION set_next_numero_sequencia();
