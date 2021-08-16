from main import db

class Products(db.Model):
  __tablename__ = 'Products'
  id = db.Column(db.String, primary_key=True)
  product_name = db.Column(db.String(80))
  description = db.Column(db.Text(250))
  price = db.Column(db.Text(250))
  colour = db.Column(db.Text(250))
  size = db.Column(db.Text(250))
  brand = db.Column(db.Text(250))
  image1 = db.Column(db.String(120))
  gender = db.Column(db.Text(250))
  product_type = db.Column(db.Text(250))
  store_availability = db.Column(db.String(80))



class Customer(db.Model):
  __tablename__ = 'Customer'
  id = db.Column(db.String, primary_key=True)
  customer_name = db.Column(db.String(80))
  customer_email = db.Column(db.Text(250))
  customer_phone = db.Column(db.Text(250))


class User(db.Model):
  __tablename__ = 'User'
  id = db.Column(db.String, primary_key=True)
  first_name = db.Column(db.String(80))
  last_name = db.Column(db.String(80))
  mobile = db.Column(db.Text(250))
  email = db.Column(db.Text(250))
  image = db.Column(db.String(80))
  size = db.Column(db.Text(250))
  gender = db.Column(db.Text(250))

class Reviews(db.Model):
  __tablename__ = 'Reviews'
  id = db.Column(db.String, primary_key=True)
  associated_product = db.Column(db.String(100), db.ForeignKey('Products.id'), nullable = False)
  name = db.Column(db.String(100))
  rating = db.Column(db.Integer)
  comment = db.Column(db.Text(250))


  def __repr__(self):
      return '<Comment %r>'%self.id
