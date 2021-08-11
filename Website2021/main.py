from flask import Flask, render_template, url_for, request

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


# route for about page
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/nav")
def nav(womens_all):
    ya_dig = models.Products.query.order_by(models.Products.id).first()

    all_products = models.Products.query.order_by(models.Products.id).all()
    return render_template("nav.html", all_products=all_products, ya_dig=ya_dig)


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


# shop landing page
@app.route("/shop")
def shop():
    all_products = models.Products.query.order_by(models.Products.id).all()
    return render_template("shop.html", all_products=all_products)


#######################################
@app.route("/shop/mens")
def mens_filter():
    mens_all = (
        models.Products.query.order_by(models.Products.gender)
        .filter_by(gender="mens")
        .all()
    )
    # filter_first = models.Products.query.filter_by(gender="mens").first()
    return render_template("mens_filter.html", mens_all=mens_all)


# mens shopping filter for differnt clothing types
@app.route("/shop/mens/<product_type>")
def product_type_filter(product_type):
    product_type = (
        models.Products.query.order_by(models.Products.product_type)
        .filter_by(product_type=product_type)
        .filter_by(gender="mens")
        .all()
    )
    return render_template("product_type_filter.html", product_type=product_type)


@app.route("/shop/womens")
def womens_shop_filter():
    womens_all = (
        models.Products.query.order_by(models.Products.gender)
        .filter_by(gender="womens")
        .all()
    )
    # filter_first = models.Products.query.filter_by(gender="mens").first()
    return render_template("womens_filter.html", womens_all=womens_all)


# womens shopping filter for differnt clothing types
@app.route("/shop/womens/<product_type>")
def womens_product_type_filter(product_type):
    product_type = (
        models.Products.query.order_by(models.Products.product_type)
        .filter_by(product_type=product_type)
        .filter_by(gender="womens")
        .all()
    )
    return render_template("product_type_filter.html", product_type=product_type)


@app.route("/shop/brands/<brand>")
def separate_brands(brand):
    all_brands = models.Products.query.filter_by(brand=brand).all()
    return render_template("separate_brands.html", all_brands=all_brands)


# seprate products pages
@app.route("/products/<id>", methods=['GET','POST'])
def separate_products(id,add_review):
    sep = models.Products.query.filter_by(id=id).first_or_404()
    review = models.Reviews.query.filter_by(comment.add_review==id).first()
    return render_template("separate_products.html", sep=sep)


# route for sell page
@app.route("/sell")
def sell():
    return render_template("sell.html")


# reroutes 404 errrors
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
