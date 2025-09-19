"""
Análise de Vendas - Exercício Python
Implemente todas as funções seguindo as especificações
"""
import pandas as pd
from datetime import datetime
import os

def ler_dados(caminho_arquivo='../vendas.csv'):
    """
    Lê o arquivo CSV de vendas
    
    Args:
        caminho_arquivo (str): Caminho para o arquivo CSV
        
    Returns:
        pd.DataFrame: DataFrame com os dados carregados
        
    Exemplo de uso:
        df = ler_dados('../vendas.csv')
        print(df.head())
    """
    # TODO: Implementar leitura do CSV
    # Dicas:
    # - Use pd.read_csv()
    # - Configure parse_dates=['data'] para converter datas
    # - Trate encoding se necessário
    pass

def exibir_primeiras_linhas(df, n=5):
    """
    Exibe as primeiras N linhas do DataFrame
    
    Args:
        df (pd.DataFrame): DataFrame com os dados
        n (int): Número de linhas a exibir (padrão: 5)
        
    Retorna: None (apenas imprime)
    """
    # TODO: Implementar exibição
    # Use df.head(n) e print()
    pass

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
    # Dicas:
    # 1. Criar coluna 'total' = quantidade * preco_unitario
    # 2. Agrupar por vendedor: df.groupby('vendedor')
    # 3. Somar os totais: .sum()['total']
    pass

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
    # Dicas:
    # 1. Agrupar por produto: df.groupby('produto')
    # 2. Somar quantidades: .sum()['quantidade'] 
    # 3. Encontrar o máximo: .idxmax()
    pass

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
    # Dicas:
    # 1. Criar coluna total_faturamento = quantidade * preco_unitario
    # 2. Agrupar por categoria
    # 3. Somar faturamento por categoria
    # 4. Encontrar categoria com maior valor
    pass

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
    # Dicas:
    # 1. Converter data_inicio e data_fim para datetime
    # 2. Filtrar df onde data está no intervalo
    # 3. Use: (df['data'] >= data_inicio) & (df['data'] <= data_fim)
    pass

def main():
    """
    Função principal que executa todas as análises
    Demonstra o uso de todas as funções implementadas
    """
    print("=== ANÁLISE DE VENDAS ===")
    
    # TODO: Implementar execução completa
    # 1. Carregar dados com ler_dados()
    # 2. Exibir primeiras 5 linhas
    # 3. Mostrar vendas por vendedor
    # 4. Mostrar produto mais vendido
    # 5. Mostrar categoria com maior faturamento
    # 6. Exemplo de filtro por período
    
    # Exemplo de estrutura:
    # try:
    #     df = ler_dados('../vendas.csv')
    #     print("Dados carregados com sucesso!")
    #     exibir_primeiras_linhas(df)
    #     
    #     vendas = vendas_por_vendedor(df)
    #     print(f"Vendas por vendedor: {vendas}")
    #     
    #     produto_top = produto_mais_vendido(df)
    #     print(f"Produto mais vendido: {produto_top}")
    #     
    # except Exception as e:
    #     print(f"Erro na análise: {e}")
    
    pass

if __name__ == "__main__":
    main()
