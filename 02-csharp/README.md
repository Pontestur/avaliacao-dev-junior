# Avaliação Técnica - Parte 2: C#

## Visão Geral
Nesta etapa da avaliação, você trabalhará com um projeto em C# que simula um sistema básico de gerenciamento de estoque. Sua tarefa é implementar métodos que estão marcados como `TODO` e fazer todos os testes passarem.

## Estrutura do Projeto
```
02-csharp/
├── AvaliationApp/                 # Projeto principal
│   ├── Produto.cs                 # Classe que representa um produto
│   ├── EstoqueManager.cs          # Classe para gerenciar o estoque
│   └── AvaliationApp.csproj       # Arquivo de projeto
└── AvaliationApp.Tests/           # Projeto de testes
    ├── ProdutoTests.cs            # Testes da classe Produto
    ├── EstoqueManagerTests.cs     # Testes da classe EstoqueManager
    └── AvaliationApp.Tests.csproj # Arquivo de projeto de testes
```

## Tecnologias Utilizadas
- **.NET 9.0** - Framework principal
- **xUnit** - Framework de testes
- **C# 13** - Linguagem de programação

## Tarefas a Implementar

### 1. Classe Produto (`Produto.cs`)
Implemente o método `CalcularDesconto`:
- Deve calcular o preço com desconto aplicado
- Recebe um percentual de desconto (0-100)
- Retorna o preço com desconto aplicado
- Exemplo: preço R$ 100,00 com 10% de desconto = R$ 90,00

### 2. Classe EstoqueManager (`EstoqueManager.cs`)
Implemente os seguintes métodos:

#### `AdicionarProduto(Produto produto)`
- Adiciona um produto à lista interna de produtos
- **Validações:** Não aceitar produtos nulos, IDs duplicados, nomes ou categorias vazias

#### `BuscarPorCategoria(string categoria)`
- Retorna todos os produtos que pertencem à categoria especificada
- **Busca case-insensitive** e remove espaços em branco
- Retorna lista vazia se categoria for inválida

#### `ProdutosMaisCaros()`
- Retorna os 3 produtos mais caros do estoque
- Ordena por preço (decrescente), em caso de empate por nome (crescente)
- Se houver menos de 3 produtos, retorna todos os disponíveis

#### `ValorTotalEstoque()`
- Calcula valor total com **desconto progressivo:**
  - 10+ produtos: 5% desconto
  - 20+ produtos: 10% desconto
  - 50+ produtos: 15% desconto

#### `EstatisticasPorCategoria()`
- Agrupa produtos por categoria
- Retorna objeto anônimo com: Categoria, Quantidade, PrecoMedio, ProdutoMaisCaro
- Ordenado por quantidade de produtos (decrescente)

## Como Executar

### Pré-requisitos
- .NET 9.0 SDK instalado
- Editor de código (Visual Studio, VS Code, Rider, etc.)

### Comandos para Execução

1. **Navegar para o diretório do projeto:**
   Execute no terminal:
   ```
   cd 02-csharp
   ```

2. **Restaurar dependências:**
   Execute no terminal:
   ```
   dotnet restore
   ```

3. **Compilar o projeto:**
   Execute no terminal:
   ```
   dotnet build
   ```

4. **Executar os testes:**
   Execute no terminal:
   ```
   dotnet test
   ```

5. **Executar testes com detalhes:**
   Execute no terminal:
   ```
   dotnet test --verbosity normal
   ```

6. **Executar testes específicos:**
   Execute no terminal:
   ```
   # Executar apenas testes de uma classe
   dotnet test --filter "FullyQualifiedName~ProdutoTests"
   dotnet test --filter "FullyQualifiedName~EstoqueManagerTests"

   # Executar um teste específico
   dotnet test --filter "FullyQualifiedName=AvaliationApp.Tests.ProdutoTests.CalcularDesconto_DeveRetornarPrecoComDesconto"

   # Ou usando DisplayName (mais simples)
   dotnet test --filter "DisplayName~CalcularDesconto_DeveRetornarPrecoComDesconto"
   ```

### Debugging e Desenvolvimento

#### Visual Studio Code
1. Instale a extensão **C# Dev Kit**
2. Abra o projeto no VS Code
3. Para debuggar testes:
   - Abra o arquivo de teste desejado
   - Clique no ícone "▷" ao lado do teste que deseja executar
   - Ou use `Ctrl+F5` para executar sem debug
   - Ou use `F5` para executar com debug


#### Linha de Comando com Debug
Execute no terminal:
```
# Executar em modo debug (útil para ver stack traces completos)
dotnet test --logger "console;verbosity=detailed"

# Executar com informações de cobertura
dotnet test --collect:"XPlat Code Coverage"
```

### Estado Inicial dos Testes
Ao executar `dotnet test` antes de implementar os métodos, você verá:
```
Com falha! – Com falha: 16, Aprovado: 3, Ignorado: 0, Total: 19
```

Isso é esperado, pois os métodos ainda não foram implementados.

## Critérios de Avaliação

### Funcionalidade (40 pontos)
- ✅ Todos os testes devem passar
- ✅ Implementação correta dos cálculos
- ✅ Tratamento adequado de casos especiais (listas vazias, valores zero, etc.)

### Qualidade do Código (35 pontos)
- ✅ Código limpo e legível
- ✅ Uso adequado de LINQ quando apropriado
- ✅ Seguir convenções de nomenclatura do C#
- ✅ Implementação eficiente dos algoritmos

### Boas Práticas (25 pontos)
- ✅ Validação de parâmetros quando necessário
- ✅ Uso correto de tipos de retorno
- ✅ Manutenção da encapsulação
- ✅ Sem alteração na assinatura dos métodos existentes

## Testes Incluídos

### ProdutoTests
- Criação de produto com propriedades corretas
- Cálculo de desconto (10% e 0%)
- Validação de preço negativo (deve lançar exceção)

### EstoqueManagerTests
- Adição de produtos
- Busca por categoria
- Seleção dos 3 produtos mais caros
- Cálculo do valor total do estoque
- Comportamento com estoque vazio

## Regras Importantes

1. **NÃO altere a assinatura dos métodos existentes**
2. **NÃO altere os testes existentes**
3. **NÃO adicione novos arquivos** - trabalhe apenas com os arquivos fornecidos
4. **Todos os testes devem passar** para a solução ser considerada válida
5. **Use apenas recursos padrão do .NET** - não adicione bibliotecas externas


## Status Esperado Após Implementação
Quando você implementar todos os métodos corretamente, ao executar `dotnet test`, você deve ver algo como:

```
Aprovado!  - Com falha:     0, Aprovado:    19, Ignorado:     0, Total:    19
```

## Entrega
Implemente apenas os métodos marcados com `TODO` nos arquivos:
- `AvaliationApp/Produto.cs`
- `AvaliationApp/EstoqueManager.cs`

Certifique-se de que todos os testes passem antes de considerar a implementação completa.

---

**Boa sorte! 🚀**