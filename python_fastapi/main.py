from fastapi import FastAPI, Depends, HTTPException
import sqlite3
from pydantic import BaseModel
from typing import List
import threading

app = FastAPI()

# Initialize the SQLite database connection and create a table
conn = sqlite3.connect("data/database.db")
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT
    )
    """
)
conn.commit()

# Models using Pydantic for request and response validation


class Item(BaseModel):
    name: str
    description: str = None

# Helper function to get the SQLite connection for the current thread


# Thread-local storage to hold the SQLite connection and cursor
local_data = threading.local()

# Helper function to get the SQLite connection for the current thread


def get_db_conn():
    # Check if the current thread has a connection; if not, create a new connection
    if not hasattr(local_data, "conn"):
        local_data.conn = sqlite3.connect("data/database.db")
    return local_data.conn

# Create a new item


@app.post("/items/", response_model=Item)
def create_item(item: Item, conn: sqlite3.Connection = Depends(get_db_conn)):
    with conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO items (name, description) VALUES (?, ?)",
                       (item.name, item.description))
        # item_id = cursor.lastrowid
    # item.id = item_id
    return item

# Retrieve all items


@app.get("/items/", response_model=List[Item])
def read_items(conn: sqlite3.Connection = Depends(get_db_conn)):
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items")
        items = [{"id": row[0], "name": row[1], "description": row[2]}
                 for row in cursor.fetchall()]
    return items

# Retrieve a single item by ID


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, conn: sqlite3.Connection = Depends(get_db_conn)):
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
        item = cursor.fetchone()
    if item:
        return {"id": item[0], "name": item[1], "description": item[2]}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
