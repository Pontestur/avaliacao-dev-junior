#!/bin/bash
# run-tests.sh - Executa todos os testes da avaliação

echo "🧪 Executando todos os testes..."

# Função para colorir output
red='\033[0;31m'
green='\033[0;32m'
yellow='\033[1;33m'
nc='\033[0m' # No Color

# 1. Testes SQL
echo -e "\n${yellow}📊 Testando SQL...${nc}"
cd 01-sql/tests
py test_queries.py
sql_result=$?
cd ../..

# 2. Testes C#
echo -e "\n${yellow}⚙️ Testando C#...${nc}"
cd 02-csharp/AvaliationApp.Tests
dotnet test --verbosity minimal
csharp_result=$?
cd ../..

# 3. Testes Python
echo -e "\n${yellow}🐍 Testando Python...${nc}"
cd 03-python/tests
py -m pytest test_analise.py -v
python_result=$?
cd ../..

# 4. Testes Angular
echo -e "\n${yellow}🅰️ Testando Angular...${nc}"
cd 04-angular/tarefas-app
ng test --watch=false --browsers=ChromeHeadless > /dev/null 2>&1
angular_result=$?
cd ../..

# Resultado final
echo -e "\n📋 RELATÓRIO DE TESTES:"
echo "=========================="

if [ $sql_result -eq 0 ]; then
    echo -e "SQL: ${green}✅ PASSOU${nc}"
else
    echo -e "SQL: ${red}❌ FALHOU${nc}"
fi

if [ $csharp_result -eq 0 ]; then
    echo -e "C#: ${green}✅ PASSOU${nc}"
else
    echo -e "C#: ${red}❌ FALHOU${nc}"
fi

if [ $python_result -eq 0 ]; then
    echo -e "Python: ${green}✅ PASSOU${nc}"
else
    echo -e "Python: ${red}❌ FALHOU${nc}"
fi

if [ $angular_result -eq 0 ]; then
    echo -e "Angular: ${green}✅ PASSOU${nc}"
else
    echo -e "Angular: ${red}❌ FALHOU${nc}"
fi

# Calcular pontuação total
total_passed=$(( (sql_result == 0) + (csharp_result == 0) + (python_result == 0) + (angular_result == 0) ))
echo -e "\n🏆 Tecnologias funcionando: ${total_passed}/4"

if [ $total_passed -eq 4 ]; then
    echo -e "${green}🎉 Ambiente pronto para avaliação!${nc}"
else
    echo -e "${red}⚠️ Corrigir problemas antes de iniciar${nc}"
fi