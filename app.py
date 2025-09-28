from flask import Flask
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    try:
        conn = sqlite3.connect("my_data.db")
        df = pd.read_sql_query("SELECT * FROM my_table", conn)
        conn.close()
        return df.to_html(classes="table table-striped")
    except Exception as e:
        return f"<h3>Error: {e}</h3>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)