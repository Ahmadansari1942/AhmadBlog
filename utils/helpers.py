from datetime import datetime

def format_date(date_str):
    """Format date string to readable format"""
    date = datetime.strptime(date_str, '%Y-%m-%d')
    return date.strftime('%B %d, %Y')

def truncate_text(text, length=150):
    """Truncate text to specified length"""
    if len(text) <= length:
        return text
    return text[:length].rsplit(' ', 1)[0] + '...'

def get_category_color(category):
    """Get color for category"""
    colors = {
        'apps': {'bg': '#22c55e', 'text': 'white'},
        'art': {'bg': '#ec4899', 'text': 'white'},
        'books': {'bg': '#f97316', 'text': 'white'},
        'health': {'bg': '#14b8a6', 'text': 'white'},
        'history': {'bg': '#a855f7', 'text': 'white'},
        'movies': {'bg': '#ef4444', 'text': 'white'},
        'travel': {'bg': '#3b82f6', 'text': 'white'},
        'web': {'bg': '#06b6d4', 'text': 'white'},
        'other': {'bg': '#6b7280', 'text': 'white'}
    }
    return colors.get(category, colors['other'])
