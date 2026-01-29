# db_probe.py
from dotenv import load_dotenv
import os, psycopg, sys, traceback

load_dotenv()
host = os.getenv("PGHOST","localhost")
port = int(os.getenv("PGPORT","55432"))
db   = os.getenv("PGDATABASE","netspider")
user = os.getenv("PGUSER","postgres")
pw   = os.getenv("PGPASSWORD","password")

print(f"Trying {user}@{host}:{port}/{db}")
try:
    conn = psycopg.connect(
        host=host, port=port, dbname=db, user=user, password=pw,
        connect_timeout=5,
    )
    with conn, conn.cursor() as cur:
        cur.execute("select current_database(), current_user;")
        print("CONNECTED:", cur.fetchone())
except Exception as e:
    print("FAILED:", type(e).__name__, e)
    traceback.print_exc()
    sys.exit(1)
