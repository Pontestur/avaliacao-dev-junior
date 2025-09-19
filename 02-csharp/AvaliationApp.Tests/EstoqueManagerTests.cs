// 02-csharp/AvaliationApp.Tests/EstoqueManagerTests.cs
using Xunit;
using AvaliationApp;
using System.Linq;

namespace AvaliationApp.Tests
{
    public class EstoqueManagerTests
    {
        [Fact]
        public void AdicionarProduto_DeveAdicionarProdutoNaLista()
        {
            // Arrange
            var estoque = new EstoqueManager();
            var produto = new Produto
            {
                Id = 1,
                Nome = "Smartphone",
                Preco = 1500.00m,
                Categoria = "Eletrônicos"
            };

            // Act
            estoque.AdicionarProduto(produto);
            var produtos = estoque.ObterTodosProdutos();

            // Assert
            Assert.Single(produtos);
            Assert.Equal("Smartphone", produtos.First().Nome);
        }

        [Fact]
        public void BuscarPorCategoria_DeveRetornarProdutosDaCategoria()
        {
            // Arrange
            var estoque = new EstoqueManager();
            
            var produto1 = new Produto { Id = 1, Nome = "Notebook", Preco = 2500m, Categoria = "Eletrônicos" };
            var produto2 = new Produto { Id = 2, Nome = "Mesa", Preco = 500m, Categoria = "Móveis" };
            var produto3 = new Produto { Id = 3, Nome = "Mouse", Preco = 50m, Categoria = "Eletrônicos" };

            estoque.AdicionarProduto(produto1);
            estoque.AdicionarProduto(produto2);
            estoque.AdicionarProduto(produto3);

            // Act
            var eletronicos = estoque.BuscarPorCategoria("Eletrônicos");

            // Assert
            Assert.Equal(2, eletronicos.Count());
            Assert.All(eletronicos, p => Assert.Equal("Eletrônicos", p.Categoria));
        }

        [Fact]
        public void ProdutosMaisCaros_DeveRetornarTop3()
        {
            // Arrange
            var estoque = new EstoqueManager();
            
            // Adicionando 5 produtos com preços diferentes
            estoque.AdicionarProduto(new Produto { Id = 1, Nome = "Produto1", Preco = 100m, Categoria = "A" });
            estoque.AdicionarProduto(new Produto { Id = 2, Nome = "Produto2", Preco = 300m, Categoria = "A" });
            estoque.AdicionarProduto(new Produto { Id = 3, Nome = "Produto3", Preco = 200m, Categoria = "A" });
            estoque.AdicionarProduto(new Produto { Id = 4, Nome = "Produto4", Preco = 500m, Categoria = "A" });
            estoque.AdicionarProduto(new Produto { Id = 5, Nome = "Produto5", Preco = 400m, Categoria = "A" });

            // Act
            var maisCaros = estoque.ProdutosMaisCaros();

            // Assert
            Assert.Equal(3, maisCaros.Count());
            Assert.Equal(500m, maisCaros.First().Preco); // Mais caro primeiro
            Assert.Equal(300m, maisCaros.Last().Preco);  // Terceiro mais caro
        }

        [Fact]
        public void ValorTotalEstoque_DeveCalcularSomaCorreta()
        {
            // Arrange
            var estoque = new EstoqueManager();
            
            estoque.AdicionarProduto(new Produto { Id = 1, Nome = "P1", Preco = 100.50m, Categoria = "A" });
            estoque.AdicionarProduto(new Produto { Id = 2, Nome = "P2", Preco = 250.75m, Categoria = "B" });
            estoque.AdicionarProduto(new Produto { Id = 3, Nome = "P3", Preco = 49.25m, Categoria = "A" });

            // Act
            var valorTotal = estoque.ValorTotalEstoque();

            // Assert
            Assert.Equal(400.50m, valorTotal);
        }

        [Fact]
        public void EstoqueVazio_DeveRetornarValoresCorretos()
        {
            // Arrange
            var estoque = new EstoqueManager();

            // Act & Assert
            Assert.Empty(estoque.ObterTodosProdutos());
            Assert.Empty(estoque.BuscarPorCategoria("Qualquer"));
            Assert.Empty(estoque.ProdutosMaisCaros());
            Assert.Equal(0m, estoque.ValorTotalEstoque());
        }
    }
}