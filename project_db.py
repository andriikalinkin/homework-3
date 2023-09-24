import sqlite3
from random import randint

from faker import Faker


fake = Faker()


def customers_data() -> list:
    """Generate data for customers table."""
    data = []

    for _ in range(100):
        first_name = fake.first_name()
        last_name = fake.last_name()

        data.append((first_name, last_name))

    return data


def tracks_data() -> list:
    """Generate data for tracks table."""
    data = []

    for _ in range(100):
        artist = fake.first_name()
        title = fake.catch_phrase()
        length = randint(120, 600)
        year = fake.random_int(min=1950, max=2023)

        data.append((artist, title, length, year))

    return data


def init_db() -> None:
    """Initialize and fill the DB."""
    connection = sqlite3.connect("project_db.db")
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name VARCHAR(50),
                        last_name VARCHAR(50));
    """)
    cursor.executemany("INSERT INTO customers (first_name, last_name) VALUES (?, ?)", customers_data())

    cursor.execute("""CREATE TABLE IF NOT EXISTS tracks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    artist VARCHAR(50),
                    title VARCHAR(50),
                    length INT,
                    year INT);
    """)
    cursor.executemany("INSERT INTO tracks (artist, title, length, year) VALUES (?, ?, ?, ?)", tracks_data())

    connection.commit()
    cursor.close()

    return


def get_distinct_names() -> list:
    """Get all distinct names from `customer` table."""
    data = []

    connection = sqlite3.connect("project_db.db")
    cursor = connection.cursor()

    cursor.execute("SELECT DISTINCT first_name FROM customers;")

    for i in cursor.fetchall():
        data.append(i)

    return data


def get_tracks_quantity() -> list:
    """Get quantity of all tracks in `tracks` table."""
    connection = sqlite3.connect("project_db.db")
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM tracks;")

    return cursor.fetchone()


def get_all_tracks_content() -> list:
    """Get all content of `tracks` table. """
    data = []

    connection = sqlite3.connect("project_db.db")
    cursor = connection.cursor()

    cursor.execute("SELECT  id, artist, title, length, year FROM tracks;")

    for i in cursor.fetchall():
        data.append(i)

    return data
