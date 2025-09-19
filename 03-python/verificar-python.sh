#!/bin/bash
echo "Verificando implementacao Python..."

cd 03-python/tests

echo "Executando testes detalhados..."

py -m pytest test_analise.py -v --tb=short

TEST_RESULT=$?

if [ $TEST_RESULT -eq 0 ]; then
    echo "Todos os testes Python passaram!"
    echo "Implementacao esta correta"
else
    echo "Alguns testes falharam"
    echo "Revise a implementacao das funcoes"
fi

echo ""
echo "Testando manualmente algumas funcoes..."

cd ../..

# Teste manual sem emojis
py << 'PYTHON_EOF'
import sys
import os
sys.path.insert(0, os.path.join('03-python', 'solucao'))

try:
    import analise_vendas
    print("Modulo importado com sucesso")
    
    funcoes = ['ler_dados', 'vendas_por_vendedor', 'produto_mais_vendido']
    for func in funcoes:
        if hasattr(analise_vendas, func):
            print(f"Funcao {func} encontrada")
        else:
            print(f"Funcao {func} NAO encontrada")
            
except Exception as e:
    print(f"Erro na importacao: {e}")
PYTHON_EOF

echo "Verificacao Python concluida!"
