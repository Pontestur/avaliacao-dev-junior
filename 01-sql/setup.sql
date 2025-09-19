-- Criação das tabelas para avaliação
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    categoria TEXT,
    ano_publicacao INTEGER,
    disponivel BOOLEAN DEFAULT 1
);

CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT UNIQUE,
    data_cadastro DATE
);

CREATE TABLE IF NOT EXISTS emprestimos (
    id INTEGER PRIMARY KEY,
    usuario_id INTEGER,
    livro_id INTEGER,
    data_emprestimo DATE,
    data_devolucao DATE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (livro_id) REFERENCES livros(id)
);

-- Dados de teste
INSERT INTO usuarios (nome, email, data_cadastro) VALUES
('João Silva', 'joao@email.com', '2024-01-15'),
('Maria Santos', 'maria@email.com', '2024-02-20'),
('Pedro Costa', 'pedro@email.com', '2024-03-10');

INSERT INTO livros (titulo, autor, categoria, ano_publicacao, disponivel) VALUES
('Clean Code', 'Robert Martin', 'Tecnologia', 2008, 1),
('O Alquimista', 'Paulo Coelho', 'Ficção', 1988, 0),
('Estruturas de Dados', 'Thomas Cormen', 'Tecnologia', 2009, 1),
('1984', 'George Orwell', 'Ficção', 1949, 1),
('Python para Iniciantes', 'Mark Lutz', 'Tecnologia', 2020, 0);

INSERT INTO emprestimos (usuario_id, livro_id, data_emprestimo, data_devolucao) VALUES
(1, 2, '2024-08-15', '2024-08-30'),
(2, 5, '2024-09-01', NULL),
(1, 1, '2024-09-10', '2024-09-15'),
(3, 3, '2024-09-12', NULL);
