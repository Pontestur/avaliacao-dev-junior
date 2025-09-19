// 02-csharp/AvaliationApp.Tests/ProdutoTests.cs
using Xunit;
using AvaliationApp;
using System;

namespace AvaliationApp.Tests
{
    public class ProdutoTests
    {
        [Fact]
        public void Produto_DeveCriarComPropriedadesCorretas()
        {
            // Arrange & Act
            var produto = new Produto
            {
                Id = 1,
                Nome = "Notebook",
                Preco = 2500.00m,
                Categoria = "Eletrônicos"
            };

            // Assert
            Assert.Equal(1, produto.Id);
            Assert.Equal("Notebook", produto.Nome);
            Assert.Equal(2500.00m, produto.Preco);
            Assert.Equal("Eletrônicos", produto.Categoria);
        }

        [Fact]
        public void CalcularDesconto_DeveRetornarPrecoComDesconto()
        {
            // Arrange
            var produto = new Produto
            {
                Id = 1,
                Nome = "Mouse",
                Preco = 100.00m,
                Categoria = "Eletrônicos"
            };

            // Act
            var precoComDesconto = produto.CalcularDesconto(10);

            // Assert
            Assert.Equal(90.00m, precoComDesconto);
        }

        [Fact]
        public void CalcularDesconto_DeveManterPrecoSemDesconto()
        {
            // Arrange
            var produto = new Produto
            {
                Id = 1,
                Nome = "Teclado",
                Preco = 200.00m,
                Categoria = "Eletrônicos"
            };

            // Act
            var precoComDesconto = produto.CalcularDesconto(0);

            // Assert
            Assert.Equal(200.00m, precoComDesconto);
        }

        [Theory]
        [InlineData(-100)]
        [InlineData(-50.5)]
        public void Produto_NaoDeveAceitarPrecoNegativo(decimal precoInvalido)
        {
            // Assert
            Assert.Throws<ArgumentException>(() => 
            {
                var produto = new Produto
                {
                    Id = 1,
                    Nome = "Produto Teste",
                    Preco = precoInvalido,
                    Categoria = "Teste"
                };
            });
        }
    }
}



