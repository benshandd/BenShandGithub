from flask import Flask, render_template,url_for, request

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from config import Config  # config now moved to its own file

app = Flask(__name__)
app.config.from_object(Config)  # applying all config to app
db = SQLAlchemy(app)

import models

@app.route("/", methods=['GET', 'POST'], defaults={"page": 1})
def home():
        return render_template("home.html")


#route for about page
@app.route("/about")
def about():
    return render_template("about.html")


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

#######################################
@app.route("/shop")
def shop():
    all_products = models.Products.query.order_by(models.Products.id).all()
    return render_template("shop.html",all_products=all_products)



@app.route('/products/<id>')
def separate_products(id):
    sep= models.Products.query.filter_by(id=id).first_or_404()
    return render_template('separate_products.html', sep=sep)


#route for sell page
@app.route("/sell")
def sell():
    return render_template("sell.html")

@app.route('/search/<int:page>', methods=['GET', 'POST'])
def search(page):
    page = page
    pages = 5
    #employees = Employees.query.filter().all()
    #employees = Employees.query.paginate(page,pages,error_out=False)
    employees = models.Products.query.order_by(models.Products.id.asc()).paginate(page,pages,error_out=False)  #desc()
    if request.method == 'POST' and 'tag' in request.form:
       tag = request.form["tag"]
       search = "%{}%".format(tag)
       #employees = Employees.query.filter(Employees.fullname.like(search)).paginate(per_page=pages, error_out=False) # LIKE: query.filter(User.name.like('%ednalan%'))
       #employees = Employees.query.filter(Employees.fullname == 'Tiger Nixon').paginate(per_page=pages, error_out=True) # equals: query.filter(User.name == 'ednalan')
       #employees = Employees.query.filter(Employees.fullname.in_(['rai', 'kenshin', 'Ednalan'])).paginate(per_page=pages, error_out=True) # IN: query.filter(User.name.in_(['rai', 'kenshin', 'Ednalan']))
       #employees = Employees.query.filter(Employees.fullname == 'Tiger Nixon', Employees.position == 'System Architect').paginate(per_page=pages, error_out=True) # AND: query.filter(User.name == 'ednalan', User.fullname == 'clyde ednalan')
       employees = models.Products.query.filter(or_(models.Products.product_name == 'Shirt', Employees.product_name == 'Pants')).paginate(per_page=pages, error_out=True) # OR: from sqlalchemy import or_  filter(or_(User.name == 'ednalan', User.name == 'caite'))
       return render_template('search.html', shirts=shirts, tag=tag)
    return render_template('search.html', shirts=shirts)

#reroutes 404 errrors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
