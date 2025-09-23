# Avaliação Técnica - Desenvolvedor Fullstack Junior

## 🎯 Objetivo
Avaliar conhecimentos em Git, SQL, C#, Python e Angular através de exercícios práticos.

## 📋 Pré-requisitos (Windows + Visual Studio Code)

### Software Obrigatório:

1. **Visual Studio Code** - [Download aqui](https://code.visualstudio.com/)
2. **Git for Windows** - [Download aqui](https://git-scm.com/download/win)
3. **.NET 9.0 SDK** - [Download aqui](https://dotnet.microsoft.com/download)
4. **Python 3.7+** - [Download aqui](https://python.org/downloads) ⚠️ Marcar "Add to PATH"
5. **Node.js 18+** - [Download aqui](https://nodejs.org) (inclui npm)

### Comandos pós-instalação:
```cmd
# Instalar Angular CLI
npm install -g @angular/cli

# Verificar instalações
git --version
dotnet --version
python --version
node --version
npm --version
ng version
```

### Extensões Recomendadas do VS Code:

#### Para SQL:
- **SQLite** (alexcvzz.vscode-sqlite) - *Obrigatória para Parte 1*

#### Para C#:
- **C# Dev Kit** (Microsoft)
- **.NET Install Tool** (Microsoft)

#### Para Python:
- **Python** (Microsoft)
- **Pylance** (Microsoft)

#### Para Angular:
- **Angular Language Service** (Angular)
- **TypeScript Importer** (pmneo)

#### Geral:
- **GitLens** (Eric Amodio)
- **Auto Rename Tag** (Jun Han)

## ✅ Verificar Instalação

Abra o **Terminal** no VS Code (`Ctrl + '`) e execute:

## 🚀 Como Executar Cada Parte

### 1️⃣ SQL (Parte 1)

**O que fazer:**
- Completar **4 consultas SQL** no arquivo `01-sql/solucao/consultas.sql`
- Usar extensão **SQLite** do VS Code para testar consultas
- Banco de dados: sistema de biblioteca (livros, usuários, empréstimos)

**Comandos:**
```cmd
cd 01-sql
pip install -r requirements.txt
pytest tests/ -v
```

**Extensão obrigatória no VS Code:**
- **SQLite** (alexcvzz.vscode-sqlite) - para visualizar dados e testar consultas

### 2️⃣ C# (Parte 2)

**O que fazer:**
- Implementar métodos em classes `Produto.cs` e `EstoqueManager.cs`
- Conceitos: POO, LINQ, manipulação de listas, validações

**Comandos:**
```cmd
cd 02-csharp
dotnet restore
dotnet build
dotnet test --logger console
```

### 3️⃣ Python (Parte 3)

**O que fazer:**
- Implementar **6 funções** de análise de dados com pandas
- Arquivo: `03-python/solucao/analise_vendas.py`
- Conceitos: manipulação de DataFrames, agregações, filtros

**Comandos:**
```cmd
cd 03-python
pip install -r requirements.txt
cd solucao
python analise_vendas.py
cd ..
pytest tests/ -v
```

### 4️⃣ Angular (Parte 4)

**O que fazer:**
- Implementar **Lista de Tarefas** no componente principal
- Arquivo: `04-angular/tarefas-app/src/app/app.component.ts` e `.html`
- Conceitos: data binding, eventos, diretivas, services

**Comandos:**
```cmd
cd 04-angular\tarefas-app
npm install
ng serve
```
**Abrir navegador em:** `http://localhost:4200`

## ⏰ Tempo Estimado por Exercício
- **SQL**: 30 minutos
- **C#**: 45 minutos
- **Python**: 35 minutos
- **Angular**: 60 minutos

**Total: ~3 horas**

## 🧪 Executar Testes

### No Terminal do VS Code (`Ctrl + '`):

```cmd
# SQL
cd 01-sql
pytest tests/ -v

# C#
cd 02-csharp
dotnet test --logger console

# Python
cd 03-python
pytest tests/ -v

# Angular (opcional - testes unitários)
cd 04-angular\tarefas-app
ng test --watch=false --browsers=ChromeHeadless
```

## 📁 Estrutura do Projeto

```
avaliacao-dev-junior/
├── 01-sql/           # Exercícios de consultas SQL
├── 02-csharp/        # Exercícios de C# (.NET 9.0)
├── 03-python/        # Exercícios de análise de dados Python
├── 04-angular/       # Exercícios de frontend Angular
└── README.md         # Este arquivo
```

## 📚 Links Úteis

- [Documentação .NET](https://docs.microsoft.com/dotnet/)
- [Documentação Python](https://docs.python.org/)
- [Documentação Angular](https://angular.io/docs)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

## 🆘 Problemas Comuns

### Erro de versão do .NET
```bash
# Verificar versão instalada
dotnet --version
# Deve ser 9.0.x
```

### Erro de módulos Python não encontrados
```cmd
# Instalar dependências
pip install -r requirements.txt

# Ou usar ambiente virtual (recomendado)
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Erro no Angular CLI
```cmd
# Instalar Angular CLI globalmente
npm install -g @angular/cli
# Verificar instalação
ng version
```

### Abrindo projetos no VS Code
```cmd
# Abrir pasta específica
code 02-csharp
code 03-python
code 04-angular\tarefas-app

# Ou abrir pasta atual
code .
```

---

**Boa sorte com a avaliação! 🚀**
