# Avaliação Técnica - Parte 3: Python

## Visão Geral
Nesta etapa da avaliação, você trabalhará com análise de dados em Python usando pandas. Sua tarefa é implementar funções para análise de vendas a partir de um arquivo CSV, demonstrando conhecimento em manipulação de dados, agregações e filtros.

## Estrutura do Projeto
```
03-python/
├── vendas.csv                    # Arquivo de dados de vendas
├── requirements.txt              # Dependências do projeto
├── solucao/
│   └── analise_vendas.py        # Arquivo principal - IMPLEMENTAR AQUI
├── tests/
│   └── test_analise.py          # Testes automatizados
```

## Tecnologias Utilizadas
- **Python 3.7+** - Linguagem de programação
- **Pandas 2.1.4** - Manipulação e análise de dados
- **pytest 7.4.3** - Framework de testes

## Dados de Exemplo
O arquivo `vendas.csv` contém dados com as seguintes colunas:
```csv
data,produto,categoria,quantidade,preco_unitario,vendedor
2024-01-15,Notebook Dell,Eletrônicos,2,2500.00,João Silva
2024-01-16,Mouse Gamer,Eletrônicos,5,45.00,Maria Santos
2024-01-17,Cadeira Ergonômica,Móveis,1,350.00,João Silva
```

### Estrutura dos Dados
- **data**: Data da venda (formato YYYY-MM-DD)
- **produto**: Nome do produto vendido
- **categoria**: Categoria do produto (Eletrônicos, Móveis, etc.)
- **quantidade**: Quantidade vendida
- **preco_unitario**: Preço unitário do produto
- **vendedor**: Nome do vendedor

## Tarefas a Implementar

Implemente as 6 funções marcadas com `TODO` no arquivo `solucao/analise_vendas.py`:

### 1. `ler_dados(caminho_arquivo=None)`
- Carrega os dados do arquivo CSV
- Usa o arquivo `vendas.csv` na pasta raiz do projeto
- Retorna um DataFrame pandas com as colunas corretas

### 2. `exibir_primeiras_linhas(df, n=5)`
- Retorna as primeiras N linhas do DataFrame
- Retorna um DataFrame com as N primeiras linhas

### 3. `vendas_por_vendedor(df)`
- Calcula o total de vendas por vendedor (quantidade * preço unitário)
- Retorna Series ou dict com vendedor → total de vendas
- **Exemplo resultado**: `{'João Silva': 4850.0, 'Maria Santos': 1865.0}`

### 4. `produto_mais_vendido(df)`
- Identifica o produto com maior quantidade total vendida
- Retorna o nome do produto (string)

### 5. `categoria_maior_faturamento(df)`
- Identifica a categoria com maior faturamento total
- Retorna o nome da categoria (string)

### 6. `filtrar_por_periodo(df, data_inicio, data_fim)`
- Filtra vendas por período específico
- Parâmetros: datas no formato 'YYYY-MM-DD'
- Retorna DataFrame filtrado

## Função Main()

A função `main()` já está implementada e serve para testar suas funções. Ela:
- Testa cada função em sequência
- Mostra se cada função está `[OK]` ou `[PENDENTE]`
- Exibe os resultados quando as funções estão implementadas
- Não quebra se alguma função não estiver implementada

Execute no terminal: `py analise_vendas.py` para ver quais funções ainda precisam ser implementadas.

## Como Executar

### Pré-requisitos
- Python 3.7 ou superior instalado
- pip (gerenciador de pacotes Python)

### Comandos para Execução

1. **Navegar para o diretório:**
   Execute no terminal:
   ```
   cd 03-python
   ```

2. **Instalar dependências:**
   Execute no terminal:
   ```
   pip install -r requirements.txt
   # ou no Windows:
   py -m pip install -r requirements.txt
   ```

3. **Executar os testes:**
   Execute no terminal:
   ```
   pytest tests/test_analise.py -v
   # ou no Windows:
   py -m pytest tests/test_analise.py -v
   ```

4. **Executar testes específicos:**
   Execute no terminal:
   ```
   # Testar função específica
   pytest tests/test_analise.py::TestFuncaoLerDados -v
   pytest tests/test_analise.py::TestFuncaoVendasPorVendedor -v

   # Testar um teste específico
   pytest tests/test_analise.py::TestFuncaoVendasPorVendedor::test_vendas_por_vendedor_calculo -v
   ```

5. **Executar seu código:**
   Execute no terminal:
   ```
   cd solucao
   py analise_vendas.py
   ```


### Debugging e Desenvolvimento

#### Visual Studio Code
1. Instale a extensão **Python** da Microsoft
2. Configure o interpretador Python: `Ctrl+Shift+P` → "Python: Select Interpreter"
3. Para debuggar:
   - Abra `analise_vendas.py`
   - Defina breakpoints clicando na margem esquerda
   - Pressione `F5` para executar com debug


## Critérios de Avaliação

### Funcionalidade (100 pontos)
- ✅ Todas as funções retornam os resultados corretos
- ✅ Leitura do CSV funciona adequadamente
- ✅ Cálculos matemáticos precisos
- ✅ Filtros retornam dados corretos
- ✅ Todos os testes passam

## Testes Incluídos

### Testes por Função
Cada função tem seus próprios testes específicos:

**1. `ler_dados`**
- Verifica se função existe
- Testa se retorna DataFrame válido
- Verifica se carrega colunas obrigatórias

**2. `exibir_primeiras_linhas`**
- Verifica se função existe
- Testa comportamento padrão (5 linhas)
- Testa com parâmetro específico

**3. `vendas_por_vendedor`**
- Verifica se função existe
- Testa cálculo correto: João: 4450, Maria: 250, Pedro: 800

**4. `produto_mais_vendido`**
- Verifica se função existe
- Testa identificação correta (Mouse = maior quantidade)

**5. `categoria_maior_faturamento`**
- Verifica se função existe
- Testa identificação correta (Eletrônicos = maior faturamento)

**6. `filtrar_por_periodo`**
- Verifica se função existe
- Testa filtro correto por datas

### Teste de Integração
- Testa todas as funções com o arquivo CSV real


## Estado dos Testes

### Antes da Implementação
```
8 failed, 6 passed
Testes básicos passam, implementação pendente
```

### Após Implementação Correta
```
14 passed
All tests passed successfully!
```


## Regras Importantes

1. **NÃO altere o arquivo de testes**
2. **NÃO modifique o arquivo vendas.csv**
3. **Implemente apenas no arquivo** `solucao/analise_vendas.py`
4. **Todos os testes devem passar** para a solução ser considerada válida

## Entrega
Implemente todas as funções marcadas com `TODO` no arquivo:
- `solucao/analise_vendas.py`

Certifique-se de que todos os testes passem antes de considerar a implementação completa.

---

**Boa sorte! 🐍**