-- ADMINISTRADOR
GRANT SELECT ON
    utilizadores_view,
    garcons_view,
    cozinheiros_view,
    administradores_view,
    superusers_view,
    cargos_view
TO administrador;
GRANT EXECUTE ON PROCEDURE create_utilizadores TO administrador;
GRANT EXECUTE ON PROCEDURE update_utilizadores TO administrador;
GRANT EXECUTE ON PROCEDURE delete_utilizadores TO administrador;
GRANT EXECUTE ON PROCEDURE promover_utilizadores TO administrador; -- nao se pode promover o proprio utilizador

-- GARCOM
GRANT SELECT ON
    garcons_view,
TO garcom;
GRANT EXECUTE ON PROCEDURE update_utilizadores TO garcom; -- So se pode alterar o próprio utilizador

-- COZINHEIRO
GRANT SELECT ON
    cozinheiros_view,
TO cozinheiro;
GRANT EXECUTE ON PROCEDURE update_utilizadores TO cozinheiro; -- So se pode alterar o próprio utilizador