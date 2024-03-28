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
    """Insert a new word into the Words table."""
    sql = ''' INSERT INTO Words(word_text)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, (word,))
    return cur.lastrowid


def main():
    database = r'C:\Users\hc158\GitHub\Python\BE_API_soundoftext\sqlite\translate.db'

    sql_create_words_table = """ CREATE TABLE IF NOT EXISTS Words (
                                        word_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        word_text TEXT NOT NULL
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create Words table
        create_table(conn, sql_create_words_table)

        # Read words from file and insert into the Words table
        words_file_path = r'C:\Users\hc158\GitHub\Python\BE_API_soundoftext\sqlite\en_words.txt'
        with open(words_file_path, 'r') as words_file:
            for word in words_file:
                word = word.strip()  # Remove whitespace
                if word:  # Check if the word is not empty
                    insert_word(conn, word)
        conn.commit()  # Commit the changes
        print("Words have been added to the database.")
    else:
        print("Error! cannot create the database connection.")

    if conn:
        conn.close()


if __name__ == '__main__':
    main()