import pandas as pd
from datetime import datetime
import os


caminho_arquivo = os.path.join(os.path.dirname(__file__), '..', 'vendas.csv')
df = pd.read_csv(caminho_arquivo)
print(df.head(1))

"""
    Calcula o total de vendas por vendedor

    Args:
        df (pd.DataFrame): DataFrame com os dados de vendas

    Returns:
        pd.Series ou dict: Vendedor como chave, total vendas como valor

    Exemplo resultado esperado:
        {'João Silva': 4850.0, 'Maria Santos': 1865.0, ...}
"""
vendas_por_produto = df.groupby('produto')['quantidade'].sum()
print(vendas_por_produto.sort_values(ascending=False).head(1))

