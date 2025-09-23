# 01-sql/tests/test_queries.py - Testes robustos para validação SQL
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

        # Dados esperados: livros com disponivel = 1, ordenados por título
        expected_data = [
            {'titulo': '1984', 'autor': 'George Orwell'},
            {'titulo': 'Clean Code', 'autor': 'Robert Martin'},
            {'titulo': 'Estruturas de Dados', 'autor': 'Thomas Cormen'}
        ]

        if len(result) != 3:
            print(f"ERRO: Esperado 3 livros, recebido {len(result)}")
            conn.close()
            return False

        # Validar cada registro retornado
        for i, expected in enumerate(expected_data):
            row = result[i]
            row_str = ' '.join(str(item) for item in row)

            # Verificar se o título esperado está presente
            if expected['titulo'] not in row_str:
                print(f"ERRO: Livro '{expected['titulo']}' não encontrado na posição {i+1}")
                print(f"Linha recebida: {row}")
                conn.close()
                return False

            # Verificar se o autor correspondente também está presente
            if expected['autor'] not in row_str:
                print(f"ERRO: Autor '{expected['autor']}' não encontrado para o livro '{expected['titulo']}'")
                print(f"Linha recebida: {row}")
                conn.close()
                return False

        print("SUCESSO: Exercício 1 correto")
        conn.close()
        return True

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

        # Dados esperados: empréstimos com data_devolucao = NULL
        expected_combinations = [
            {'usuario': 'Maria Santos', 'livro': 'Python para Iniciantes'},
            {'usuario': 'Pedro Costa', 'livro': 'Estruturas de Dados'}
        ]

        if len(result) != 2:
            print(f"ERRO: Esperado 2 empréstimos ativos, recebido {len(result)}")
            conn.close()
            return False

        # Verificar se cada combinação esperada está presente
        found_combinations = []
        for row in result:
            row_str = ' '.join(str(item) for item in row)

            for expected in expected_combinations:
                if expected['usuario'] in row_str and expected['livro'] in row_str:
                    found_combinations.append(expected)
                    break

        if len(found_combinations) != 2:
            print(f"ERRO: Nem todas as combinações usuário-livro foram encontradas")
            print(f"Esperado: {expected_combinations}")
            print(f"Resultado: {result}")
            conn.close()
            return False

        # Verificar se são exatamente as combinações esperadas
        for expected in expected_combinations:
            if expected not in found_combinations:
                print(f"ERRO: Combinação {expected} não encontrada")
                conn.close()
                return False

        print("SUCESSO: Exercício 2 correto")
        conn.close()
        return True

    except Exception as e:
        print(f"ERRO: Erro na consulta - {e}")
        conn.close()
        return False

def test_exercicio_3():
    """Teste: Contar quantos livros cada usuário já pegou emprestado"""
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

        # Dados esperados: contagem de empréstimos por usuário
        expected_counts = {
            'João Silva': 2,    # 2 empréstimos
            'Maria Santos': 1,   # 1 empréstimo
            'Pedro Costa': 1     # 1 empréstimo
        }

        if len(result) != 3:
            print(f"ERRO: Esperado 3 usuários, recebido {len(result)}")
            conn.close()
            return False

        # Verificar cada usuário e sua contagem
        found_counts = {}
        for row in result:
            row_str = ' '.join(str(item) for item in row)

            # Encontrar qual usuário está nesta linha
            usuario_found = None
            for usuario in expected_counts.keys():
                if usuario in row_str:
                    usuario_found = usuario
                    break

            if not usuario_found:
                print(f"ERRO: Usuário não identificado na linha: {row}")
                conn.close()
                return False

            # Encontrar a contagem na linha
            count_found = None
            for item in row:
                if isinstance(item, int) and item > 0:
                    count_found = item
                    break

            if count_found is None:
                print(f"ERRO: Contagem não encontrada para usuário {usuario_found}")
                print(f"Linha: {row}")
                conn.close()
                return False

            found_counts[usuario_found] = count_found

        # Verificar se as contagens estão corretas
        for usuario, expected_count in expected_counts.items():
            if usuario not in found_counts:
                print(f"ERRO: Usuário {usuario} não encontrado nos resultados")
                conn.close()
                return False

            if found_counts[usuario] != expected_count:
                print(f"ERRO: {usuario} deveria ter {expected_count} empréstimos, encontrado {found_counts[usuario]}")
                conn.close()
                return False

        print("SUCESSO: Exercício 3 correto")
        conn.close()
        return True

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

        # Com os dados atuais, todos os usuários fizeram empréstimos
        # Portanto, a consulta deve retornar 0 registros
        if len(result) == 0:
            print("SUCESSO: Exercício 4 correto")
            conn.close()
            return True
        else:
            print(f"ERRO: Não deveria retornar registros (todos os usuários fizeram empréstimos)")
            print(f"Registros encontrados: {result}")
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