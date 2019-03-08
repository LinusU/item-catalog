#!/usr/bin/env python3
"""Backend of Item Catalog app."""

from flask import Flask, render_template

from item_catalog import dummydatabase

app = Flask(__name__)


@app.route('/')
def index():
    """Return index page.
    
    The index page presents:
    - a header with the title of the website and a button that takes 
    you to the login page. If you are logged in it logs you out.
    - a categories menu that displays all available categories.
    - a column with the latest items added.
    """
    category1 = dummydatabase.Category('Category one', 1)
    category2 = dummydatabase.Category('Category two', 2)
    category3 = dummydatabase.Category('Category three', 3)
    categories = [category1, category2, category3]
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


@app.route('/category/new/')
def newCategory():
    """Return page to add a NEW CATEGORY."""
    return render_template('index.html')


@app.route('/category/<int:categoryid>/edit/')
def editCategory(categoryid):
    """Return page to add a EDIT CATEGORY."""
    return render_template('index.html')


@app.route('/category/<int:categoryid>/delete/')
def deleteCategory(categoryid):
    """Return page to add a DELETE CATEGORY."""
    return render_template('index.html')


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
