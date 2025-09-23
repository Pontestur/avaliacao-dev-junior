# 📊 Avaliação SQL - Sistema de Biblioteca

## 🎯 Objetivo

Esta avaliação testa seus conhecimentos fundamentais de SQL através de um sistema simples de biblioteca. Você precisa completar **4 consultas SQL** no arquivo `solucao/consultas.sql`.

## 🛠️ Configuração do Ambiente

### Extensão Obrigatória
Instale a extensão **SQLite** (alexcvzz.vscode-sqlite) no VS Code.

### Como Usar a Extensão SQLite

#### 1. 📊 Visualizar Dados das Tabelas
1. Abra o arquivo `database.db` no VS Code
2. Pressione `Ctrl+Shift+P` (ou `Cmd+Shift+P` no Mac)
3. Digite: `SQLite: Open Database`
4. Selecione o arquivo `database.db`
5. Uma nova aba "SQLite Explorer" aparecerá na barra lateral
6. Clique nas tabelas para ver sua estrutura
7. Clique no ícone "▶️ Show Table" para ver os dados

#### 2. 🔍 Executar Consultas SQL
1. Crie um novo arquivo (ex: `teste.sql`)
2. Escreva sua consulta SQL
3. Pressione `Ctrl+Shift+P` → `SQLite: Run Query`
4. Selecione o banco `database.db`
5. Os resultados aparecerão em uma nova aba

#### 3. 💡 Dica Rápida
- Selecione o texto da consulta antes de executar
- Use `Ctrl+Shift+Q` para executar rapidamente

## 📋 Estrutura do Banco de Dados

O banco possui 3 tabelas principais:

### 📚 **livros**
```sql
id INTEGER PRIMARY KEY
titulo TEXT NOT NULL
autor TEXT NOT NULL
categoria TEXT
ano_publicacao INTEGER
disponivel BOOLEAN DEFAULT 1
```

### 👤 **usuarios**
```sql
id INTEGER PRIMARY KEY
nome TEXT NOT NULL
email TEXT UNIQUE
data_cadastro DATE
```

### 📖 **emprestimos**
```sql
id INTEGER PRIMARY KEY
usuario_id INTEGER → REFERENCES usuarios(id)
livro_id INTEGER → REFERENCES livros(id)
data_emprestimo DATE
data_devolucao DATE (NULL = ainda não devolvido)
```

### 🔗 Relacionamentos
- Um usuário pode ter vários empréstimos
- Um livro pode ser emprestado várias vezes
- `disponivel = 0` significa que o livro está emprestado

### 📊 Dados de Exemplo
```
Usuários: João Silva, Maria Santos, Pedro Costa
Livros: Clean Code, O Alquimista, Estruturas de Dados, 1984, Python para Iniciantes
Empréstimos: 4 registros (2 ativos, 2 devolvidos)
```

## ✏️ Exercícios

Edite o arquivo `solucao/consultas.sql` e complete os 4 exercícios:

### **Exercício 1: Livros Disponíveis**
Listar todos os livros disponíveis ordenados por título

### **Exercício 2: Empréstimos Ativos**
Mostrar empréstimos não devolvidos com nome do usuário e título do livro

### **Exercício 3: Livros por Usuário**
Contar quantos livros cada usuário já pegou emprestado

### **Exercício 4: Usuários Inativos**
Encontrar usuários que nunca fizeram empréstimos

## 🧪 Como Testar

### Executar Testes Automatizados
```bash
# No diretório raiz do projeto
py 01-sql/tests/test_queries.py
```

### Interpretar Resultados
- ✅ **SUCESSO**: Consulta correta
- ❌ **ERRO**: Problema na consulta (sintaxe, lógica ou resultado incorreto)
- 🎯 **Meta**: 4/4 exercícios corretos



**⏱️ Tempo estimado:** 30-45 minutos