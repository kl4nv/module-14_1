import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL)
    ''')

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()

initiate_db()
if len(get_all_products()) == 0:
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products(id, title, description, price) VALUES(?, ?, ?, ?)',
                       (i, f'Витамин {i}', f'Описание {i}', i * 1000))

connection.commit()

if __name__ == "__main__":
    connection.close()
