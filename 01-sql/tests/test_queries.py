# 01-sql/tests/test_queries.py - Versão com busca de chaves corrigida
import sqlite3
import os
import sys

def connect_db():
    """Conecta com o banco de dados SQLite"""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'database.db')
    db_path = os.path.normpath(db_path)
    return sqlite3.connect(db_path)

def read_sql_file():
    """Lê o arquivo de consultas do candidato"""
    tests_dir = os.path.dirname(__file__)
    sql_dir = os.path.dirname(tests_dir)
    solucao_dir = os.path.join(sql_dir, 'solucao')
    sql_file = os.path.join(solucao_dir, 'consultas.sql')
    
    print(f"Procurando arquivo SQL em: {sql_file}")
    
    if not os.path.exists(sql_file):
        print(f"Arquivo não encontrado: {sql_file}")
        return None
    
    with open(sql_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Separa as consultas por comentários
    queries = {}
    current_query = ""
    current_name = ""
    
    for line in content.split('\n'):
        line = line.strip()
        if line.startswith('-- Exercício') or line.startswith('-- EXERCÍCIO'):
            if current_name and current_query:
                queries[current_name] = current_query.strip()
            current_name = line.replace('-- ', '').lower()
            current_query = ""
        elif not line.startswith('--') and line and not line.startswith('TODO'):
            current_query += line + "\n"
    
    # Adiciona a última consulta
    if current_name and current_query:
        queries[current_name] = current_query.strip()
    
    print(f"Consultas encontradas: {list(queries.keys())}")
    return queries

def find_query(queries, exercise_num):
    """Busca consulta por número do exercício"""
    if not queries:
        return None
    
    search_key = f'exercício {exercise_num}'
    for key in queries.keys():
        if key.startswith(search_key):
            return queries[key]
    return None

def test_exercicio_1():
    """Teste: Listar livros disponíveis ordenados por título"""
    print("Testando Exercício 1: Livros disponíveis...")
    
    conn = connect_db()
    cursor = conn.cursor()
    
    queries = read_sql_file()
    query = find_query(queries, 1)
    
    if not query:
        print("ERRO: Consulta 1 não encontrada")
        conn.close()
        return False
    
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        
        # Verificações
        expected_books = ['1984', 'Clean Code', 'Estruturas de Dados']
        actual_books = [row[1] if len(row) > 1 else row[0] for row in result]
        
        if len(result) == 3 and actual_books == expected_books:
            print("SUCESSO: Exercício 1 correto")
            conn.close()
            return True
        else:
            print(f"ERRO: Esperado {expected_books}, recebido {actual_books}")
            conn.close()
            return False
            
    except Exception as e:
        print(f"ERRO: Erro na consulta - {e}")
        conn.close()
        return False

def test_exercicio_2():
    """Teste: Empréstimos ativos com joins"""
    print("Testando Exercício 2: Empréstimos ativos...")
    
    conn = connect_db()
    cursor = conn.cursor()
    
    queries = read_sql_file()
    query = find_query(queries, 2)
    
    if not query:
        print("ERRO: Consulta 2 não encontrada")
        conn.close()
        return False
    
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        
        # Deve retornar 2 empréstimos ativos
        if len(result) == 2:
            print("SUCESSO: Exercício 2 correto")
            conn.close()
            return True
        else:
            print(f"ERRO: Esperado 2 registros, recebido {len(result)}")
            conn.close()
            return False
            
    except Exception as e:
        print(f"ERRO: Erro na consulta - {e}")
        conn.close()
        return False

def test_exercicio_3():
    """Teste: Contar livros por usuário"""
    print("Testando Exercício 3: Livros por usuário...")
    
    conn = connect_db()
    cursor = conn.cursor()
    
    queries = read_sql_file()
    query = find_query(queries, 3)
    
    if not query:
        print("ERRO: Consulta 3 não encontrada")
        conn.close()
        return False
    
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        
        # Verificar se tem aggregação (GROUP BY)
        query_upper = query.upper()
        has_group_by = 'GROUP BY' in query_upper
        has_count = 'COUNT(' in query_upper
        
        if has_group_by and has_count and len(result) > 0:
            print("SUCESSO: Exercício 3 correto")
            conn.close()
            return True
        else:
            print("ERRO: Deve usar GROUP BY e COUNT")
            conn.close()
            return False
            
    except Exception as e:
        print(f"ERRO: Erro na consulta - {e}")
        conn.close()
        return False

def test_exercicio_4():
    """Teste: Usuários que nunca fizeram empréstimos"""
    print("Testando Exercício 4: Usuários sem empréstimos...")
    
    conn = connect_db()
    cursor = conn.cursor()
    
    queries = read_sql_file()
    query = find_query(queries, 4)
    
    if not query:
        print("ERRO: Consulta 4 não encontrada")
        conn.close()
        return False
    
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        
        # Não deve retornar registros (todos os usuários fizeram empréstimos)
        if len(result) == 0:
            print("SUCESSO: Exercício 4 correto")
            conn.close()
            return True
        else:
            print("ERRO: Não deveria retornar registros")
            conn.close()
            return False
            
    except Exception as e:
        print(f"ERRO: Erro na consulta - {e}")
        conn.close()
        return False

def main():
    """Executa todos os testes SQL"""
    print("=" * 50)
    print("TESTES SQL - SISTEMA DE BIBLIOTECA")
    print("=" * 50)
    
    queries = read_sql_file()
    if not queries:
        print("ERRO: Arquivo 'solucao/consultas.sql' não encontrado ou vazio!")
        print("Crie o arquivo com suas consultas SQL")
        sys.exit(1)
    
    tests = [
        test_exercicio_1,
        test_exercicio_2, 
        test_exercicio_3,
        test_exercicio_4
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"RESULTADO SQL: {passed}/4 exercícios corretos")
    print("=" * 50)
    
    # Retorna 0 se todos passaram, 1 se houve falhas
    sys.exit(0 if passed == 4 else 1)

if __name__ == "__main__":
    main()
