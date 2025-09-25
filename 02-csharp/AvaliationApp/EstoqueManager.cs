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
            // TODO: Implementar adição de produto com validações
            // - Verificar se produto não é null
            // - Verificar se já existe produto com mesmo Id
            // - Validar se Nome não está vazio
            // - Validar se Categoria não está vazia
            throw new NotImplementedException("Método AdicionarProduto não implementado");
        }

        /// <summary>
        /// Busca produtos por categoria
        /// Regras: Busca case-insensitive e deve remover espaços em branco das extremidades
        /// </summary>
        public IEnumerable<Produto> BuscarPorCategoria(string categoria)
        {
            // TODO: Implementar busca por categoria com validações
            // - Verificar se categoria não é null ou vazia
            // - Fazer busca case-insensitive
            // - Remover espaços em branco da categoria antes da busca
            // - Retornar lista vazia se categoria for inválida
            throw new NotImplementedException("Método BuscarPorCategoria não implementado");
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
            throw new NotImplementedException("Método ProdutosMaisCaros não implementado");
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
            // TODO: Implementar cálculo do valor total com desconto progressivo
            // - Somar todos os preços dos produtos
            // - Aplicar desconto baseado na quantidade total de produtos
            // - Retornar o valor com desconto aplicado
            throw new NotImplementedException("Método ValorTotalEstoque não implementado");
        }

        /// <summary>
        /// Agrupa produtos por categoria e retorna estatísticas de cada categoria
        /// Retorna: Nome da categoria, Quantidade de produtos, Preço médio, Produto mais caro
        /// </summary>
        public IEnumerable<object> EstatisticasPorCategoria()
        {
            // TODO: Implementar agrupamento e cálculo de estatísticas
            // - Agrupar produtos por categoria
            // - Para cada categoria calcular: quantidade, preço médio, produto mais caro
            // - Retornar objeto anônimo com: Categoria, Quantidade, PrecoMedio, ProdutoMaisCaro
            // - Ordenar por quantidade de produtos (decrescente)
            throw new NotImplementedException("Método EstatisticasPorCategoria não implementado");
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
