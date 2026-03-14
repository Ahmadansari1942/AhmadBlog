(Professional README)
AhmadBlog Logo

AhmadBlog
A Modern Python Flask Blog Application

PythonFlaskLicenseStatus

Features • Demo • Installation • Usage • Deployment • Contributing

About The Project
AhmadBlog is a beautifully designed, fully functional blog application built with Python Flask. It features a modern dark theme, smooth animations, and a responsive design that works perfectly on all devices.

Created By
Ahmad Ansari - Full Stack Developer

GitHub: @ahmadansari
Passionate about creating beautiful, functional web applications
Features
Core Features
Modern UI/UX - Stunning dark theme with smooth animations
Responsive Design - Works on desktop, tablet, and mobile
9 Categories - Apps, Art, Books, Health, History, Movies, Travel, Web, Other
Featured Articles - Highlight important content
Search Functionality - Find articles quickly
CRUD Operations - Create, Read, Update, Delete articles
Admin Features
Admin Dashboard - Manage all articles from one place
Statistics - View article counts by category
Quick Actions - Edit, Delete articles easily
Technical Features
Flask Backend - Lightweight Python framework
JSON Database - No SQL required, easy to deploy
RESTful API - JSON endpoints for integration
Image Support - URL or file upload for article images
SEO Friendly - Proper meta tags and structure
Demo
Screenshots
Home Page
Home Page

Article Page
Article Page

Create Article
Create Article

Admin Dashboard
Admin Dashboard

Installation
Prerequisites
Python 3.10 or higher
pip (Python package manager)
Quick Start
Clone the repository
git clone https://github.com/ahmadansari/AhmadBlog.gitcd AhmadBlog
Create virtual environment
bash

python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
Install dependencies
bash

pip install -r requirements.txt
Run the application
bash

python run.py
Open in browser
text

http://localhost:5000
Project Structure
text

AhmadBlog/
├── app.py                    # Flask app factory
├── config.py                 # Configuration settings
├── requirements.txt          # Python dependencies
├── run.py                    # Application entry point
├── README.md                 # Documentation
├── .gitignore               # Git ignore file
├── .env.example             # Environment variables template
├── Procfile                 # Heroku deployment
├── runtime.txt              # Python version for Heroku
│
├── models/
│   ├── __init__.py
│   └── article.py           # Article model
│
├── routes/
│   ├── __init__.py
│   ├── main.py              # Main routes
│   ├── articles.py          # Article routes
│   ├── admin.py             # Admin routes
│   └── api.py               # API routes
│
├── templates/
│   ├── base.html            # Base template
│   ├── index.html           # Home page
│   ├── article.html         # Single article
│   ├── category.html        # Category page
│   ├── create_article.html  # Create form
│   ├── edit_article.html    # Edit form
│   ├── admin.html           # Admin dashboard
│   ├── about.html           # About page
│   ├── contact.html         # Contact page
│   ├── search.html          # Search results
│   └── 404.html             # Error page
│
├── static/
│   ├── css/
│   │   └── style.css        # Main stylesheet
│   ├── js/
│   │   └── main.js          # Main JavaScript
│   └── images/
│       ├── logo.png         # Logo
│       └── favicon.ico      # Favicon
│
├── data/
│   └── articles.json        # Articles database
│
├── utils/
│   ├── __init__.py
│   └── helpers.py           # Helper functions
│
└── screenshots/             # Demo screenshots
    ├── home.png
    ├── article.png
    ├── create.png
    └── admin.png
Usage
Creating Articles
Click "Create Article" in the navigation
Fill in the form:
Title
Excerpt (short summary)
Category (choose from 9 options)
Author Name
Read Time
Image URL (optional)
Content (full article text)
Click "Publish Article"
Managing Articles
Edit: Click "Edit Article" on any article page
Delete: Click "Delete" and confirm
Feature: Set featured: true in articles.json
Using the API
bash

# Get all articles
curl http://localhost:5000/api/articles

# Get specific article
curl http://localhost:5000/api/articles/1

# Get articles by category
curl http://localhost:5000/api/articles?category=apps

# Search articles
curl http://localhost:5000/api/articles?search=python

# Get statistics
curl http://localhost:5000/api/stats
Deployment
Heroku
Create Heroku app
bash

heroku create ahmadblog
Push to Heroku
bash

git push heroku main
Open the app
bash

heroku open
Render
Connect your GitHub repository to Render
Select "Web Service"
Build Command: pip install -r requirements.txt
Start Command: gunicorn run:app
PythonAnywhere
Upload your code to PythonAnywhere
Create a new web app
Set virtual environment and WSGI configuration
Railway
Connect GitHub repository
Railway auto-detects Flask
Deploy with one click
Environment Variables
Create a .env file based on .env.example:

env

SECRET_KEY=your-secret-key-here
FLASK_ENV=development
FLASK_DEBUG=1
API Reference
Endpoints
Method
Endpoint
Description
GET	/api/articles	Get all articles
GET	/api/articles/<id>	Get single article
GET	/api/articles?category=<cat>	Filter by category
GET	/api/articles?search=<query>	Search articles
GET	/api/featured	Get featured article
GET	/api/stats	Get statistics

Response Format
json

{
  "id": 1,
  "title": "Article Title",
  "excerpt": "Short summary",
  "content": "Full content...",
  "category": "apps",
  "image": "https://...",
  "author": "Ahmad Ansari",
  "date": "2024-01-15",
  "read_time": "8 min read",
  "featured": true
}
Technologies Used
Backend: Python, Flask
Frontend: HTML5, CSS3, JavaScript
Styling: Tailwind CSS (CDN), Custom CSS
Fonts: Space Grotesk, Syne (Google Fonts)
Icons: SVG Icons
Database: JSON Files
Deployment: Gunicorn, Heroku/Render
Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
Ahmad Ansari

GitHub: @ahmadansari
Project Link: https://github.com/ahmadansari/AhmadBlog
Acknowledgments
Flask documentation
Tailwind CSS
Unsplash for placeholder images
Google Fonts
<p align="center">
Made with ❤️ by <strong>Ahmad Ansari</strong>
</p>

<p align="center">
⭐ Star this repo if you found it useful! ⭐
</p>
```
