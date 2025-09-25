using System;

namespace AvaliationApp
{
    public class Produto
    {
        private decimal _preco;

        public int Id { get; set; }
        public string Nome { get; set; } = string.Empty;
        
        public decimal Preco 
        { 
            get => _preco;
            set 
            {
                if (value < 0)
                    throw new ArgumentException("Preço não pode ser negativo");
                _preco = value;
            }
        }
        
        public string Categoria { get; set; } = string.Empty;

        /// <summary>
        /// Calcula o preço com desconto aplicado.
        /// </summary>
        /// <param name="percentualDesconto">Percentual de desconto (0-100)</param>
        /// <returns>Preço com desconto aplicado</returns>
        public decimal CalcularDesconto(decimal percentualDesconto)
        {
            // 1. Validação: Garante que o percentual esteja entre 0 e 100.
            if (percentualDesconto < 0 || percentualDesconto > 100)
            {
                throw new ArgumentOutOfRangeException(nameof(percentualDesconto), 
                    "O percentual de desconto deve estar entre 0 e 100.");
            }
            return this.Preco * (1 - (percentualDesconto / 100));
        }
    }
}
