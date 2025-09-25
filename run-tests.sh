#!/bin/bash
# run-tests.sh - Executa todos os testes da avaliação

echo "🧪 Executando todos os testes de verificação do ambiente..."
echo "==========================================================="

# Função para colorir output
red='\033[0;31m'
green='\033[0;32m'
yellow='\033[1;33m'
nc='\033[0m' # No Color

# Detectar comando Python
if command -v py >/dev/null 2>&1; then
    PYTHON_CMD="py"
else
    PYTHON_CMD="python"
fi

# Variáveis para rastrear resultados
sql_result=1
csharp_result=1
python_result=1
angular_result=1

# 1. Testes SQL
echo -e "\n${yellow}📊 Testando SQL...${nc}"
echo "=============================="
if [ -f "01-sql/tests/test_queries.py" ] && [ -f "01-sql/database.db" ]; then
    cd 01-sql/tests
    $PYTHON_CMD test_queries.py
    sql_result=$?
    cd ../..

    if [ $sql_result -eq 0 ]; then
        echo "✅ Testes SQL: ambiente configurado corretamente"
    else
        echo "❌ Testes SQL: problemas encontrados"
    fi
else
    echo "❌ Testes SQL: arquivos não encontrados (test_queries.py ou database.db)"
    sql_result=1
fi

# 2. Testes C#
echo -e "\n${yellow}⚙️ Testando C#...${nc}"
echo "=========================="
if [ -d "02-csharp/AvaliationApp.Tests" ]; then
    cd 02-csharp
    echo "Executando build e testes C#..."
    dotnet test --verbosity minimal
    csharp_result=$?
    cd ..

    if [ $csharp_result -eq 0 ]; then
        echo "✅ Testes C#: ambiente configurado corretamente"
    else
        echo "❌ Testes C#: problemas encontrados"
    fi
else
    echo "❌ Testes C#: projeto de testes não encontrado"
    csharp_result=1
fi

# 3. Testes Python
echo -e "\n${yellow}🐍 Testando Python...${nc}"
echo "==========================="
if [ -f "03-python/tests/test_analise.py" ] && [ -f "03-python/vendas.csv" ]; then
    cd 03-python/tests
    echo "Executando testes Python..."
    $PYTHON_CMD -m pytest test_analise.py -v
    python_result=$?
    cd ../..

    if [ $python_result -eq 0 ]; then
        echo "✅ Testes Python: ambiente configurado corretamente"
    else
        echo "❌ Testes Python: problemas encontrados"
    fi
else
    echo "❌ Testes Python: arquivos não encontrados (test_analise.py ou vendas.csv)"
    python_result=1
fi

# 4. Verificação Angular (sem testes específicos - apenas verificar estrutura)
echo -e "\n${yellow}🅰️ Verificando Angular...${nc}"
echo "=============================="
if [ -f "04-angular/tarefas-app/package.json" ] && [ -d "04-angular/tarefas-app/node_modules" ]; then
    cd 04-angular/tarefas-app
    echo "Verificando build do Angular..."

    # Tentar um build rápido para verificar se está tudo OK
    if ng build --configuration production --output-path=dist-test > /dev/null 2>&1; then
        echo "✅ Build Angular: sucesso"
        angular_result=0
        # Limpar diretório de teste
        rm -rf dist-test 2>/dev/null
    else
        echo "❌ Build Angular: falhou"
        angular_result=1
    fi
    cd ../..
else
    echo "❌ Angular: projeto não encontrado ou dependências não instaladas"
    angular_result=1
fi

# Resultado final
echo -e "\n📋 RELATÓRIO FINAL DOS TESTES:"
echo "====================================="

if [ $sql_result -eq 0 ]; then
    echo -e "SQL: ${green}✅ FUNCIONANDO${nc} (banco + testes encontrados)"
else
    echo -e "SQL: ${red}❌ PROBLEMA${nc} (verificar database.db e test_queries.py)"
fi

if [ $csharp_result -eq 0 ]; then
    echo -e "C#: ${green}✅ FUNCIONANDO${nc} (build + testes executados)"
else
    echo -e "C#: ${red}❌ PROBLEMA${nc} (verificar .NET SDK ou código)"
fi

if [ $python_result -eq 0 ]; then
    echo -e "Python: ${green}✅ FUNCIONANDO${nc} (pandas + pytest funcionais)"
else
    echo -e "Python: ${red}❌ PROBLEMA${nc} (verificar pandas ou test_analise.py)"
fi

if [ $angular_result -eq 0 ]; then
    echo -e "Angular: ${green}✅ FUNCIONANDO${nc} (projeto + dependências OK)"
else
    echo -e "Angular: ${red}❌ PROBLEMA${nc} (verificar Node.js ou dependências)"
fi

# Calcular pontuação total
total_passed=$(( (sql_result == 0) + (csharp_result == 0) + (python_result == 0) + (angular_result == 0) ))

echo ""
echo "🏆 Tecnologias funcionando: ${total_passed}/4"

if [ $total_passed -eq 4 ]; then
    echo -e "${green}🎉 AMBIENTE TOTALMENTE FUNCIONAL!${nc}"
    echo -e "${green}   Candidatos podem iniciar a avaliação.${nc}"
    echo ""
    echo "📖 Próximos passos:"
    echo "   1. Consultar README.md para instruções"
    echo "   2. Navegar para cada pasta (01-sql, 02-csharp, 03-python, 04-angular)"
    echo "   3. Seguir as instruções específicas de cada exercício"
elif [ $total_passed -ge 2 ]; then
    echo -e "${yellow}⚠️  AMBIENTE PARCIALMENTE FUNCIONAL${nc}"
    echo -e "${yellow}   Corrigir problemas antes de iniciar avaliação.${nc}"
else
    echo -e "${red}❌ MUITOS PROBLEMAS ENCONTRADOS${nc}"
    echo -e "${red}   Execute './setup.sh' novamente para reconfigurar.${nc}"
fi

echo ""
echo "Para reconfigurar completamente: rm .setup_done && ./setup.sh"