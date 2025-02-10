-- ADMINISTRADOR
REVOKE EXECUTE ON PROCEDURE create_utilizadores FROM administrador;
REVOKE EXECUTE ON PROCEDURE update_utilizadores FROM administrador;
REVOKE EXECUTE ON PROCEDURE delete_utilizadores FROM administrador;
REVOKE EXECUTE ON PROCEDURE promover_utilizadores FROM administrador;

-- GARCOM
REVOKE EXECUTE ON PROCEDURE update_utilizadores FROM garcom;

-- COZINHEIRO
REVOKE EXECUTE ON PROCEDURE update_utilizadores FROM cozinheiro;