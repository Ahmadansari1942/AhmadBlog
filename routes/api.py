from flask import Blueprint, jsonify, request
from models.article import Article

api = Blueprint('api', __name__)

@api.route('/articles')
def get_articles():
    category = request.args.get('category')
    sort = request.args.get('sort', 'date-desc')
    search = request.args.get('search', '')
    
    if search:
        articles = Article.search(search)
    elif category and category != 'all':
        articles = Article.get_by_category(category)
    else:
        articles = Article.get_all()
    
    # Sort
    reverse = sort.endswith('-desc')
    sort_key = sort.split('-')[0]
    
    if sort_key == 'date':
        articles.sort(key=lambda x: x['date'], reverse=reverse)
    elif sort_key == 'title':
        articles.sort(key=lambda x: x['title'], reverse=reverse)
    
    return jsonify(articles)

@api.route('/articles/<int:article_id>')
def get_article(article_id):
    article = Article.get_by_id(article_id)
    if article:
        return jsonify(article)
    return jsonify({'error': 'Article not found'}), 404

@api.route('/featured')
def get_featured():
    article = Article.get_featured()
    return jsonify(article)

@api.route('/stats')
def get_stats():
    articles = Article.get_all()
    categories = {}
    for article in articles:
        cat = article['category']
        categories[cat] = categories.get(cat, 0) + 1
    
    return jsonify({
        'total_articles': len(articles),
        'total_categories': len(categories),
        'categories': categories
    })
