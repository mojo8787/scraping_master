import csv
import sqlite3

# CSV Storage
def save_to_csv(data, filename):
    """
    Saves the scraped data to a CSV file.
    """
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

# Database Storage (using SQLite for example)
def save_to_db(data, db_name):
    """
    Saves the scraped data to a SQLite database.
    """
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    # Assuming 'data' is a list of tuples representing rows
    cur.executemany('INSERT INTO your_table_name (column1, column2, ...) VALUES (?, ?, ...)', data)

    conn.commit()
    conn.close()

# Add more functions for database operations as needed (like creating tables, updating rows, etc.)
