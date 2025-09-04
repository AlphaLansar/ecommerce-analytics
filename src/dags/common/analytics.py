import pandas as pd

def daily_stock(products_df, orders_df):
    products_df['daily_stock'] = products_df['stock'] - orders_df['quantity'].sum()
    return products_df

def new_clients(clients_df, start_date):
    new_clients_df = clients_df[clients_df['signup_date'] >= start_date]
    return new_clients_df

def monthly_revenue(orders_df):
    orders_df['month'] = pd.to_datetime(orders_df['order_date']).dt.to_period('M')
    revenue_df = orders_df.groupby('month')['total_price'].sum().reset_index()
    return revenue_df
