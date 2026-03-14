from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from models.article import Article
import os
from werkzeug.utils import secure_filename
from config import Config

articles = Blueprint('articles', __name__)

@articles.route('/<int:article_id>')
def view(article_id):
    article = Article.get_by_id(article_id)
    if not article:
        return render_template('404.html'), 404
    related = [a for a in Article.get_all() if a['category'] == article['category'] and a['id'] != article_id][:3]
    return render_template('article.html', article=article, related=related)

@articles.route('/category/<string:category>')
def category(category):
    articles_list = Article.get_by_category(category)
    return render_template('category.html', articles=articles_list, category=category)

@articles.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        excerpt = request.form.get('excerpt')
        content = request.form.get('content')
        category = request.form.get('category')
        author = request.form.get('author')
        read_time = request.form.get('read_time')
        
        image = request.form.get('image_url', 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&q=80')
        
        if 'image_file' in request.files:
            file = request.files['image_file']
            if file and file.filename:
                filename = secure_filename(file.filename)
                filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
                file.save(filepath)
                image = f'/static/uploads/{filename}'
        
        article_data = {
            'title': title,
            'excerpt': excerpt,
            'content': content,
            'category': category,
            'image': image,
            'author': author,
            'read_time': read_time
        }
        
        Article.create(article_data)
        flash('Article created successfully!', 'success')
        return redirect(url_for('main.index'))
    
    return render_template('create_article.html')

@articles.route('/<int:article_id>/edit', methods=['GET', 'POST'])
def edit(article_id):
    article = Article.get_by_id(article_id)
    if not article:
        return render_template('404.html'), 404
    
    if request.method == 'POST':
        article['title'] = request.form.get('title')
        article['excerpt'] = request.form.get('excerpt')
        article['content'] = request.form.get('content')
        article['category'] = request.form.get('category')
        article['author'] = request.form.get('author')
        article['read_time'] = request.form.get('read_time')
        
        if request.form.get('image_url'):
            article['image'] = request.form.get('image_url')
        
        Article.update(article_id, article)
        flash('Article updated successfully!', 'success')
        return redirect(url_for('articles.view', article_id=article_id))
    
    return render_template('edit_article.html', article=article)

@articles.route('/<int:article_id>/delete', methods=['POST'])
def delete(article_id):
    Article.delete(article_id)
    flash('Article deleted successfully!', 'success')
    return redirect(url_for('main.index'))
