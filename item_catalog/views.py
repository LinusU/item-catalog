#!/usr/bin/env python3
"""Backend of Item Catalog app."""

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from item_catalog import dummydatabase
from item_catalog.models import Base, Category, Item

app = Flask(__name__)

engine = create_engine('sqlite:///itemcatalog.db',
                       connect_args={'check_same_thread': False})
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def index():
    """Return index page.
    
    The index page presents:
    - a header with the title of the website and a button that takes 
    you to the login page. If you are logged in it logs you out.
    - a categories menu that displays all available categories.
    - a column with the latest items added.
    """
    categories = session.query(Category).all()
    return render_template('landingpage.html', categories=categories)


@app.route('/login/')
def login():
    """Return page with login options."""
    return render_template('landingpage.html')


@app.route('/categories/')
def showCategories():
    """Return categories page."""
    return render_template('index.html')


@app.route('/category/<int:categoryid>/')
def showCategory(categoryid):
    """Return page with all items in a category."""
    category1 = dummydatabase.Category('Category one', 1)
    category2 = dummydatabase.Category('Category two', 2)
    category3 = dummydatabase.Category('Category three', 3)
    categories = [category1, category2, category3]
    return render_template('landingpage.html', categories=categories)


@app.route('/category/new/', methods=['GET','POST'])
def newCategory():
    """Return page to add a NEW CATEGORY."""
    if request.method == 'POST':
        pass
        return redirect(url_for('index'))
    elif request.method == 'GET':
        return render_template('index.html')


@app.route('/category/<int:categoryid>/edit/')
def editCategory(categoryid):
    """Return page to add a EDIT CATEGORY."""
    return render_template('index.html')


@app.route('/category/<int:categoryid>/delete/')
def deleteCategory(categoryid):
    """Return page to add a DELETE CATEGORY."""
    category1 = dummydatabase.Category('Category one', 1)
    category2 = dummydatabase.Category('Category two', 2)
    category3 = dummydatabase.Category('Category three', 3)
    categories = [category1, category2, category3]
    return render_template('categorydelete.html', category=categories[0])


@app.route('/category/<int:categoryid>/item/<int:itemid>/')
def showItems(categoryid, itemid):
    """Return page with description of specific item."""
    return render_template('index.html')


@app.route('/category/<int:categoryid>/item/new/')
def newItem(categoryid):
    """Return page to add a new item to the category."""
    return render_template('index.html')


@app.route('/category/<int:categoryid>/item/<int:itemid>/edit/')
def editItem(categoryid, itemid):
    """Return page to EDIT specific ITEM."""
    return render_template('index.html')


@app.route('/category/<int:categoryid>/item/<int:itemid>/delete/')
def deleteItem(categoryid, itemid):
    """Return page to DELETE specific ITEM."""
    return render_template('index.html')


@app.route('/category/<int:categoryid>/JSON/')
def categoryAPIEndpoint(categoryid):
    """Return page to display JSON formatted information of category."""
    return render_template('index.html')


@app.route('/category/<int:categoryid>/item/<int:itemid>/JSON/')
def itemAPIEndpoint(categoryid, itemid):
    """Return page to display JSON formatted information of item."""
    return render_template('index.html')


def main():
    """Serve up a webpage on localhost."""
    app.secret_key = 'key'
    app.run('localhost', port=8080, debug=True)


if __name__ == "__main__":
    main()
