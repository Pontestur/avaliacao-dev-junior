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
        /// </summary>
        public void AdicionarProduto(Produto produto)
        {
            // TODO: Implementar adição de produto
            throw new NotImplementedException("Método AdicionarProduto não implementado");
        }

        /// <summary>
        /// Busca produtos por categoria
        /// </summary>
        public IEnumerable<Produto> BuscarPorCategoria(string categoria)
        {
            // TODO: Implementar busca por categoria
            throw new NotImplementedException("Método BuscarPorCategoria não implementado");
        }

        /// <summary>
        /// Retorna os 3 produtos mais caros
        /// </summary>
        public IEnumerable<Produto> ProdutosMaisCaros()
        {
            // TODO: Implementar busca dos mais caros (top 3)
            throw new NotImplementedException("Método ProdutosMaisCaros não implementado");
        }

        /// <summary>
        /// Calcula o valor total de todos os produtos no estoque
        /// </summary>
        public decimal ValorTotalEstoque()
        {
            // TODO: Implementar cálculo do valor total
            throw new NotImplementedException("Método ValorTotalEstoque não implementado");
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
