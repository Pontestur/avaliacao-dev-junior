#!/bin/bash
# setup.sh - Script para configurar o ambiente de avaliação

echo "🚀 Configurando ambiente de avaliação..."

# Criar estrutura de pastas
echo "📁 Criando estrutura de pastas..."
mkdir -p 01-sql/{tests,solucao}
mkdir -p 02-csharp
mkdir -p 03-python/{tests,solucao}
mkdir -p 04-angular
mkdir -p 05-git

# 1. Setup SQL
echo "🗄️ Configurando banco SQLite..."
cat > 01-sql/setup.sql << 'EOF'
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
EOF

# Criar banco SQLite
sqlite3 01-sql/database.db < 01-sql/setup.sql

# 2. Setup C#
echo "⚙️ Configurando projeto C#..."
cd 02-csharp

# Criar projeto principal
dotnet new classlib -n AvaliationApp
cd AvaliationApp

# Remover arquivo padrão e criar estrutura
rm Class1.cs

# Criar projeto de testes
cd ..
dotnet new xunit -n AvaliationApp.Tests
cd AvaliationApp.Tests

# Adicionar referência
dotnet add reference ../AvaliationApp/AvaliationApp.csproj

cd ../..

# 3. Setup Python
echo "🐍 Configurando ambiente Python..."
cat > 03-python/requirements.txt << 'EOF'
pandas==2.1.4
pytest==7.4.3
pytest-xdist==3.5.0
EOF

# Criar dados de teste
cat > 03-python/vendas.csv << 'EOF'
data,produto,categoria,quantidade,preco_unitario,vendedor
2024-01-15,Notebook Dell,Eletrônicos,2,2500.00,João Silva
2024-01-16,Mouse Gamer,Eletrônicos,5,45.00,Maria Santos
2024-01-17,Cadeira Ergonômica,Móveis,1,350.00,João Silva
2024-01-18,Monitor 24pol,Eletrônicos,3,800.00,Pedro Costa
2024-01-19,Teclado Mecânico,Eletrônicos,4,120.00,Maria Santos
2024-01-20,Mesa Escritório,Móveis,2,450.00,João Silva
2024-01-21,Headset,Eletrônicos,6,80.00,Pedro Costa
2024-01-22,Smartphone,Eletrônicos,1,1200.00,Maria Santos
2024-01-23,Tablet,Eletrônicos,2,600.00,João Silva
2024-01-24,Impressora,Eletrônicos,1,350.00,Pedro Costa
EOF

# Instalar dependências Python
pip install -r 03-python/requirements.txt

# 4. Setup Angular
echo "🅰️ Configurando projeto Angular..."
cd 04-angular
ng new tarefas-app --routing=true --style=css --skip-git=true
cd tarefas-app

# Instalar dependências de teste
npm install --save-dev @angular/testing jasmine karma
cd ../..

# 5. Criar .gitignore
echo "📝 Criando .gitignore..."
cat > .gitignore << 'EOF'
# .NET
bin/
obj/
*.user
*.suo
.vs/

# Python
__pycache__/
*.pyc
*.pyo
venv/
.pytest_cache/

# Node.js
node_modules/
dist/
.angular/

# SQLite
*.db-journal

# IDE
.vscode/settings.json
EOF

# 6. Criar README principal
cat > README.md << 'EOF'
# Avaliação Técnica - Desenvolvedor Fullstack Junior

## 🎯 Objetivo
Avaliar conhecimentos em Git, SQL, C#, Python e Angular

## 🚀 Como começar
1. Execute: `./setup.sh`
2. Execute: `./run-tests.sh` (para verificar ambiente)
3. Siga as instruções em cada pasta

## ⏰ Tempo por exercício
- Git: 15 min
- SQL: 30 min  
- C#: 45 min
- Python: 35 min
- Angular: 55 min

## 🧪 Executar testes
```bash
# Todos os testes
./run-tests.sh

# Por tecnologia
pytest 01-sql/tests/
dotnet test 02-csharp/AvaliationApp.Tests/
pytest 03-python/tests/
ng test --watch=false --browsers=ChromeHeadless
```
EOF

echo "✅ Setup concluído! Execute './run-tests.sh' para verificar o ambiente."