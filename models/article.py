import json
import os
from datetime import datetime
from config import Config

class Article:
    def __init__(self, data=None):
        if data:
            self.id = data.get('id')
            self.title = data.get('title')
            self.excerpt = data.get('excerpt')
            self.content = data.get('content')
            self.category = data.get('category')
            self.image = data.get('image')
            self.author = data.get('author')
            self.date = data.get('date')
            self.read_time = data.get('read_time')
            self.featured = data.get('featured', False)
    
    @staticmethod
    def get_data_path():
        return os.path.join(Config.DATA_FOLDER, 'articles.json')
    
    @staticmethod
    def get_all():
        try:
            with open(Article.get_data_path(), 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return Article.get_default_articles()
    
    @staticmethod
    def get_by_id(article_id):
        articles = Article.get_all()
        for article in articles:
            if article['id'] == article_id:
                return article
        return None
    
    @staticmethod
    def get_by_category(category):
        articles = Article.get_all()
        return [a for a in articles if a['category'] == category]
    
    @staticmethod
    def get_featured():
        articles = Article.get_all()
        for article in articles:
            if article.get('featured'):
                return article
        return articles[0] if articles else None
    
    @staticmethod
    def search(query):
        articles = Article.get_all()
        query = query.lower()
        return [
            a for a in articles 
            if query in a['title'].lower() 
            or query in a['excerpt'].lower() 
            or query in a['author'].lower()
        ]
    
    @staticmethod
    def create(data):
        articles = Article.get_all()
        new_id = max([a['id'] for a in articles], default=0) + 1
        data['id'] = new_id
        data['date'] = datetime.now().strftime('%Y-%m-%d')
        data['featured'] = False
        articles.insert(0, data)
        Article.save_all(articles)
        return data
    
    @staticmethod
    def update(article_id, data):
        articles = Article.get_all()
        for i, article in enumerate(articles):
            if article['id'] == article_id:
                data['id'] = article_id
                articles[i] = data
                Article.save_all(articles)
                return data
        return None
    
    @staticmethod
    def delete(article_id):
        articles = Article.get_all()
        articles = [a for a in articles if a['id'] != article_id]
        Article.save_all(articles)
        return True
    
    @staticmethod
    def save_all(articles):
        with open(Article.get_data_path(), 'w', encoding='utf-8') as f:
            json.dump(articles, f, indent=2, ensure_ascii=False)
    
    @staticmethod
    def get_default_articles():
        return [
            {
                "id": 1,
                "title": "Building Scalable Web Applications with Python FastAPI",
                "excerpt": "Learn how to create high-performance APIs using Python's fastest framework.",
                "content": "Python has become one of the most popular languages for web development, and FastAPI has emerged as a game-changer in building APIs. This comprehensive guide walks you through setting up a production-ready FastAPI application with proper architecture, authentication, and database integration.",
                "category": "apps",
                "image": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&q=80",
                "author": "Ahmad Hassan",
                "date": "2024-01-15",
                "read_time": "8 min read",
                "featured": True
            },
            {
                "id": 2,
                "title": "The Art of Minimalist UI Design",
                "excerpt": "Discover the principles behind creating stunning user interfaces with less.",
                "content": "Minimalist design has transcended trend status to become a fundamental approach in modern UI/UX. This article explores the philosophy of 'less but better' and how to apply it effectively.",
                "category": "art",
                "image": "https://images.unsplash.com/photo-1545235617-9465d2a55698?w=800&q=80",
                "author": "Sarah Chen",
                "date": "2024-01-12",
                "read_time": "6 min read",
                "featured": False
            },
            {
                "id": 3,
                "title": "10 Must-Read Books for Software Engineers",
                "excerpt": "Curated reading list covering system design, clean code, and career growth.",
                "content": "Continuous learning is the hallmark of a great software engineer. This carefully curated list spans technical depth, architectural wisdom, and career navigation.",
                "category": "books",
                "image": "https://images.unsplash.com/photo-1512820790803-83ca734da794?w=800&q=80",
                "author": "Michael Torres",
                "date": "2024-01-10",
                "read_time": "10 min read",
                "featured": False
            },
            {
                "id": 4,
                "title": "Mindfulness Practices for Remote Workers",
                "excerpt": "Working from home blurs boundaries. Learn practical mindfulness techniques.",
                "content": "The shift to remote work has brought unprecedented challenges to our mental well-being. This guide introduces practical mindfulness techniques specifically designed for remote workers.",
                "category": "health",
                "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=800&q=80",
                "author": "Emma Williams",
                "date": "2024-01-08",
                "read_time": "7 min read",
                "featured": False
            },
            {
                "id": 5,
                "title": "Ancient Rome: Engineering Marvels",
                "excerpt": "Explore the revolutionary engineering achievements of ancient Rome.",
                "content": "The Roman Empire's engineering achievements remain among humanity's most impressive accomplishments. From aqueducts to roads, Roman engineers solved problems we still face today.",
                "category": "history",
                "image": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800&q=80",
                "author": "James Mitchell",
                "date": "2024-01-05",
                "read_time": "12 min read",
                "featured": False
            },
            {
                "id": 6,
                "title": "The Evolution of Sci-Fi Cinema",
                "excerpt": "Trace the visual and thematic evolution of science fiction in film.",
                "content": "Science fiction cinema has always been a mirror reflecting society's hopes and fears about the future. From Metropolis to Dune, the genre has evolved alongside our technological capabilities.",
                "category": "movies",
                "image": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&q=80",
                "author": "Alex Rivera",
                "date": "2024-01-03",
                "read_time": "9 min read",
                "featured": False
            },
            {
                "id": 7,
                "title": "Hidden Gems of Southeast Asia",
                "excerpt": "Escape the tourist crowds and discover authentic experiences.",
                "content": "Beyond the famous temples of Angkor Wat and beaches of Thailand lies a Southeast Asia few tourists ever see. This guide takes you to remote villages and hidden waterfalls.",
                "category": "travel",
                "image": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&q=80",
                "author": "Nina Patel",
                "date": "2024-01-01",
                "read_time": "11 min read",
                "featured": False
            },
            {
                "id": 8,
                "title": "Web Performance Optimization Guide",
                "excerpt": "Speed isn't a feature, it's a requirement. Master Core Web Vitals.",
                "content": "In an era where users abandon sites that take more than three seconds to load, performance optimization isn't optional. This comprehensive guide covers everything from critical rendering path optimization.",
                "category": "web",
                "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&q=80",
                "author": "David Kim",
                "date": "2023-12-28",
                "read_time": "14 min read",
                "featured": False
            },
            {
                "id": 9,
                "title": "Docker and Kubernetes: Zero to Production",
                "excerpt": "Container orchestration demystified for modern deployments.",
                "content": "Containerization has revolutionized how we build, ship, and run applications. This tutorial takes you from Docker basics to advanced Kubernetes deployments.",
                "category": "apps",
                "image": "https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?w=800&q=80",
                "author": "Ahmad Hassan",
                "date": "2023-12-25",
                "read_time": "15 min read",
                "featured": False
            },
            {
                "id": 10,
                "title": "Color Theory for Digital Designers",
                "excerpt": "Beyond the color wheel: psychological impact and accessibility.",
                "content": "Color is one of the most powerful tools in a designer's arsenal. This article explores the psychological effects of different hues and practical techniques for creating harmonious palettes.",
                "category": "art",
                "image": "https://images.unsplash.com/photo-1541701494587-cb58502866ab?w=800&q=80",
                "author": "Sofia Martinez",
                "date": "2023-12-22",
                "read_time": "8 min read",
                "featured": False
            },
            {
                "id": 11,
                "title": "The Psychology of Habit Formation",
                "excerpt": "Science-backed strategies for building positive habits.",
                "content": "Understanding the neuroscience behind habit formation is the key to lasting behavior change. This article breaks down the habit loop and shows you how to hack it for personal growth.",
                "category": "health",
                "image": "https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=800&q=80",
                "author": "Dr. Lisa Park",
                "date": "2023-12-20",
                "read_time": "9 min read",
                "featured": False
            },
            {
                "id": 12,
                "title": "Exploring the Silk Road Today",
                "excerpt": "Follow the path of merchants through Central Asia.",
                "content": "The Silk Road wasn't just a trade route—it was the internet of the ancient world. This travelogue follows modern paths through the historic Silk Road cities of Samarkand and Bukhara.",
                "category": "travel",
                "image": "https://images.unsplash.com/photo-1539650116574-8efeb43e2750?w=800&q=80",
                "author": "Omar Farouk",
                "date": "2023-12-18",
                "read_time": "10 min read",
                "featured": False
            },
            {
                "id": 13,
                "title": "Machine Learning Fundamentals",
                "excerpt": "Demystifying ML concepts without heavy math.",
                "content": "Machine learning can seem intimidating, but the core concepts are more accessible than you might think. This beginner-friendly guide explains supervised and unsupervised learning.",
                "category": "apps",
                "image": "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=800&q=80",
                "author": "Rachel Green",
                "date": "2023-12-15",
                "read_time": "12 min read",
                "featured": False
            },
            {
                "id": 14,
                "title": "Modern JavaScript ES2024 Features",
                "excerpt": "Stay current with the latest JavaScript enhancements.",
                "content": "JavaScript continues to evolve rapidly, and ES2024 brings exciting new features that will change how you write code. From new array methods to syntax improvements.",
                "category": "web",
                "image": "https://images.unsplash.com/photo-1579468118864-1b9ea3c0db4a?w=800&q=80",
                "author": "Chris Johnson",
                "date": "2023-12-12",
                "read_time": "8 min read",
                "featured": False
            },
            {
                "id": 15,
                "title": "The Renaissance of Vinyl Records",
                "excerpt": "Analog audio in a digital age explained.",
                "content": "In an era of infinite streaming, vinyl records have made an unexpected comeback. This isn't just nostalgia—there are legitimate reasons audiophiles are drawn to the format.",
                "category": "other",
                "image": "https://images.unsplash.com/photo-1483412033650-1015ddeb83d1?w=800&q=80",
                "author": "Marcus Webb",
                "date": "2023-12-10",
                "read_time": "7 min read",
                "featured": False
            },
            {
                "id": 16,
                "title": "Python Automation Scripts for Daily Tasks",
                "excerpt": "Automate your boring tasks with these Python scripts.",
                "content": "Learn how to write Python scripts that automate your daily repetitive tasks. From file organization to email automation, these practical examples will save you hours of work.",
                "category": "apps",
                "image": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&q=80",
                "author": "Ahmad Hassan",
                "date": "2023-12-08",
                "read_time": "11 min read",
                "featured": False
            },
            {
                "id": 17,
                "title": "Classic Literature That Changed the World",
                "excerpt": "Timeless books that shaped human thought and society.",
                "content": "From Shakespeare to Tolstoy, certain literary works have fundamentally altered how we see ourselves and our world. Explore these masterpieces and understand their lasting impact.",
                "category": "books",
                "image": "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=800&q=80",
                "author": "Elizabeth Moore",
                "date": "2023-12-05",
                "read_time": "13 min read",
                "featured": False
            },
            {
                "id": 18,
                "title": "The Rise of Independent Cinema",
                "excerpt": "How indie films are reshaping the movie industry.",
                "content": "Independent filmmakers are challenging Hollywood's dominance with innovative storytelling and fresh perspectives. Discover the movement that's democratizing cinema.",
                "category": "movies",
                "image": "https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=800&q=80",
                "author": "Jordan Lee",
                "date": "2023-12-02",
                "read_time": "8 min read",
                "featured": False
            },
            {
                "id": 19,
                "title": "Digital Nomad Guide to Europe",
                "excerpt": "Best cities, visas, and tips for remote work in Europe.",
                "content": "Everything you need to know about working remotely while traveling through Europe. From affordable cities to reliable WiFi, plan your nomadic adventure.",
                "category": "travel",
                "image": "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?w=800&q=80",
                "author": "Lucas Schmidt",
                "date": "2023-11-28",
                "read_time": "14 min read",
                "featured": False
            },
            {
                "id": 20,
                "title": "Building a Personal Brand Online",
                "excerpt": "Strategies for establishing your digital presence.",
                "content": "In the digital age, your online presence is your calling card. Learn how to build an authentic personal brand that opens doors and creates opportunities.",
                "category": "other",
                "image": "https://images.unsplash.com/photo-1611162616475-46b635cb6868?w=800&q=80",
                "author": "Maya Johnson",
                "date": "2023-11-25",
                "read_time": "9 min read",
                "featured": False
            }
        ]
