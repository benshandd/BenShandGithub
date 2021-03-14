import sqlite3
from flask import Flask, render_template
from flask import g

app = Flask(__name__)


@app.route("/")
def home():
        conn = sqlite3.connect('CreatePizza.db')
        c = conn.cursor()
        #query selects all from DiscountBox table
        c.execute("SELECT * FROM Pizza ;")
        fetch = c.fetchall()
        conn.close()
        return render_template("home.html", fetch=fetch)


if __name__ == "__main__":
    app.run(debug=True)
