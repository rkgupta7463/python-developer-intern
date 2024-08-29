import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('python_intern.db')
cursor = conn.cursor()

# Task 1: Query users who joined within a specific date range
def get_users_by_join_date(start_date, end_date):
    query = '''
    SELECT * FROM users WHERE join_date BETWEEN ? AND ?
    '''
    cursor.execute(query, (start_date, end_date))
    return cursor.fetchall()

# Task 2: Calculate the total amount spent by each user
def get_total_spent_by_users():
    query = '''
    SELECT users.name, users.email, SUM(transactions.amount) as total_spent
    FROM users
    JOIN transactions ON users.user_id = transactions.user_id
    GROUP BY users.user_id
    '''
    cursor.execute(query)
    return cursor.fetchall()

# Task 3: Generate a report with user details and total amount spent
def get_user_spending_report():
    query = '''
    SELECT users.name, users.email, SUM(transactions.amount) as total_spent
    FROM users
    LEFT JOIN transactions ON users.user_id = transactions.user_id
    GROUP BY users.user_id
    '''
    cursor.execute(query)
    return cursor.fetchall()

# Task 4: Find the top 3 users who spent the most
def get_top_spenders(limit=3):
    query = '''
    SELECT users.name, SUM(transactions.amount) as total_spent
    FROM users
    JOIN transactions ON users.user_id = transactions.user_id
    GROUP BY users.user_id
    ORDER BY total_spent DESC
    LIMIT ?
    '''
    cursor.execute(query, (limit,))
    return cursor.fetchall()

# Task 5: Calculate the average transaction amount
def get_average_transaction_amount():
    query = '''
    SELECT AVG(amount) FROM transactions
    '''
    cursor.execute(query)
    return cursor.fetchone()[0]

# Task 6: Identify users with no transactions
def get_users_with_no_transactions():
    query = '''
    SELECT users.name, users.email
    FROM users
    LEFT JOIN transactions ON users.user_id = transactions.user_id
    WHERE transactions.transaction_id IS NULL
    '''
    cursor.execute(query)
    return cursor.fetchall()

# Example usage
print("Users who joined between 2023-01-01 and 2023-03-01:")
print(get_users_by_join_date('2023-01-01', '2023-03-01'))

print("\nTotal amount spent by each user:")
print(get_total_spent_by_users())

print("\nUser spending report:")
print(get_user_spending_report())

print("\nTop 3 spenders:")
print(get_top_spenders())

print("\nAverage transaction amount:")
print(get_average_transaction_amount())

print("\nUsers with no transactions:")
print(get_users_with_no_transactions())

# Close the connection
conn.close()
