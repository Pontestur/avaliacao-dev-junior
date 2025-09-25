# Avaliação Técnica - Desenvolvedor Fullstack Junior

## 🎯 Objetivo
Avaliar conhecimentos em SQL, C#, Python e Angular através de exercícios práticos.

## 📋 Pré-requisitos

### Software Obrigatório:
1. **Visual Studio Code** - [Download aqui](https://code.visualstudio.com/)
2. **Git for Windows** - [Download aqui](https://git-scm.com/download/win)
3. **.NET 9.0 SDK** - [Download aqui](https://dotnet.microsoft.com/download)
4. **Python 3.7+** - [Download aqui](https://python.org/downloads) ⚠️ Marcar "Add to PATH"
5. **Node.js 18+** - [Download aqui](https://nodejs.org) (inclui npm)

### Comandos pós-instalação:
```cmd
# Verificar instalações
git --version
dotnet --version
python --version  # ou py --version no Windows
node --version
npm --version
```

## 🚀 Setup Automático

**Execute uma única vez para configurar todo o ambiente:**

Execute no terminal:
```
./setup.sh
```

O script irá:
- ✅ Verificar todas as dependências necessárias
- ✅ Criar banco SQLite com dados de teste
- ✅ Configurar projetos C# com testes
- ✅ Instalar dependências Python (pandas, pytest)
- ✅ Criar projeto Angular com dependências
- ✅ Inicializar repositório Git

**Para verificar se tudo está funcionando:**
Execute no terminal:
```
./run-tests.sh
```

## 📋 O Que Você Precisa Implementar

### 1️⃣ SQL (30 min) - `01-sql/solucao/consultas.sql`
**Sistema de Biblioteca**
- ✏️ **4 consultas SQL** sobre livros, usuários e empréstimos
- 📊 Consultas com JOIN, GROUP BY, filtros e ordenação
- 🗄️ Banco SQLite com dados de teste já criado

**Para testar:**
Execute no terminal:
```
cd 01-sql/tests && python test_queries.py
```

### 2️⃣ C# (45 min) - Classes em `02-csharp/AvaliationApp/`
**Sistema de Estoque**
- ✏️ Implementar métodos em `Produto.cs` e `EstoqueManager.cs`
- 🔧 Validações, LINQ, lógica de negócio e tratamento de erros
- 🧪 **19 testes** para validar implementação

**Para testar:**
Execute no terminal:
```
cd 02-csharp && dotnet test
```

### 3️⃣ Python (35 min) - `03-python/solucao/analise_vendas.py`
**Análise de Dados de Vendas**
- ✏️ **6 funções** de análise com pandas
- 📊 Manipulação de DataFrame, agrupamentos, filtros
- 📁 CSV com dados de vendas já criado

**Para testar:**
Execute no terminal:
```
cd 03-python/tests && python -m pytest test_analise.py -v
```

### 4️⃣ Angular (60 min) - `04-angular/tarefas-app/src/app/`
**Lista de Tarefas**
- ✏️ Implementar CRUD de tarefas no componente principal
- 🔄 Data binding, eventos, diretivas estruturais
- 🎨 Interface responsiva e funcional

**Para testar:**
Execute no terminal:
```
cd 04-angular/tarefas-app && ng serve
```
**Abrir:** `http://localhost:4200`

## ⏰ Tempo Total Estimado: ~3 horas

## 📁 Estrutura do Projeto

```
avaliacao-dev-junior/
├── 01-sql/
│   ├── database.db          # Banco SQLite (criado pelo setup)
│   ├── solucao/
│   │   └── consultas.sql    # 👈 IMPLEMENTAR AQUI
│   └── tests/
├── 02-csharp/
│   ├── AvaliationApp/
│   │   ├── Produto.cs       # 👈 IMPLEMENTAR AQUI
│   │   └── EstoqueManager.cs # 👈 IMPLEMENTAR AQUI
│   └── AvaliationApp.Tests/ # Testes (19 testes)
├── 03-python/
│   ├── vendas.csv           # Dados de teste (criado pelo setup)
│   ├── solucao/
│   │   └── analise_vendas.py # 👈 IMPLEMENTAR AQUI
│   └── tests/
├── 04-angular/
│   └── tarefas-app/         # Projeto Angular (criado pelo setup)
│       └── src/app/
│           ├── app.component.ts  # 👈 IMPLEMENTAR AQUI
│           └── app.component.html # 👈 IMPLEMENTAR AQUI
├── setup.sh                # Script de configuração
├── run-tests.sh            # Script de verificação
└── README.md               # Este arquivo
```

## 🧪 Comandos de Teste por Tecnologia

Execute no terminal:
```
# Testar tudo de uma vez
./run-tests.sh

# Testar individualmente:

# SQL
cd 01-sql/tests && python test_queries.py

# C#
cd 02-csharp && dotnet test --verbosity minimal

# Python
cd 03-python/tests && python -m pytest test_analise.py -v

# Angular (build apenas - sem testes unitários específicos)
cd 04-angular/tarefas-app && ng build
```

## 💡 Extensões Recomendadas do VS Code

### Essenciais:
- **SQLite** (alexcvzz.vscode-sqlite) - *Para visualizar banco de dados*
- **C# Dev Kit** (Microsoft) - *Para C#*
- **Python** (Microsoft) - *Para Python*
- **Angular Language Service** (Angular) - *Para Angular*


## 🆘 Problemas Comuns

### ❌ Setup falhou
Execute no terminal:
```
# Reconfigurar tudo
rm .setup_done && ./setup.sh
```

### ❌ Erro de versão do .NET
Execute no terminal:
```
dotnet --version  # Deve ser 9.0.x
```

### ❌ Python não encontrado no Windows
```cmd
# Tentar com 'py' ao invés de 'python'
py --version
py -m pip install pandas pytest
```

### ❌ Angular CLI não instalado
Execute no terminal:
```
npm install -g @angular/cli
ng version
```

### 💡 Abrindo projetos no VS Code
Execute no terminal:
```
# Projeto específico
code 02-csharp
code 03-python
code 04-angular/tarefas-app

# Pasta raiz (recomendado)
code .
```

## 📚 Links de Referência

- [.NET Documentation](https://docs.microsoft.com/dotnet/)
- [Python Documentation](https://docs.python.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Angular Documentation](https://angular.io/docs)
- [SQLite Tutorial](https://www.sqlite.org/lang.html)

## ✅ Critérios de Avaliação

### SQL (25%)
- ✅ Sintaxe correta e consultas funcionais
- ✅ Uso adequado de JOIN, GROUP BY, WHERE
- ✅ Resultados corretos conforme especificação

### C# (25%)
- ✅ Implementação completa dos métodos
- ✅ Validações e tratamento de erros
- ✅ Uso adequado de LINQ e POO

### Python (25%)
- ✅ Funções implementadas corretamente
- ✅ Uso adequado do pandas
- ✅ Manipulação correta de DataFrames

### Angular (25%)
- ✅ CRUD funcional completo
- ✅ Interface responsiva e usável
- ✅ Uso correto de TypeScript e Angular

---

## 🎯 **Começar Agora**

1. **Execute:** `./setup.sh` (uma única vez)
2. **Verifique:** `./run-tests.sh`
3. **Implemente:** seguindo a estrutura acima
4. **Teste:** conforme avança nas implementações

**Boa sorte! 🚀**