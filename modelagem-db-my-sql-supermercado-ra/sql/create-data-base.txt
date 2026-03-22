
-- ===============================================
-- BANCO DE DADOS: SUPERMERCADO R&A
-- MODELO FÍSICO COM PKs E FKs
-- ===============================================

CREATE DATABASE IF NOT EXISTS supermercado_ra;
USE supermercado_ra;

-- ===============================================
-- CLIENTE
-- ===============================================
CREATE TABLE tbl_cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_cliente VARCHAR(45) NOT NULL,
    telefone VARCHAR(45),
    cpf VARCHAR(15)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ===============================================
-- COLABORADORES
-- ===============================================
CREATE TABLE tbl_colaboradores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_colaborador VARCHAR(45) NOT NULL,
    cargo VARCHAR(25),
    cpf VARCHAR(15),
    data_admissao DATE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ===============================================
-- FORNECEDOR
-- ===============================================
CREATE TABLE tbl_fornecedor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(45) NOT NULL,
    cnpj VARCHAR(14) NOT NULL,
    telefone VARCHAR(12)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ===============================================
-- PRODUTO
-- ===============================================
CREATE TABLE tbl_produto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    preco_unitario DECIMAL(10,2) NOT NULL,
    descricao TEXT,
    tbl_fornecedor_id INT NOT NULL,
    CONSTRAINT fk_produto_fornecedor
        FOREIGN KEY (tbl_fornecedor_id)
        REFERENCES tbl_fornecedor(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ===============================================
-- VENDAS
-- ===============================================
CREATE TABLE tbl_vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    valor_total FLOAT,
    data_venda DATE,
    tbl_cliente_id INT NOT NULL,
    tbl_colaboradores_id INT NOT NULL,
    CONSTRAINT fk_vendas_cliente
        FOREIGN KEY (tbl_cliente_id)
        REFERENCES tbl_cliente(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    CONSTRAINT fk_vendas_colaboradores
        FOREIGN KEY (tbl_colaboradores_id)
        REFERENCES tbl_colaboradores(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ===============================================
-- ITENS DE VENDA
-- ===============================================
CREATE TABLE tbl_item_vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quantidade INT NOT NULL,
    preco_unitario FLOAT NOT NULL,
    tbl_produto_id INT NOT NULL,
    tbl_vendas_id INT NOT NULL,
    CONSTRAINT fk_itemvendas_produto
        FOREIGN KEY (tbl_produto_id)
        REFERENCES tbl_produto(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    CONSTRAINT fk_itemvendas_vendas
        FOREIGN KEY (tbl_vendas_id)
        REFERENCES tbl_vendas(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ===============================================
-- PAGAMENTOS
-- ===============================================
CREATE TABLE tbl_pagamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    valor_pagamento FLOAT NOT NULL,
    tbl_colaboradores_id INT NOT NULL,
    tbl_fornecedor_id INT NOT NULL,
    CONSTRAINT fk_pagamento_colaborador
        FOREIGN KEY (tbl_colaboradores_id)
        REFERENCES tbl_colaboradores(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    CONSTRAINT fk_pagamento_fornecedor
        FOREIGN KEY (tbl_fornecedor_id)
        REFERENCES tbl_fornecedor(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
