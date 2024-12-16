CREATE OR REPLACE FUNCTION create_ingrediente(
    _id_fornecedor INT,
    _nome VARCHAR,
    _url_imagem VARCHAR DEFAULT NULL,
    _quantidade_stock INT,
    _unidade_medida VARCHAR,
    _limite_stock INT DEFAULT NULL,
    _preco DECIMAL(10, 2)
) RETURNS VOID AS $$
BEGIN
    INSERT INTO ingredientes (
        id_fornecedor, nome, url_imagem, quantidade_stock,
        unidade_medida, limite_stock, preco, created_at, updated_at
    ) VALUES (
        _id_fornecedor, _nome, _url_imagem, _quantidade_stock,
        _unidade_medida, _limite_stock, _preco, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
    );
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION update_ingrediente(
    _id_ingrediente INT,
    _id_fornecedor INT,
    _nome VARCHAR,
    _url_imagem VARCHAR DEFAULT NULL,
    _quantidade_stock INT,
    _unidade_medida VARCHAR,
    _limite_stock INT DEFAULT NULL,
    _preco DECIMAL(10, 2)
) RETURNS VOID AS $$
BEGIN
    UPDATE ingredientes
    SET id_fornecedor = _id_fornecedor,
        nome = _nome,
        url_imagem = _url_imagem,
        quantidade_stock = _quantidade_stock,
        unidade_medida = _unidade_medida,
        limite_stock = _limite_stock,
        preco = _preco,
        updated_at = CURRENT_TIMESTAMP
    WHERE id_ingrediente = _id_ingrediente;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION delete_ingrediente(_id_ingrediente INT) RETURNS VOID AS $$
BEGIN
    DELETE FROM ingredientes WHERE id_ingrediente = _id_ingrediente;
END;
$$ LANGUAGE plpgsql;
