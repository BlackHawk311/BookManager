import psycopg

# We connect to the database (Postgres) with :
# - psycopg2 package
# - infos coming from the setup we did in docker-compose.yml
# http://bdd:5432

# connect to db
conn = psycopg.connect(
    host="bdd",
    port="5432",
    database="john",
    user="john",
    password="example"
)

# -> select items from db
cur = conn.cursor()
cur.execute('SELECT * FROM books')
books = cur.fetchall()
cur.close()

# -> insert item into db
cur = conn.cursor()
cur.execute("""
 INSERT INTO books (name)
 VALUES (%s);
 """,
 'Da Vinci Code')
cur.close()