using System;
using System.Collections.Generic;
using System.Linq;

namespace AvaliationApp
{
    public class EstoqueManager
    {
        private readonly List<Produto> _produtos;

        public EstoqueManager()
        {
            _produtos = new List<Produto>();
        }

        /// <summary>
        /// Adiciona um produto ao estoque
        /// Regras: Não permitir produtos duplicados (mesmo Id) e validar dados obrigatórios
        /// </summary>
        public void AdicionarProduto(Produto produto)
        {
            // 1. Verificar se o objeto produto é nulo 
            if (produto == null)
            {
                throw new ArgumentNullException(nameof(produto), "O produto não pode ser nulo.");
            }

            // 2. Validar se o Nome não está vazio ou nulo
            if (string.IsNullOrEmpty(produto.Nome))
            {
                throw new ArgumentException("O nome do produto não pode ser vazio.", nameof(produto.Nome));
            }

            // 3. Validar se a Categoria não está vazia ou nula
            if (string.IsNullOrEmpty(produto.Categoria))
            {
                throw new ArgumentException("A categoria do produto não pode ser vazia.", nameof(produto.Categoria));
            }

            // 4. Verificar se já existe um produto com o mesmo Id na lista
            if (_produtos.Any(p => p.Id == produto.Id))
            {
                throw new ArgumentException($"Já existe um produto cadastrado com o Id {produto.Id}.", nameof(produto));            }

            _produtos.Add(produto);
        }

        /// <summary>
        /// Busca produtos por categoria
        /// Regras: Busca case-insensitive e deve remover espaços em branco das extremidades
        /// </summary>
        public IEnumerable<Produto> BuscarPorCategoria(string categoria)
        {
            // Regra: Verificar se categoria não é null ou vazia
            // Regra: Retornar lista vazia se categoria for inválida
            if (string.IsNullOrWhiteSpace(categoria))
            {
                return Enumerable.Empty<Produto>();
            }

            // Regra: Remover espaços em branco da categoria antes da busca
            var categoriaLimpa = categoria.Trim();

            // Regra: Fazer busca case-insensitive
            return _produtos.Where(p => 
                string.Equals(p.Categoria, categoriaLimpa, StringComparison.OrdinalIgnoreCase)
            );
        }

        /// <summary>
        /// Retorna os produtos mais caros (máximo 3)
        /// Regras: Em caso de empate no preço, priorizar por ordem alfabética do nome
        /// </summary>
        public IEnumerable<Produto> ProdutosMaisCaros()
        {
            // TODO: Implementar busca dos mais caros com critério de desempate
            // - Ordenar por preço (decrescente) e depois por nome (crescente)
            // - Retornar no máximo 3 produtos
            // - Se houver menos de 3 produtos, retornar todos
            return _produtos.OrderByDescending(p => p.Preco).ThenBy(p => p.Nome).Take(3);
        }

        /// <summary>
        /// Calcula o valor total de todos os produtos no estoque
        /// Regras: Aplicar desconto progressivo baseado na quantidade de produtos
        /// 10+ produtos: 5% de desconto
        /// 20+ produtos: 10% de desconto
        /// 50+ produtos: 15% de desconto
        /// </summary>
        public decimal ValorTotalEstoque()
        {
            decimal valorBruto = _produtos.Sum(p => p.Preco);
            int quantidadeTotal = _produtos.Count;
            
            decimal percentualDesconto = 0m;

            if (quantidadeTotal >= 50)
            {
                percentualDesconto = 15m;
            }
            else if (quantidadeTotal >= 30)
            {
                percentualDesconto = 10m; 
            }
            else if (quantidadeTotal >= 10)
            {
                percentualDesconto = 5m;
            }

            decimal valorDoDesconto = valorBruto * (percentualDesconto / 100);
            decimal valorFinal = valorBruto - valorDoDesconto;

            return valorFinal;
        }

        /// <summary>
        /// Agrupa produtos por categoria e retorna estatísticas de cada categoria.
        /// Retorna: Nome da categoria, Quantidade de produtos, Preço médio, Produto mais caro.
        /// </summary>
        public IEnumerable<object> EstatisticasPorCategoria()
        {
            return _produtos
                // 1. Agrupa todos os produtos pela propriedade 'Categoria'.
                //    O resultado é uma coleção de grupos, onde cada grupo tem uma chave (a categoria)
                //    e uma lista de todos os produtos pertencentes a essa categoria.
                .GroupBy(p => p.Categoria)
                
                // 2. Transforma (projeta) cada grupo em um novo objeto anônimo
                //    com as estatísticas calculadas.
                .Select(grupo => new
                {
                    // A chave do grupo é o nome da categoria.
                    Categoria = grupo.Key,
                    
                    // Conta quantos produtos existem no grupo.
                    Quantidade = grupo.Count(),
                    
                    // Calcula a média de preço dos produtos no grupo.
                    PrecoMedio = grupo.Average(p => p.Preco),
                    
                    // Encontra o produto mais caro dentro do grupo ordenando-os
                    // por preço e pegando o primeiro.
                    ProdutoMaisCaro = grupo.OrderByDescending(p => p.Preco).First()
                })
                
                // 3. Ordena a lista final de estatísticas pela quantidade de produtos
                //    em ordem decrescente (da maior para a menor).
                .OrderByDescending(estatisticas => estatisticas.Quantidade);
        }

        /// <summary>
        /// Método auxiliar para testes - retorna todos os produtos
        /// </summary>
        public IEnumerable<Produto> ObterTodosProdutos()
        {
            return _produtos.AsReadOnly();
        }
    }
}
