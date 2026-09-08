import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_FILE = BASE_DIR / "customer_support.db"


def get_connection():
    """Create a connection to the SQLite database."""
    return sqlite3.connect(DATABASE_FILE)


def initialize_database():
    """Create the tickets table if it does not exist."""

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT NOT NULL,
            intent TEXT NOT NULL,
            confidence REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    connection.commit()
    connection.close()


def log_ticket(query, intent, confidence):
    """Store a classified customer query."""

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO tickets (query, intent, confidence)
        VALUES (?, ?, ?)
        """,
        (query, intent, confidence),
    )

    connection.commit()
    connection.close()


def get_ticket_statistics():
    """Return the number of tickets for each intent."""

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT intent, COUNT(*)
        FROM tickets
        GROUP BY intent
        ORDER BY COUNT(*) DESC
        """
    )

    results = cursor.fetchall()

    connection.close()

    return results


if __name__ == "__main__":

    initialize_database()

    print(f"Database created: {DATABASE_FILE}")

    log_ticket(
        "Why was I charged twice?",
        "billing",
        0.92,
    )

    print("\nTicket statistics:")

    for intent, count in get_ticket_statistics():
        print(f"{intent}: {count}")