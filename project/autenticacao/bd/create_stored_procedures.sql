CREATE OR REPLACE PROCEDURE mee(OUT e JSON) 
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT json_agg(row_to_json(t)) 
    INTO e
    FROM (
        SELECT current_user AS user
    ) t;
END;
$$;

CREATE OR REPLACE PROCEDURE create_cargos(_new_designacao VARCHAR(100), OUT _new_cargo JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO cargos (designacao)
    VALUES (_new_designacao)
    RETURNING row_to_json(cargos) INTO _new_cargo;
END;
$$;

CREATE OR REPLACE PROCEDURE update_cargos(id_cargo_in INT, _new_designacao VARCHAR(100), OUT _new_cargo JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE cargos
    SET designacao = _new_designacao
    WHERE id_cargo = id_cargo_in
    RETURNING row_to_json(cargos) INTO _new_cargo;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_cargos(id_cargo_in INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM cargos
    WHERE id_cargo = id_cargo_in;
END;
$$;


CREATE OR REPLACE PROCEDURE create_utilizadores(_new_username VARCHAR(50), _new_id_cargo INT, _new_first_name VARCHAR(100), _new_last_name VARCHAR(100), _new_is_superuser BOOLEAN, _new_url_imagem VARCHAR(2048), _new_password VARCHAR(255), OUT _new_utilizador JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO utilizadores (username, id_cargo, first_name, last_name, is_superuser, url_imagem, password)
    VALUES (_new_username, _new_id_cargo, _new_first_name, _new_last_name, _new_is_superuser, _new_url_imagem, _new_password)
    RETURNING row_to_json(utilizadores) INTO _new_utilizador;
END;
$$;


CREATE OR REPLACE PROCEDURE update_utilizadores(id_in INT, _new_id_cargo INT, _new_first_name VARCHAR(100), _new_last_name VARCHAR(100), _new_is_superuser BOOLEAN, _new_username VARCHAR(50), _new_url_imagem VARCHAR(2048), _new_password VARCHAR(255), OUT _new_utilizador JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE utilizadores
    SET id_cargo = _new_id_cargo, first_name = _new_first_name, last_name = _new_last_name, is_superuser = _new_is_superuser, username = _new_username, url_imagem = _new_url_imagem, password = _new_password
    WHERE id = id_in
    RETURNING row_to_json(utilizadores) INTO _new_utilizador;
END;
$$;

CREATE OR REPLACE PROCEDURE promover_utilizadores(id_in INT, _new_id_cargo INT, OUT _new_utilizador JSON)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE utilizadores
    SET id_cargo = _new_id_cargo
    WHERE id = id_in
    RETURNING row_to_json(utilizadores) INTO _new_utilizador;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_utilizadores(id_in INT, OUT _id INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM utilizadores
    WHERE id = id_in
    RETURNING id INTO _id;
END;
$$;