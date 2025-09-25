#!/bin/bash
# setup.sh - Script completo para configurar o ambiente de avaliação

echo "🚀 Configurando ambiente de avaliação..."
echo "========================================"

# Verificar se já existe setup
if [ -f ".setup_done" ]; then
    echo "⚠️  Setup já foi executado anteriormente."
    echo "Para recriar, delete o arquivo '.setup_done' e execute novamente."
    exit 0
fi

# Função para verificar comandos
check_command() {
    if command -v "$1" >/dev/null 2>&1; then
        echo "✅ $1 encontrado"
        return 0
    else
        echo "❌ $1 não encontrado"
        return 1
    fi
}

# Verificar dependências
echo ""
echo "🔍 Verificando dependências..."
echo "=============================="

MISSING_DEPS=false

if ! check_command "dotnet"; then
    echo "   Instale o .NET SDK: https://dotnet.microsoft.com/download"
    MISSING_DEPS=true
fi

if ! check_command "python" && ! check_command "py"; then
    echo "   Instale Python: https://python.org/downloads"
    MISSING_DEPS=true
fi

if ! check_command "node"; then
    echo "   Instale Node.js: https://nodejs.org"
    MISSING_DEPS=true
fi

if ! check_command "sqlite3"; then
    echo "⚠️  sqlite3 não encontrado (não é obrigatório - usaremos Python para criar o banco)"
fi

if ! check_command "git"; then
    echo "   Instale Git: https://git-scm.com/download"
    MISSING_DEPS=true
fi

if [ "$MISSING_DEPS" = true ]; then
    echo ""
    echo "❌ Dependências em falta. Instale-as e execute o setup novamente."
    exit 1
fi

# Detectar comando Python
if command -v py >/dev/null 2>&1; then
    PYTHON_CMD="py"
else
    PYTHON_CMD="python"
fi

echo ""
echo "📁 Criando estrutura de pastas..."
echo "================================="

# Criar estrutura que ainda não existe
mkdir -p 01-sql/tests 2>/dev/null
mkdir -p 03-python/tests 2>/dev/null

# 1. Setup SQLite Database
echo ""
echo "🗄️ Configurando banco SQLite..."
echo "==============================="

# Criar banco usando Python para melhor compatibilidade
cat > temp_create_db.py << 'EOF'
import sqlite3
import os

# Garantir que diretório existe
os.makedirs('01-sql', exist_ok=True)

conn = sqlite3.connect('01-sql/database.db')
cursor = conn.cursor()

# Remover tabelas se existirem
cursor.execute('DROP TABLE IF EXISTS emprestimos;')
cursor.execute('DROP TABLE IF EXISTS livros;')
cursor.execute('DROP TABLE IF EXISTS usuarios;')

# Criar tabelas
cursor.execute('''
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT UNIQUE,
    data_cadastro DATE
);
''')

cursor.execute('''
CREATE TABLE livros (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    categoria TEXT,
    ano_publicacao INTEGER,
    disponivel BOOLEAN DEFAULT 1
);
''')

cursor.execute('''
CREATE TABLE emprestimos (
    id INTEGER PRIMARY KEY,
    usuario_id INTEGER,
    livro_id INTEGER,
    data_emprestimo DATE,
    data_devolucao DATE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (livro_id) REFERENCES livros(id)
);
''')

# Dados de teste
usuarios = [
    ('João Silva', 'joao@email.com', '2024-01-15'),
    ('Maria Santos', 'maria@email.com', '2024-02-20'),
    ('Pedro Costa', 'pedro@email.com', '2024-03-10')
]

livros = [
    ('Clean Code', 'Robert Martin', 'Tecnologia', 2008, 1),
    ('O Alquimista', 'Paulo Coelho', 'Ficção', 1988, 0),
    ('Estruturas de Dados', 'Thomas Cormen', 'Tecnologia', 2009, 1),
    ('1984', 'George Orwell', 'Ficção', 1949, 1),
    ('Python para Iniciantes', 'Mark Lutz', 'Tecnologia', 2020, 0)
]

emprestimos = [
    (1, 2, '2024-08-15', '2024-08-30'),
    (2, 5, '2024-09-01', None),
    (1, 1, '2024-09-10', '2024-09-15'),
    (3, 3, '2024-09-12', None)
]

cursor.executemany('INSERT INTO usuarios VALUES (NULL, ?, ?, ?)', usuarios)
cursor.executemany('INSERT INTO livros VALUES (NULL, ?, ?, ?, ?, ?)', livros)
cursor.executemany('INSERT INTO emprestimos VALUES (NULL, ?, ?, ?, ?)', emprestimos)

conn.commit()
conn.close()

print('Banco SQLite criado com sucesso!')
EOF

$PYTHON_CMD temp_create_db.py
rm temp_create_db.py

# 2. Setup C#
echo ""
echo "⚙️ Configurando projeto C#..."
echo "============================="

if [ ! -d "02-csharp/AvaliationApp" ]; then
    cd 02-csharp

    # Criar projeto principal
    dotnet new classlib -n AvaliationApp --force
    cd AvaliationApp
    rm -f Class1.cs 2>/dev/null

    # Voltar e criar projeto de testes
    cd ..
    dotnet new xunit -n AvaliationApp.Tests --force
    cd AvaliationApp.Tests

    # Adicionar referência
    dotnet add reference ../AvaliationApp/AvaliationApp.csproj

    cd ../..
    echo "✅ Projeto C# criado!"
else
    echo "✅ Projeto C# já existe!"
fi

# 3. Setup Python
echo ""
echo "🐍 Configurando ambiente Python..."
echo "=================================="

# Criar requirements.txt
cat > 03-python/requirements.txt << 'EOF'
pandas>=2.0.0
pytest>=7.0.0
pytest-xdist>=3.0.0
EOF

# Criar dados de teste CSV
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
echo "Instalando dependências Python..."
$PYTHON_CMD -m pip install -r 03-python/requirements.txt

echo "✅ Python configurado!"

# 4. Setup Angular
echo ""
echo "🅰️ Configurando projeto Angular..."
echo "=================================="

# Sempre instalar Angular CLI globalmente (candidato precisará dos comandos ng)
if ! command -v ng >/dev/null 2>&1; then
    echo "Instalando Angular CLI globalmente..."
    npm install -g @angular/cli
    echo "✅ Angular CLI instalado!"
else
    echo "✅ Angular CLI já instalado!"
fi

# Verificar se projeto existe e instalar dependências se necessário
if [ -d "04-angular/tarefas-app" ]; then
    if [ ! -d "04-angular/tarefas-app/node_modules" ]; then
        echo "Instalando dependências do projeto Angular..."
        cd 04-angular/tarefas-app
        npm install
        cd ../..
        echo "✅ Dependências Angular instaladas!"
    else
        echo "✅ Projeto Angular já configurado!"
    fi
else
    echo "⚠️  Projeto Angular não encontrado em 04-angular/tarefas-app"
    echo "   (Será criado quando fornecido na estrutura para o candidato)"
fi

# 5. Setup Git
echo ""
echo "📝 Configurando Git..."
echo "====================="

if [ ! -d ".git" ]; then
    git init
    echo "✅ Repositório Git inicializado!"
else
    echo "✅ Repositório Git já existe!"
fi

# Criar .gitignore se não existir
if [ ! -f ".gitignore" ]; then
cat > .gitignore << 'EOF'
# .NET
bin/
obj/
*.user
*.suo
.vs/
.vscode/

# Python
__pycache__/
*.pyc
*.pyo
venv/
.pytest_cache/
*.egg-info/

# Node.js
node_modules/
dist/
.angular/
*.log

# SQLite
*.db-journal

# OS
.DS_Store
Thumbs.db

# Setup
.setup_done
EOF
fi

# 6. Teste final do ambiente
echo ""
echo "🧪 Testando ambiente..."
echo "======================"

SETUP_OK=true

# Teste SQLite
echo -n "SQLite Database: "
if [ -f "01-sql/database.db" ]; then
    echo "OK (banco criado)"
else
    echo "PROBLEMA"
    SETUP_OK=false
fi

# Teste Python + Pandas
echo -n "Python + Pandas: "
if $PYTHON_CMD -c "import pandas as pd; print('OK - Versao:', pd.__version__)" 2>/dev/null; then
    echo "OK"
else
    echo "PROBLEMA"
    SETUP_OK=false
fi

# Teste Python + Pytest
echo -n "Python + Pytest: "
if $PYTHON_CMD -c "import pytest; print('OK - Versao:', pytest.__version__)" 2>/dev/null; then
    echo "OK"
else
    echo "PROBLEMA"
    SETUP_OK=false
fi

# Teste C#
echo -n "C# Build: "
if dotnet build 02-csharp/AvaliationApp/AvaliationApp.csproj >/dev/null 2>&1; then
    echo "✅ OK"
else
    echo "❌ PROBLEMA"
    SETUP_OK=false
fi

# Teste Angular
echo -n "Angular Project: "
if [ -f "04-angular/tarefas-app/package.json" ] && [ -d "04-angular/tarefas-app/node_modules" ]; then
    echo "✅ OK"
else
    echo "❌ PROBLEMA"
    SETUP_OK=false
fi

# Marcar setup como concluído
if [ "$SETUP_OK" = true ]; then
    touch .setup_done
    echo ""
    echo "🎉 SETUP CONCLUÍDO COM SUCESSO!"
    echo "==============================="
    echo ""
    echo "📋 Resumo do ambiente:"
    echo "- SQLite: Banco com usuários, livros e empréstimos"
    echo "- Python: $(${PYTHON_CMD} --version 2>/dev/null || echo 'Versão não detectada')"
    echo "- C#: .NET $(dotnet --version 2>/dev/null || echo 'Versão não detectada')"
    echo "- Angular: Projeto tarefas-app criado"
    echo "- Git: Repositório inicializado"
    echo ""
    echo "🚀 Próximos passos:"
    echo "1. Execute: ./run-tests.sh (para verificar testes)"
    echo "2. Siga as instruções em cada pasta (01-sql/, 02-csharp/, etc.)"
    echo ""
    echo "📖 Documentação completa no README.md"
else
    echo ""
    echo "❌ SETUP FALHOU!"
    echo "Verifique os erros acima e execute novamente."
    echo "Para forçar novo setup: rm .setup_done && ./setup.sh"
    exit 1
fi