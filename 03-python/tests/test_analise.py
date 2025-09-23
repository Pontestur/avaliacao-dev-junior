import pytest
import pandas as pd
import os
import sys

# Adicionar pasta de solução ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solucao'))

@pytest.fixture
def dados_teste():
    """Dados de teste conhecidos para verificar resultados"""
    return pd.DataFrame({
        'data': pd.to_datetime(['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18']),
        'produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor'],
        'categoria': ['Eletrônicos', 'Eletrônicos', 'Eletrônicos', 'Eletrônicos'],
        'quantidade': [2, 5, 3, 1],
        'preco_unitario': [2000.0, 50.0, 150.0, 800.0],
        'vendedor': ['João', 'Maria', 'João', 'Pedro']
    })

class TestFuncaoLerDados:
    """Testa a função ler_dados"""

    def test_ler_dados_existe(self):
        """Verifica se a função ler_dados existe"""
        import analise_vendas
        assert hasattr(analise_vendas, 'ler_dados'), "Função 'ler_dados' não encontrada"

    def test_ler_dados_retorna_dataframe(self):
        """Verifica se ler_dados retorna um DataFrame válido"""
        import analise_vendas

        df = analise_vendas.ler_dados()

        assert isinstance(df, pd.DataFrame), "ler_dados deve retornar um DataFrame"
        assert len(df) > 0, "DataFrame não deve estar vazio"

        # Verificar colunas obrigatórias
        colunas_esperadas = ['data', 'produto', 'categoria', 'quantidade', 'preco_unitario', 'vendedor']
        for coluna in colunas_esperadas:
            assert coluna in df.columns, f"Coluna '{coluna}' não encontrada"

class TestFuncaoExibirPrimeirasLinhas:
    """Testa a função exibir_primeiras_linhas"""

    def test_exibir_primeiras_linhas_existe(self):
        """Verifica se a função exibir_primeiras_linhas existe"""
        import analise_vendas
        assert hasattr(analise_vendas, 'exibir_primeiras_linhas'), "Função 'exibir_primeiras_linhas' não encontrada"

    def test_exibir_primeiras_linhas_padrao(self, dados_teste):
        """Testa exibir_primeiras_linhas com valor padrão (5 linhas)"""
        import analise_vendas

        resultado = analise_vendas.exibir_primeiras_linhas(dados_teste)

        assert isinstance(resultado, pd.DataFrame), "Deve retornar um DataFrame"
        assert len(resultado) == 4, f"Com 4 registros, deve retornar 4 linhas, retornou {len(resultado)}"

    def test_exibir_primeiras_linhas_parametro(self, dados_teste):
        """Testa exibir_primeiras_linhas com parâmetro específico"""
        import analise_vendas

        resultado = analise_vendas.exibir_primeiras_linhas(dados_teste, 2)

        assert isinstance(resultado, pd.DataFrame), "Deve retornar um DataFrame"
        assert len(resultado) == 2, f"Deve retornar 2 linhas, retornou {len(resultado)}"

class TestFuncaoVendasPorVendedor:
    """Testa a função vendas_por_vendedor"""

    def test_vendas_por_vendedor_existe(self):
        """Verifica se a função vendas_por_vendedor existe"""
        import analise_vendas
        assert hasattr(analise_vendas, 'vendas_por_vendedor'), "Função 'vendas_por_vendedor' não encontrada"

    def test_vendas_por_vendedor_calculo(self, dados_teste):
        """Testa se o cálculo de vendas por vendedor está correto"""
        import analise_vendas

        resultado = analise_vendas.vendas_por_vendedor(dados_teste)

        # Converter para dict se for Series
        if isinstance(resultado, pd.Series):
            resultado = resultado.to_dict()

        assert isinstance(resultado, dict), "Deve retornar dict ou Series"

        # Verificar cálculos específicos
        # João: Notebook (2 * 2000) + Teclado (3 * 150) = 4000 + 450 = 4450
        # Maria: Mouse (5 * 50) = 250
        # Pedro: Monitor (1 * 800) = 800
        assert resultado['João'] == 4450.0, f"Total João esperado: 4450, recebido: {resultado.get('João')}"
        assert resultado['Maria'] == 250.0, f"Total Maria esperado: 250, recebido: {resultado.get('Maria')}"
        assert resultado['Pedro'] == 800.0, f"Total Pedro esperado: 800, recebido: {resultado.get('Pedro')}"

class TestFuncaoProdutoMaisVendido:
    """Testa a função produto_mais_vendido"""

    def test_produto_mais_vendido_existe(self):
        """Verifica se a função produto_mais_vendido existe"""
        import analise_vendas
        assert hasattr(analise_vendas, 'produto_mais_vendido'), "Função 'produto_mais_vendido' não encontrada"

    def test_produto_mais_vendido_resultado(self, dados_teste):
        """Testa se identifica o produto mais vendido corretamente"""
        import analise_vendas

        resultado = analise_vendas.produto_mais_vendido(dados_teste)

        assert isinstance(resultado, str), "Deve retornar uma string"
        # Mouse tem quantidade 5 (maior quantidade)
        assert resultado == 'Mouse', f"Produto mais vendido esperado: Mouse, recebido: {resultado}"

class TestFuncaoCategoriaMaiorFaturamento:
    """Testa a função categoria_maior_faturamento"""

    def test_categoria_maior_faturamento_existe(self):
        """Verifica se a função categoria_maior_faturamento existe"""
        import analise_vendas
        assert hasattr(analise_vendas, 'categoria_maior_faturamento'), "Função 'categoria_maior_faturamento' não encontrada"

    def test_categoria_maior_faturamento_resultado(self, dados_teste):
        """Testa se identifica a categoria com maior faturamento"""
        import analise_vendas

        resultado = analise_vendas.categoria_maior_faturamento(dados_teste)

        assert isinstance(resultado, str), "Deve retornar uma string"
        # Eletrônicos: (2*2000) + (5*50) + (3*150) + (1*800) = 4000 + 250 + 450 + 800 = 5500
        assert resultado == 'Eletrônicos', f"Categoria esperada: Eletrônicos, recebido: {resultado}"

class TestFuncaoFiltrarPorPeriodo:
    """Testa a função filtrar_por_periodo"""

    def test_filtrar_por_periodo_existe(self):
        """Verifica se a função filtrar_por_periodo existe"""
        import analise_vendas
        assert hasattr(analise_vendas, 'filtrar_por_periodo'), "Função 'filtrar_por_periodo' não encontrada"

    def test_filtrar_por_periodo_resultado(self, dados_teste):
        """Testa se o filtro por período funciona corretamente"""
        import analise_vendas

        resultado = analise_vendas.filtrar_por_periodo(dados_teste, '2024-01-16', '2024-01-17')

        assert isinstance(resultado, pd.DataFrame), "Deve retornar DataFrame"
        assert len(resultado) == 2, f"Esperado 2 registros, recebido {len(resultado)}"

        produtos = resultado['produto'].tolist()
        assert 'Mouse' in produtos, "Produto 'Mouse' deveria estar no período"
        assert 'Teclado' in produtos, "Produto 'Teclado' deveria estar no período"

class TestIntegracao:
    """Teste de integração com dados reais"""

    def test_funciona_com_csv_real(self):
        """Testa se todas as funções funcionam com o arquivo CSV real"""
        import analise_vendas

        # Verificar se arquivo existe
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'vendas.csv')
        if not os.path.exists(csv_path):
            pytest.skip("Arquivo vendas.csv não encontrado")

        # Testar leitura
        df = analise_vendas.ler_dados()
        assert len(df) > 0, "Deve ler dados do CSV real"

        # Testar outras funções com dados reais
        primeiras = analise_vendas.exibir_primeiras_linhas(df, 3)
        assert len(primeiras) == 3, "Deve retornar 3 primeiras linhas"

        vendas = analise_vendas.vendas_por_vendedor(df)
        assert len(vendas) > 0, "Deve calcular vendas por vendedor"

        produto = analise_vendas.produto_mais_vendido(df)
        assert isinstance(produto, str), "Deve retornar nome do produto"

        categoria = analise_vendas.categoria_maior_faturamento(df)
        assert isinstance(categoria, str), "Deve retornar nome da categoria"

        janeiro = analise_vendas.filtrar_por_periodo(df, '2024-01-01', '2024-01-31')
        assert isinstance(janeiro, pd.DataFrame), "Deve retornar DataFrame filtrado"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])