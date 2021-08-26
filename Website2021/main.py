from flask import Flask, render_template, abort, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from config import Config  # config now moved to its own file

app = Flask(__name__)
app.config.from_object(Config)  # applying all config to app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///WhoCares.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.secret_key = 'correcthorsebatterystaple'
db = SQLAlchemy(app)

WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = 'sup3r_secr3t_passw3rd'

import models
from forms import Add_Review


@app.route("/")
def home():
    return render_template("home.html")


# route for about page
@app.route("/about")
def about():
    return render_template("about.html")

# route for about page
@app.route("/search")
def search():
    return render_template("search.html")

# route for nav that gets included in template
@app.route("/nav")
def nav(womens_all):
    all_products = models.Products.query.order_by(models.Products.id).all()
    return render_template("nav.html", all_products=all_products)

# route for all who cares stores
@app.route("/our_stores")
def our_stores():
    return render_template("our_stores.html")

# route for contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# route for about page
@app.route("/terms_of_service")
def terms_of_service():
    return render_template("terms_of_service.html")

# route for refundpolicy
@app.route("/refund_policy")
def refund_policy():
    return render_template("refund_policy.html")

# route for work with us page
@app.route("/work_with_us")
def work_with_us():
    return render_template("work_with_us.html")


# route for shop landing page
@app.route("/shop")
def shop():
    all_products = models.Products.query.order_by(models.Products.id).all()
    return render_template("shop.html", all_products=all_products)


# route for all mens clothing
@app.route("/shop/mens")
def mens_filter():
    mens_all = (
        models.Products.query.order_by(models.Products.gender)
        .filter_by(gender="mens")
        .all()
    )
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

# route for all womens clothing
@app.route("/shop/womens")
def womens_shop_filter():
    womens_all = (
        models.Products.query.order_by(models.Products.gender)
        .filter_by(gender="womens")
        .all()
    )
    return render_template("womens_filter.html", womens_all=womens_all)


# mens shopping filter for differnt clothing types
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
def separate_products(id):
    sep = models.Products.query.filter_by(id=id).first()
    reviews = (
        models.Reviews.query.order_by(models.Reviews.id)
        .filter_by(associated_product=id)
        .all()
    )
    form = Add_Review()
    if request.method=='GET':  # did the browser ask to see the page
        return render_template('separate_products.html', form=form, sep=sep,reviews=reviews)
    else:
        if form.validate_on_submit():
            print("VALID")
            new_review = models.Reviews()
            new_review.name = form.name.data
            new_review.rating = form.rating.data
            new_review.comment = form.comment.data
            db.session.add(new_review)
            db.session.commit()
            return render_template("separate_products.html", sep=sep,form=form,reviews=reviews)
        else:
            print("INVALID")
            return render_template("separate_products.html", sep=sep, form=form,reviews=reviews)



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
