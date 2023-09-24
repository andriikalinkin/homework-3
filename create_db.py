import sqlite3
from random import randint

from faker import Faker


fake = Faker()


def customers_data() -> list:
    data = []

    for _ in range(100):
        first_name = fake.first_name()
        last_name = fake.last_name()

        data.append((first_name, last_name))

    return data


def tracks_data() -> list:
    data = []

    for _ in range(100):
        artist = fake.first_name()
        title = fake.catch_phrase()
        length = randint(120, 600)
        year = fake.random_int(min=1950, max=2023)

        data.append((artist, title, length, year))

    return data


def init_db() -> None:
    con = sqlite3.connect("project_db.db")
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS customers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name VARCHAR(50),
                        last_name VARCHAR(50));
    """)
    cur.executemany("INSERT INTO customers (first_name, last_name) VALUES (?, ?)", customers_data())

    cur.execute("""CREATE TABLE IF NOT EXISTS tracks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    artist VARCHAR(50),
                    title VARCHAR(50),
                    length INT,
                    year INT);
    """)
    cur.executemany("INSERT INTO tracks (artist, title, length, year) VALUES (?, ?, ?, ?)", tracks_data())

    con.commit()
    con.close()

    return


init_db()
