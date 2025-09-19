#!/bin/bash
# final-fix.sh - Versão final corrigida

echo "Corrigindo problemas finais..."

# 1. Instalar pandas e pytest (comando direto)
echo "Instalando dependencias Python..."
py -m pip install pandas pytest

# 2. Verificar se banco SQLite tem dados
echo "Verificando banco SQLite..."
sqlite3 01-sql/database.db "SELECT COUNT(*) FROM usuarios;" > temp_count.txt 2>/dev/null
if grep -q "3" temp_count.txt; then
    echo "Banco SQLite: OK"
else
    echo "Recriando banco SQLite..."
    
    # Recriar banco sem emojis
    cat > temp_create_simple.py << 'EOF'
import sqlite3

conn = sqlite3.connect('01-sql/database.db')
cursor = conn.cursor()

# Criar tabelas
cursor.execute('DROP TABLE IF EXISTS emprestimos;')
cursor.execute('DROP TABLE IF EXISTS livros;')
cursor.execute('DROP TABLE IF EXISTS usuarios;')

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

print('Banco criado com sucesso')
EOF

    py temp_create_simple.py
    rm temp_create_simple.py
fi

rm -f temp_count.txt

# 3. Teste final completo
echo ""
echo "TESTE FINAL COMPLETO:"
echo "===================="

# SQLite
echo -n "SQLite: "
if sqlite3 01-sql/database.db "SELECT COUNT(*) FROM usuarios;" 2>/dev/null | grep -q "3"; then
    echo "OK"
    sqlite3 01-sql/database.db "SELECT COUNT(*) as usuarios, (SELECT COUNT(*) FROM livros) as livros, (SELECT COUNT(*) FROM emprestimos) as emprestimos FROM usuarios;"
else
    echo "PROBLEMA"
fi

# Python + Pandas
echo -n "Python + Pandas: "
if py -c "import pandas as pd; print('Versao:', pd.__version__)" 2>/dev/null; then
    echo "OK"
else
    echo "PROBLEMA - Executar: py -m pip install pandas"
fi

# Python + Pytest
echo -n "Python + Pytest: "
if py -c "import pytest; print('Versao:', pytest.__version__)" 2>/dev/null; then
    echo "OK"
else
    echo "PROBLEMA - Executar: py -m pip install pytest"
fi

# C#
echo -n "C#: "
if dotnet build 02-csharp/AvaliationApp/AvaliationApp.csproj > /dev/null 2>&1; then
    echo "OK"
else
    echo "PROBLEMA"
fi

# Angular
echo -n "Angular: "
if [ -f "04-angular/tarefas-app/package.json" ] && [ -d "04-angular/tarefas-app/node_modules" ]; then
    echo "OK"
else
    echo "PROBLEMA - Executar: cd 04-angular/tarefas-app && npm install"
fi

# Git
echo -n "Git: "
if [ -d ".git" ]; then
    echo "OK"
else
    echo "Inicializando..."
    git init
    echo "OK"
fi

echo ""
echo "RESUMO:"
echo "======"
echo "- SQLite: Banco com usuarios, livros e emprestimos"
echo "- Python: Versao $(py --version 2>/dev/null || echo 'N/A')"
echo "- C#: .NET $(dotnet --version 2>/dev/null || echo 'N/A')"
echo "- Angular: Projeto criado"
echo "- Git: Repositorio inicializado"

echo ""
echo "Proximo passo: bash run-tests.sh"