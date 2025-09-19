import pytest
import pandas as pd
import os
import sys
from datetime import datetime

# Adicionar pasta de solução ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solucao'))

@pytest.fixture
def dados_vendas():
    """Dados de teste conhecidos para verificar resultados"""
    return pd.DataFrame({
        'data': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18'],
        'produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor'],
        'categoria': ['Eletrônicos', 'Eletrônicos', 'Eletrônicos', 'Eletrônicos'],
        'quantidade': [2, 5, 3, 1],
        'preco_unitario': [2000.0, 50.0, 150.0, 800.0],
        'vendedor': ['João', 'Maria', 'João', 'Pedro']
    })

class TestImplementacaoBasica:
    """Testes básicos de funcionamento"""
    
    def test_arquivo_existe(self):
        """Verifica se o arquivo de solução existe"""
        solucao_path = os.path.join(os.path.dirname(__file__), '..', 'solucao', 'analise_vendas.py')
        assert os.path.exists(solucao_path), "Arquivo 'analise_vendas.py' não encontrado na pasta solucao/"

    def test_importacao_modulo(self):
        """Testa se o módulo pode ser importado sem erros"""
        try:
            import analise_vendas
            assert True
        except ImportError as e:
            pytest.fail(f"Erro ao importar módulo: {e}")
        except SyntaxError as e:
            pytest.fail(f"Erro de sintaxe no módulo: {e}")

class TestLeituraArquivo:
    """Testa leitura de arquivo CSV"""
    
    def test_ler_dados_funciona(self):
        """Verifica se consegue ler CSV corretamente"""
        import analise_vendas
        
        # Verificar se função existe
        assert hasattr(analise_vendas, 'ler_dados'), "Função 'ler_dados' não encontrada"
        
        # Testar se retorna DataFrame
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'vendas.csv')
        df = analise_vendas.ler_dados(csv_path)
        
        assert isinstance(df, pd.DataFrame), "ler_dados deve retornar um DataFrame"
        assert len(df) > 0, "DataFrame não deve estar vazio"
        assert 'produto' in df.columns, "Coluna 'produto' não encontrada"
        assert 'vendedor' in df.columns, "Coluna 'vendedor' não encontrada"

class TestAnaliseVendas:
    """Testes das análises específicas com resultados esperados"""
    
    def test_vendas_por_vendedor_calculo_correto(self, dados_vendas):
        """Testa se cálculo de vendas por vendedor está correto"""
        import analise_vendas
        
        # Verificar se função existe
        funcoes_possives = ['vendas_por_vendedor', 'calcular_vendas_vendedor', 'total_por_vendedor']
        funcao = None
        for nome in funcoes_possives:
            if hasattr(analise_vendas, nome):
                funcao = getattr(analise_vendas, nome)
                break
        
        assert funcao is not None, "Função de vendas por vendedor não encontrada"
        
        # Executar função
        resultado = funcao(dados_vendas)
        
        # Verificar resultados específicos
        # João: Notebook (2 * 2000) + Teclado (3 * 150) = 4000 + 450 = 4450
        # Maria: Mouse (5 * 50) = 250  
        # Pedro: Monitor (1 * 800) = 800
        
        assert isinstance(resultado, (pd.Series, dict)), "Deve retornar Series ou dict"
        
        if isinstance(resultado, pd.Series):
            resultado = resultado.to_dict()
        
        assert resultado['João'] == 4450.0, f"Total João esperado: 4450, recebido: {resultado.get('João')}"
        assert resultado['Maria'] == 250.0, f"Total Maria esperado: 250, recebido: {resultado.get('Maria')}"
        assert resultado['Pedro'] == 800.0, f"Total Pedro esperado: 800, recebido: {resultado.get('Pedro')}"

    def test_produto_mais_vendido_quantidade(self, dados_vendas):
        """Testa se identifica produto mais vendido por quantidade"""
        import analise_vendas
        
        funcoes_possives = ['produto_mais_vendido', 'produto_top_vendas', 'maior_quantidade']
        funcao = None
        for nome in funcoes_possives:
            if hasattr(analise_vendas, nome):
                funcao = getattr(analise_vendas, nome)
                break
                
        assert funcao is not None, "Função produto_mais_vendido não encontrada"
        
        # Executar função
        resultado = funcao(dados_vendas)
        
        # Mouse tem quantidade 5 (maior quantidade)
        assert resultado == 'Mouse', f"Produto mais vendido esperado: Mouse, recebido: {resultado}"

    def test_categoria_maior_faturamento_calculo(self, dados_vendas):
        """Testa se calcula categoria com maior faturamento"""
        import analise_vendas
        
        funcoes_possives = ['categoria_maior_faturamento', 'categoria_top', 'melhor_categoria']
        funcao = None
        for nome in funcoes_possives:
            if hasattr(analise_vendas, nome):
                funcao = getattr(analise_vendas, nome)
                break
                
        assert funcao is not None, "Função categoria_maior_faturamento não encontrada"
        
        # Executar função  
        resultado = funcao(dados_vendas)
        
        # Eletrônicos: (2*2000) + (5*50) + (3*150) + (1*800) = 4000 + 250 + 450 + 800 = 5500
        assert resultado == 'Eletrônicos', f"Categoria esperada: Eletrônicos, recebido: {resultado}"

class TestFiltrosPeriodo:
    """Testa filtros por período"""
    
    def test_filtrar_por_periodo_funcionando(self, dados_vendas):
        """Testa se filtro por período funciona corretamente"""
        import analise_vendas
        
        funcoes_possives = ['filtrar_por_periodo', 'vendas_periodo', 'filtrar_datas']
        funcao = None
        for nome in funcoes_possives:
            if hasattr(analise_vendas, nome):
                funcao = getattr(analise_vendas, nome)
                break
                
        assert funcao is not None, "Função filtrar_por_periodo não encontrada"
        
        # Testar filtro
        resultado = funcao(dados_vendas, '2024-01-16', '2024-01-17')
        
        # Deve retornar apenas registros entre 16 e 17 (Mouse e Teclado)
        assert isinstance(resultado, pd.DataFrame), "Deve retornar DataFrame"
        assert len(resultado) == 2, f"Esperado 2 registros, recebido {len(resultado)}"
        produtos = resultado['produto'].tolist()
        assert 'Mouse' in produtos and 'Teclado' in produtos, f"Produtos esperados: Mouse e Teclado, recebidos: {produtos}"

class TestResultadosReais:
    """Testa com dados reais do CSV fornecido"""
    
    def test_analise_csv_real(self):
        """Testa análise com arquivo CSV real"""
        import analise_vendas
        
        # Carregar dados reais
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'vendas.csv')
        if not os.path.exists(csv_path):
            pytest.skip("Arquivo vendas.csv não encontrado")
            
        df = analise_vendas.ler_dados(csv_path)
        
        # Verificar estrutura
        colunas_obrigatorias = ['data', 'produto', 'categoria', 'quantidade', 'preco_unitario', 'vendedor']
        for coluna in colunas_obrigatorias:
            assert coluna in df.columns, f"Coluna obrigatória '{coluna}' não encontrada"
        
        # Verificar tipos de dados
        assert df['quantidade'].dtype in ['int64', 'int32'], "Coluna quantidade deve ser numérica"
        assert df['preco_unitario'].dtype in ['float64', 'float32'], "Coluna preco_unitario deve ser float"
        
        # Testar se análises funcionam com dados reais
        if hasattr(analise_vendas, 'vendas_por_vendedor'):
            vendas = analise_vendas.vendas_por_vendedor(df)
            assert len(vendas) > 0, "Análise de vendas por vendedor deve retornar dados"

class TestQualidadeCodigo:
    """Testes de qualidade e boas práticas"""
    
    def test_uso_pandas_adequado(self):
        """Verifica uso adequado do pandas"""
        solucao_path = os.path.join(os.path.dirname(__file__), '..', 'solucao', 'analise_vendas.py')
        
        with open(solucao_path, 'r', encoding='utf-8') as f:
            codigo = f.read()
        
        # Verificar imports corretos
        assert 'import pandas' in codigo or 'from pandas import' in codigo, "Deve importar pandas"
        
        # Verificar uso de métodos pandas
        operacoes_pandas = ['groupby', 'sum()', 'max()', 'filter', 'sort_values']
        uso_pandas = any(op in codigo for op in operacoes_pandas)
        assert uso_pandas, "Deve usar operações do pandas (groupby, sum, etc.)"

    def test_tratamento_erros_basico(self):
        """Verifica tratamento básico de erros"""
        import analise_vendas
        
        # Testar com DataFrame vazio
        df_vazio = pd.DataFrame()
        
        funcoes_para_testar = []
        if hasattr(analise_vendas, 'vendas_por_vendedor'):
            funcoes_para_testar.append(('vendas_por_vendedor', analise_vendas.vendas_por_vendedor))
        
        # Pelo menos uma função deve lidar com DataFrame vazio sem quebrar
        for nome, funcao in funcoes_para_testar:
            try:
                resultado = funcao(df_vazio)
                # Se não quebrou, está bom
                assert True
            except Exception as e:
                # Aceitar apenas erros específicos esperados
                assert isinstance(e, (ValueError, KeyError)), f"Função {nome} deve tratar DataFrames vazios adequadamente"

class TestIntegracao:
    """Teste de integração completo"""
    
    def test_fluxo_completo(self):
        """Testa execução do fluxo principal"""
        import analise_vendas
        
        # Verificar se main existe e executa
        if hasattr(analise_vendas, 'main'):
            try:
                # Capturar prints se necessário
                analise_vendas.main()
                assert True, "Função main executou sem erro"
            except Exception as e:
                pytest.fail(f"Erro na execução do main: {e}")
        else:
            pytest.skip("Função main não implementada")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
