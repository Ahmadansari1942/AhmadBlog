from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.article import Article

admin = Blueprint('admin', __name__)

@admin.route('/admin')
def dashboard():
    articles = Article.get_all()
    
    # Calculate statistics
    total_articles = len(articles)
    categories = {}
    authors = {}
    
    for article in articles:
        cat = article['category']
        categories[cat] = categories.get(cat, 0) + 1
        
        author = article['author']
        authors[author] = authors.get(author, 0) + 1
    
    # Sort by count
    sorted_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)
    sorted_authors = sorted(authors.items(), key=lambda x: x[1], reverse=True)
    
    stats = {
        'total_articles': total_articles,
        'total_categories': len(categories),
        'total_authors': len(authors),
        'categories': sorted_categories,
        'top_authors': sorted_authors[:5]
    }
    
    return render_template('admin.html', articles=articles, stats=stats)

@admin.route('/admin/articles')
def articles_list():
    articles = Article.get_all()
    return render_template('admin_articles.html', articles=articles)

@admin.route('/admin/article/<int:article_id>/toggle-featured', methods=['POST'])
def toggle_featured(article_id):
    articles = Article.get_all()
    for article in articles:
        if article['id'] == article_id:
            article['featured'] = not article.get('featured', False)
            Article.save_all(articles)
            flash('Featured status updated!', 'success')
            break
    return redirect(url_for('admin.dashboard'))

@admin.route('/admin/search')
def search():
    query = request.args.get('q', '')
    articles = Article.search(query) if query else []
    return render_template('admin_search.html', articles=articles, query=query)
