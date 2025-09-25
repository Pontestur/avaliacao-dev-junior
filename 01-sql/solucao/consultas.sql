-- ========================================
-- EXERCÍCIOS SQL - SISTEMA DE BIBLIOTECA
-- ========================================
-- INSTRUÇÕES: Complete as consultas SQL abaixo

-- Exercício 1: Listar livros disponíveis ordenados por título
-- Objetivo: Mostrar todos os livros que estão disponíveis 
-- ordenados alfabeticamente por título
-- TODO: Escrever consulta aqui
SELECT * FROM livros
ORDER BY titulo ASC;

-- OU (Caso desejem apenas titulo)

SELECT titulo FROM livros
ORDER BY titulo ASC;

-- Exercício 2: Empréstimos ativos com nome do usuário e título do livro  
-- Objetivo: Mostrar empréstimos que ainda não foram devolvidos 
-- com informações do usuário e do livro
-- TODO: Escrever consulta aqui
Select * from emprestimos;

select * from emprestimos
where data_devolucao is NULL;

select u.nome, l.titulo
from emprestimos e
JOIN usuarios u on e.usuario_id = u.id
join livros l on e.livro_id = l.id
where e.data_devolucao is NULL;

-- Exercício 3: Contar quantos livros cada usuário já pegou emprestado
-- Objetivo: Mostrar nome do usuário e quantidade total de empréstimos
-- TODO: Escrever consulta aqui  

select * from usuarios;

Select * from emprestimos;


select u.nome, count(e.usuario_id) as Quantidade
from usuarios u
join emprestimos e on u.id = e.usuario_id
group by u.id, u.nome;

-- Exercício 4: Usuários que nunca fizeram empréstimos
-- Objetivo: Encontrar usuários que não têm nenhum registro na tabela emprestimos
-- TODO: Escrever consulta aqui

select u.nome from usuarios u
left join emprestimos e on u.id = e.usuario_id
where e.usuario_id is null;
-- pela query anterior - exercicio 3 - creio que todos os usuarios alugaram ao menos um livro
