import flask
from flask import render_template
from flask import redirect, request
from login_check import is_login
app = flask.Flask(__name__)


def login():
    return render_template('login.html')


def insert_data():
    return render_template('insertdata_page.html')


def verify_login():
    if request.method == 'GET':
        return "You need to login first"
    user = request.form['u_name']
    password = request.form['pwd']
    import pymongo, json
    client = pymongo.MongoClient()
    db = client.mydb
    collection = db.merchant
    for post in collection.find({'uname': user}):
        if password == post['password']:
            return render_template('index.html', uname=user)
    else:
        render_template('login.html')


def put_data():
    id = request.form['p_id']
    name = request.form['p_name']
    brand = request.form['p_brand']
    category = request.form['p_cat']
    price = request.form['p_price']
    import pymongo,json
    client = pymongo.MongoClient()
    db = client.mydb
    collection = db.warehouse
    collection.insert({'id': id, 'product': name, 'brand': brand, 'category': category, 'price': price})
    return "Collection Inserted Successfully"


def show():
    warehouse_list = []
    import pymongo, json
    client = pymongo.MongoClient()
    db = client.mydb
    collection = db.warehouse
    for post in collection.find():
        post = "Product is " + post['product'] + " of brand " + post['brand']
        warehouse_list.append(post)
    return json.dumps(warehouse_list)


def github():
    return redirect('https://alexwohlbruck.github.io/cat-facts/')


app.add_url_rule('/my_app/home/', 'login', login)
app.add_url_rule('/my_app/verify', 'verify', verify_login, methods=['GET','POST'])
app.add_url_rule('/my_app/show', 'show', show)
app.add_url_rule('/my_app/insert', 'insert', insert_data, methods=['POST'])
app.add_url_rule('/my_app/put_data', 'put_data', put_data, methods=['POST'])
#  keeping it as first example
app.add_url_rule('/my_app/github', 'github', github)

if __name__ == '__main__':
    app.run()