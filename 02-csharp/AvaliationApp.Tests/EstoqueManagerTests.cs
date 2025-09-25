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
        public void AdicionarProduto_NaoDevePermitirProdutoNull()
        {
            // Arrange
            var estoque = new EstoqueManager();

            // Act & Assert
            Assert.Throws<ArgumentNullException>(() => estoque.AdicionarProduto(null));
        }

        [Fact]
        public void AdicionarProduto_NaoDevePermitirIdDuplicado()
        {
            // Arrange
            var estoque = new EstoqueManager();
            var produto1 = new Produto { Id = 1, Nome = "P1", Preco = 100m, Categoria = "A" };
            var produto2 = new Produto { Id = 1, Nome = "P2", Preco = 200m, Categoria = "B" };

            // Act
            estoque.AdicionarProduto(produto1);

            // Assert
            Assert.Throws<ArgumentException>(() => estoque.AdicionarProduto(produto2));
        }

        [Fact]
        public void AdicionarProduto_NaoDevePermitirNomeVazio()
        {
            // Arrange
            var estoque = new EstoqueManager();
            var produto = new Produto { Id = 1, Nome = "", Preco = 100m, Categoria = "A" };

            // Act & Assert
            Assert.Throws<ArgumentException>(() => estoque.AdicionarProduto(produto));
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
        public void BuscarPorCategoria_DeveFazerBuscaCaseInsensitive()
        {
            // Arrange
            var estoque = new EstoqueManager();
            var produto = new Produto { Id = 1, Nome = "Notebook", Preco = 2500m, Categoria = "Eletrônicos" };
            estoque.AdicionarProduto(produto);

            // Act & Assert
            Assert.Single(estoque.BuscarPorCategoria("eletrônicos"));
            Assert.Single(estoque.BuscarPorCategoria("ELETRÔNICOS"));
            Assert.Single(estoque.BuscarPorCategoria("ELETRÔNicos"));
        }

        [Fact]
        public void BuscarPorCategoria_DeveIgnorarEspacosEmBranco()
        {
            // Arrange
            var estoque = new EstoqueManager();
            var produto = new Produto { Id = 1, Nome = "Notebook", Preco = 2500m, Categoria = "Eletrônicos" };
            estoque.AdicionarProduto(produto);

            // Act & Assert
            Assert.Single(estoque.BuscarPorCategoria("  Eletrônicos  "));
            Assert.Empty(estoque.BuscarPorCategoria(""));
            Assert.Empty(estoque.BuscarPorCategoria("   "));
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
        public void ProdutosMaisCaros_DeveDesempatarPorNome()
        {
            // Arrange
            var estoque = new EstoqueManager();

            // Produtos com mesmo preço para testar desempate
            estoque.AdicionarProduto(new Produto { Id = 1, Nome = "Zebra", Preco = 100m, Categoria = "A" });
            estoque.AdicionarProduto(new Produto { Id = 2, Nome = "Alpha", Preco = 100m, Categoria = "A" });
            estoque.AdicionarProduto(new Produto { Id = 3, Nome = "Beta", Preco = 100m, Categoria = "A" });

            // Act
            var maisCaros = estoque.ProdutosMaisCaros();

            // Assert
            Assert.Equal(3, maisCaros.Count());
            Assert.Equal("Alpha", maisCaros.First().Nome); // Primeiro alfabeticamente
            Assert.Equal("Beta", maisCaros.Skip(1).First().Nome);
            Assert.Equal("Zebra", maisCaros.Last().Nome);
        }

        [Fact]
        public void ValorTotalEstoque_DeveFuncionarSemDesconto()
        {
            // Arrange
            var estoque = new EstoqueManager();

            // Menos de 10 produtos - sem desconto
            estoque.AdicionarProduto(new Produto { Id = 1, Nome = "P1", Preco = 100m, Categoria = "A" });
            estoque.AdicionarProduto(new Produto { Id = 2, Nome = "P2", Preco = 200m, Categoria = "A" });

            // Act
            var valorTotal = estoque.ValorTotalEstoque();

            // Assert
            Assert.Equal(300m, valorTotal); // Sem desconto
        }

        [Fact]
        public void ValorTotalEstoque_DeveAplicarDesconto5Porcento()
        {
            // Arrange
            var estoque = new EstoqueManager();

            // 10 produtos - 5% desconto
            for (int i = 1; i <= 10; i++)
            {
                estoque.AdicionarProduto(new Produto { Id = i, Nome = $"P{i}", Preco = 100m, Categoria = "A" });
            }

            // Act
            var valorTotal = estoque.ValorTotalEstoque();

            // Assert
            Assert.Equal(950m, valorTotal); // 1000 - 5% = 950
        }

        [Fact]
        public void ValorTotalEstoque_DeveAplicarDesconto15Porcento()
        {
            // Arrange
            var estoque = new EstoqueManager();

            // 50 produtos - 15% desconto
            for (int i = 1; i <= 50; i++)
            {
                estoque.AdicionarProduto(new Produto { Id = i, Nome = $"P{i}", Preco = 100m, Categoria = "A" });
            }

            // Act
            var valorTotal = estoque.ValorTotalEstoque();

            // Assert
            Assert.Equal(4250m, valorTotal); // 5000 - 15% = 4250
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

        [Fact]
        public void EstatisticasPorCategoria_DeveCalcularCorretamente()
        {
            // Arrange
            var estoque = new EstoqueManager();

            // Categoria A: 3 produtos (100, 200, 300) - média 200, mais caro 300
            estoque.AdicionarProduto(new Produto { Id = 1, Nome = "A1", Preco = 100m, Categoria = "Eletrônicos" });
            estoque.AdicionarProduto(new Produto { Id = 2, Nome = "A2", Preco = 200m, Categoria = "Eletrônicos" });
            estoque.AdicionarProduto(new Produto { Id = 3, Nome = "A3", Preco = 300m, Categoria = "Eletrônicos" });

            // Categoria B: 2 produtos (150, 250) - média 200, mais caro 250
            estoque.AdicionarProduto(new Produto { Id = 4, Nome = "B1", Preco = 150m, Categoria = "Móveis" });
            estoque.AdicionarProduto(new Produto { Id = 5, Nome = "B2", Preco = 250m, Categoria = "Móveis" });

            // Act
            var estatisticas = estoque.EstatisticasPorCategoria().ToList();

            // Assert
            Assert.Equal(2, estatisticas.Count);

            // Primeiro deve ser Eletrônicos (3 produtos)
            var primeiraEstat = estatisticas.First();
            Assert.Equal("Eletrônicos", primeiraEstat.GetType().GetProperty("Categoria")?.GetValue(primeiraEstat));
            Assert.Equal(3, primeiraEstat.GetType().GetProperty("Quantidade")?.GetValue(primeiraEstat));
            Assert.Equal(200m, primeiraEstat.GetType().GetProperty("PrecoMedio")?.GetValue(primeiraEstat));
            Assert.Equal("A3", ((Produto)primeiraEstat.GetType().GetProperty("ProdutoMaisCaro")?.GetValue(primeiraEstat)).Nome);

            // Segunda deve ser Móveis (2 produtos)
            var segundaEstat = estatisticas.Last();
            Assert.Equal("Móveis", segundaEstat.GetType().GetProperty("Categoria")?.GetValue(segundaEstat));
            Assert.Equal(2, segundaEstat.GetType().GetProperty("Quantidade")?.GetValue(segundaEstat));
            Assert.Equal(200m, segundaEstat.GetType().GetProperty("PrecoMedio")?.GetValue(segundaEstat));
            Assert.Equal("B2", ((Produto)segundaEstat.GetType().GetProperty("ProdutoMaisCaro")?.GetValue(segundaEstat)).Nome);
        }
    }
}