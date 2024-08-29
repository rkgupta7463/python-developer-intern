import dash
from dash import dcc, html
import plotly.express as px
import sqlite3
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)

# Connect to the database and get data for visualization
conn = sqlite3.connect('python_intern.db')

# Get the top 3 spenders
top_spenders = pd.read_sql_query('''
    SELECT users.name, SUM(transactions.amount) as total_spent
    FROM users
    JOIN transactions ON users.user_id = transactions.user_id
    GROUP BY users.user_id
    ORDER BY total_spent DESC
    LIMIT 3
''', conn)

# Create a bar chart for the top spenders
fig_top_spenders = px.bar(top_spenders, x='name', y='total_spent', title='Top 3 Users by Spending')

# Get the transaction amounts over time
transactions_over_time = pd.read_sql_query('''
    SELECT transaction_date, SUM(amount) as total_amount
    FROM transactions
    GROUP BY transaction_date
    ORDER BY transaction_date
''', conn)

# Create a line chart for transaction amounts over time
fig_transactions_over_time = px.line(transactions_over_time, x='transaction_date', y='total_amount', 
                                     title='Transaction Amounts Over Time')

# Define the layout of the Dash app
app.layout = html.Div(children=[
    html.H1(children='User Spending Dashboard'),

    dcc.Graph(
        id='top-spenders-bar',
        figure=fig_top_spenders
    ),

    dcc.Graph(
        id='transactions-over-time-line',
        figure=fig_transactions_over_time
    )
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
