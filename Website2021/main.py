from flask import Flask, render_template,url_for, request

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from config import Config  # config now moved to its own file

app = Flask(__name__)
app.config.from_object(Config)  # applying all config to app
db = SQLAlchemy(app)

import models

@app.route("/")
def home():
    return render_template("home.html")


#route for about page
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/nav")
def nav(womens_all):
    womens_all = models.Products.query.order_by(models.Products.product_type).filter_by(gender="womens").first()
    return render_template("nav.html",womens_all=womens_all)


@app.route("/our_stores")
def our_stores():
    return render_template("our_stores.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/terms_of_service")
def terms_of_service():
    return render_template("terms_of_service.html")


@app.route("/refund_policy")
def refund_policy():
    return render_template("refund_policy.html")


@app.route("/work_with_us")
def work_with_us():
    return render_template("work_with_us.html")

#shop landing page
@app.route("/shop")
def shop():
    all_products = models.Products.query.order_by(models.Products.id).all()
    return render_template("shop.html",all_products=all_products)

#######################################
@app.route("/shop/<string:mens_all>")
def shop_filter(mens_all):
    mens_all = models.Products.query.order_by(models.Products.id).filter_by(gender="mens").all()
    filter = models.Products.query.order_by(models.Products.gender).first()
    #filter_first = models.Products.query.filter_by(gender="mens").first()
    return render_template("shop_filter.html", mens_all=mens_all)

@app.route("/shop<string:filter_tshirts>")
def filter_product_type(filter_tshirts):
    filter_tshirts = models.Products.query.order_by(models.Products.id).filter_by(product_type="t-shirt").all()
    return render_template("filter_product_type.html", filter_tshirts=filter_tshirts)
#filter_first=filter_first

#@app.route("/shop/<string:gender>")
#def shop_filter(gender):
    #gender = models.Products.query.filter_by(gender="womens").all()
    #return render_template("shop_filter.html",gender=gender)

#seprate products pages
@app.route('/products/<id>')
def separate_products(id):
    sep= models.Products.query.filter_by(id=id).first_or_404()
    return render_template('separate_products.html', sep=sep)


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
