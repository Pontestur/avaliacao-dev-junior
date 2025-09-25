"""
Análise de Vendas - Exercício Python
Implemente todas as funções seguindo as especificações
"""
import pandas as pd
from datetime import datetime
import os

def ler_dados():
    """
    Lê o arquivo CSV de vendas   

    Returns:
        pd.DataFrame: DataFrame com os dados carregados

    Exemplo de uso:
        df = ler_dados('../vendas.csv')
        print(df.head())
    """
    
    caminho_arquivo = os.path.join(os.path.dirname(__file__), '..', 'vendas.csv')
   
    # TODO: Implementar leitura do CSV
    df = pd.read_csv(caminho_arquivo)
    return df

def exibir_primeiras_linhas(df, n=5):
    """
    Retorna as primeiras N linhas do DataFrame

    Args:
        df (pd.DataFrame): DataFrame com os dados
        n (int): Número de linhas a retornar (padrão: 5)

    Returns:
        pd.DataFrame: Primeiras N linhas do DataFrame
    """
    # TODO: Implementar retorno das primeiras linhas
    return df.head(n)
    

def vendas_por_vendedor(df):
    """
    Calcula o total de vendas por vendedor

    Args:
        df (pd.DataFrame): DataFrame com os dados de vendas

    Returns:
        pd.Series ou dict: Vendedor como chave, total vendas como valor

    Exemplo resultado esperado:
        {'João Silva': 4850.0, 'Maria Santos': 1865.0, ...}
    """
    # TODO: Implementar cálculo
    df['total_na_venda'] = df['quantidade'] * df['preco_unitario']
    total_vendedor = df.groupby('vendedor')['total_na_venda'].sum()
    return total_vendedor

def produto_mais_vendido(df):
    """
    Identifica o produto mais vendido em quantidade
    
    Args:
        df (pd.DataFrame): DataFrame com os dados de vendas
        
    Returns:
        str: Nome do produto mais vendido
        
    Exemplo: 'Mouse Gamer' (se for o mais vendido)
    """
    # TODO: Implementar identificação
    vendas_por_produto = df.groupby('produto')['quantidade'].sum()
    mv = vendas_por_produto.sort_values(ascending=False).head(1)
    return mv

def categoria_maior_faturamento(df):
    """
    Identifica a categoria com maior faturamento

    Args:
        df (pd.DataFrame): DataFrame com os dados de vendas

    Returns:
        str: Nome da categoria com maior faturamento

    Exemplo: 'Eletrônicos' (se tiver maior faturamento)
    """
    # TODO: Implementar cálculo
    faturamento_por_categoria = df.groupby('categoria')['total_na_venda'].sum()
    return faturamento_por_categoria.head(1)
    

def filtrar_por_periodo(df, data_inicio, data_fim):
    """
    Filtra vendas por período específico
    
    Args:
        df (pd.DataFrame): DataFrame com os dados de vendas
        data_inicio (str): Data de início no formato 'YYYY-MM-DD'
        data_fim (str): Data de fim no formato 'YYYY-MM-DD'
        
    Returns:
        pd.DataFrame: DataFrame filtrado pelo período
        
    Exemplo:
        vendas_janeiro = filtrar_por_periodo(df, '2024-01-01', '2024-01-31')
    """
    # TODO: Implementar filtro
    data_inicio = '2024-01-01'
    data_fim = '2024-01-31'

    filtrado_data = df[(df['data'] >= data_inicio) & (df['data'] >= data_fim)]
    return filtrado_data

def main():
    """
    Função principal que executa todas as análises
    Demonstra o uso de todas as funções implementadas
    """
    print("=== ANÁLISE DE VENDAS ===")

    try:
        # 1. Carregar dados
        print("\n1. Carregando dados...")
        df = ler_dados()
        if df is not None:
            print(f"   [OK] Dados carregados: {len(df)} registros")
        else:
            print("   [PENDENTE] Funcao ler_dados() nao implementada")            

        # 2. Exibir primeiras linhas
        print("\n2. Primeiras linhas dos dados:")
        try:
            primeiras_linhas = exibir_primeiras_linhas(df)
            if primeiras_linhas is not None:
                print(primeiras_linhas)
                print("   [OK] Funcao exibir_primeiras_linhas() executada")
            else:
                print("   [PENDENTE] Funcao exibir_primeiras_linhas() nao implementada")
        except:
            print("   [PENDENTE] Funcao exibir_primeiras_linhas() nao implementada")

        # 3. Análise por vendedor
        print("\n3. Total de vendas por vendedor:")
        try:
            vendas = vendas_por_vendedor(df)
            if vendas is not None:
                for vendedor, total in vendas.items():
                    print(f"   {vendedor}: R$ {total:,.2f}")
                print("   [OK] Funcao vendas_por_vendedor() executada")
            else:
                print("   [PENDENTE] Funcao vendas_por_vendedor() nao implementada")
        except:
            print("   [PENDENTE] Funcao vendas_por_vendedor() nao implementada")

        # 4. Produto mais vendido
        print("\n4. Produto mais vendido:")
        try:
            produto_top = produto_mais_vendido(df)
            if produto_top is not None:
                print(f"   >> {produto_top}")
                print("   [OK] Funcao produto_mais_vendido() executada")
            else:
                print("   [PENDENTE] Funcao produto_mais_vendido() nao implementada")
        except:
            print("   [PENDENTE] Funcao produto_mais_vendido() nao implementada")

        # 5. Categoria com maior faturamento
        print("\n5. Categoria com maior faturamento:")
        try:
            categoria_top = categoria_maior_faturamento(df)
            if categoria_top is not None:
                print(f"   >> {categoria_top}")
                print("   [OK] Funcao categoria_maior_faturamento() executada")
            else:
                print("   [PENDENTE] Funcao categoria_maior_faturamento() nao implementada")
        except:
            print("   [PENDENTE] Funcao categoria_maior_faturamento() nao implementada")

        # 6. Exemplo de filtro por período
        print("\n6. Exemplo: vendas em Janeiro de 2024:")
        try:
            janeiro = filtrar_por_periodo(df, '2024-01-01', '2024-01-31')
            if janeiro is not None:
                print(f"   >> {len(janeiro)} vendas encontradas no periodo")
                print("   [OK] Funcao filtrar_por_periodo() executada")
            else:
                print("   [PENDENTE] Funcao filtrar_por_periodo() nao implementada")
        except:
            print("   [PENDENTE] Funcao filtrar_por_periodo() nao implementada")

        print("\n[CONCLUIDO] Execucao da analise finalizada!")
        print("Implemente as funcoes marcadas como [PENDENTE] para completar.")

    except Exception as e:
        print(f"\n[ERRO] Erro na analise: {e}")
        print("Verifique se todas as funcoes estao implementadas corretamente.")

if __name__ == "__main__":
    main()
