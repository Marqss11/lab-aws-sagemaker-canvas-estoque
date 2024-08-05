import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Parâmetros iniciais
num_records = 500
num_products = 25
start_date = datetime(2023, 12, 31)
days_span = num_records // num_products
max_stock_reduction = 50

# Funções auxiliares
def generate_random_stock(size, low=50, high=200):
    return np.random.randint(low, high, size)

def generate_random_sales(stock):
    return np.clip(stock - np.random.randint(0, max_stock_reduction, len(stock)), 0, None)

# Geração de dados
data = []

for day in range(days_span):
    current_date = start_date + timedelta(days=day)
    for product_id in range(1, num_products + 1):
        # Definição dos atributos do produto
        stock = generate_random_stock(1)[0]
        sales = generate_random_sales([stock])[0]
        flag_promocao = np.random.choice([0, 1])
        
        # Registro de vendas
        data.append({
            "ID_PRODUTO": product_id,
            "DIA": current_date.strftime("%Y-%m-%d"),
            "FLAG_PROMOCAO": flag_promocao,
            "QUANTIDADE_ESTOQUE": max(stock - sales, 0)
        })

# Criação do DataFrame
df = pd.DataFrame(data)

# Ajuste do tamanho do dataset
df = df.head(num_records)

# Salvar o DataFrame em um arquivo CSV
csv_path = "historico_vendas.csv"
df.to_csv(csv_path, index=False)

print(f"Arquivo CSV salvo em: {csv_path}")