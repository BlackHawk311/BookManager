from fastapi import FastAPI
import psycopg
from pydantic import BaseModel

# connect to db
conn = psycopg.connect(
    host="bdd",
    port="5432",
    database="john",
    user="john",
    password="example"
)


app = FastAPI()

@app.get("/")
def index():
# -> select items from db
    cur = conn.cursor()
    cur.execute('SELECT * FROM books')
    books = cur.fetchall()
    cur.close()
    # We return books, without any kind of formatting.
    return books

class Book(BaseModel):
    name: str

@app.post("/books")
def create_book(book: Book):
    print(book)
    return 'book_created'

@app.get("/books")
def list_books():
    return 'book list'