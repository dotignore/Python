import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Create a database connection to a SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """Create a table from the create_table_sql statement."""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_word(conn, word):
    """Insert a new word into the Words_en table."""
    sql = ''' INSERT INTO Words_en(Word, AccessCount, AudioPath)
              VALUES(?,0,NULL) '''
    cur = conn.cursor()
    cur.execute(sql, (word,))
    return cur.lastrowid

def main():
    database = r'C:\Users\hc158\GitHub\Python\BE_API_soundoftext\sqlite\translate.db'

    # SQL for creating the Words_en table without WordID
    sql_create_words_en_table = """CREATE TABLE IF NOT EXISTS Words_en (
                                    Word TEXT NOT NULL,
                                    AccessCount INTEGER DEFAULT 0,
                                    AudioPath TEXT
                                );"""

    # Create a database connection
    conn = create_connection(database)

    # Create the Words_en table
    if conn is not None:
        create_table(conn, sql_create_words_en_table)

        # Read words from file and insert into the Words_en table
        words_file_path = r'C:\Users\hc158\GitHub\Python\BE_API_soundoftext\sqlite\words_en.txt'
        with open(words_file_path, 'r') as words_file:
            for word in words_file:
                word = word.strip()  # Remove whitespace
                if word:  # Check if the word is not empty
                    insert_word(conn, word)
        conn.commit()  # Commit the changes
        print("Words have been added to the database.")
    else:
        print("Error! cannot create the database connection.")

    # Close the connection to the database
    if conn:
        conn.close()

if __name__ == '__main__':
    main()
