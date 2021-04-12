from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config  # config now moved to its own file

app = Flask(__name__)
app.config.from_object(Config)  # applying all config to app
db = SQLAlchemy(app)

# note: this import is NOT at the top of the code because
# it can't be - models.py NEEDS 'db' to be initialised before
# it can be imported, and db needs 'app' - so against normal
# protocols (and PEP8), we do this import down here after
# 'app' and then 'db' have been created.
import models # moved to its own file - it didn't belong here

@app.route("/")
def home():
        return render_template("home.html")
        page_title="HOME"

#route for about page
@app.route("/about")
def about():
    return render_template("about.html")
    page_title="ABOUT"

@app.route("/our_stores")
def our_stores():
    return render_template("our_stores.html")
    page_title="OUR_STORES"

@app.route("/contact")
def contact():
    return render_template("contact.html")
    page_title="CONTACT"

@app.route("/terms_of_service")
def terms_of_service():
    return render_template("terms_of_service.html")
    page_title="TERMS_OF_SERVICE"

@app.route("/refund_policy")
def refund_policy():
    return render_template("refund_policy.html")
    page_title="REFUND_POLICY"

@app.route("/work_with_us")
def work_with_us():
    return render_template("work_with_us.html")
    page_title="WORK_WITH_US"

@app.route("/shop")
def shop():
    all_products = models.Products.query.all()
    return render_template("shop.html",all_products=all_products)


@app.route('/products/<id>')
def separate_products(id):
        product = models.Pizza.query.filter_by(id=id).first_or_404()
        return render_template("separate_products.html")


#route for sell page
@app.route("/sell")
def sell():
    return render_template("sell.html")


#reroutes 404 errrors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
