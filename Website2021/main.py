import sqlite3
from flask import Flask, render_template
from flask import g

app = Flask(__name__)


@app.route("/")
def home():
        conn = sqlite3.connect('CreatePizza.db')
        c = conn.cursor()
        #query selects all
        c.execute("SELECT * FROM Pizza ;")
        fetch = c.fetchall()
        conn.close()
        return render_template("home.html", fetch=fetch)

#route for about
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/sell")
def sell():
    return render_template("sell.html")

@app.route('/hello/<int:id>')
def single_discountbox(id):
        conn = sqlite3.connect('AllFruitsDatabase.db')
        c = conn.cursor()
        #query selects all from Fruit table and grabs corelating information for the displayed discount box id
        c.execute("SELECT * FROM DiscountBox WHERE id=?;",(id,))
        discountboxes = c.fetchone()
        conn.close()
        return render_template("single_discountbox.html", discountboxes=discountboxes)

#reroutes 404 errrors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
