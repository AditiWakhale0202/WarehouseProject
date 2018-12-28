import flask
from flask import render_template
from flask import redirect,flash,request
app = flask.Flask(__name__)


def load():
    #flash("Hello People")
    return render_template('index.html')


def create():
    return render_template('create_warehouse.html')


def put_data():
    id = request.form['p_id']
    name = request.form['p_name']
    brand = request.form['p_brand']
    category = request.form['p_cat']
    price = request.form['p_price']
    print price
    import pymongo, json
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


app.add_url_rule('/my_app/load/', 'load', load)
app.add_url_rule('/my_app/show', 'show', show)
app.add_url_rule('/my_app/create', 'create', create, methods=['POST'])
app.add_url_rule('/my_app/put_data', 'put_data', put_data, methods=['POST'])
app.add_url_rule('/my_app/github', 'github', github)

if __name__ == '__main__':
    app.run()