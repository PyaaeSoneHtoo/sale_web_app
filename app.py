from flask import Flask, render_template
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect("my_data.db")
    df = pd.read_sql_query("SELECT * FROM my_table", conn)
    conn.close()
    return df.to_html()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)