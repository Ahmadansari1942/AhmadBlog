from flask import Blueprint, render_template, request
from models.article import Article

main = Blueprint('main', __name__)

@main.route('/')
def index():
    articles = Article.get_all()
    featured = Article.get_featured()
    return render_template('index.html', articles=articles, featured=featured)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/search')
def search():
    query = request.args.get('q', '')
    results = Article.search(query) if query else []
    return render_template('search.html', results=results, query=query)
