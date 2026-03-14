.PHONY: help install run test clean deploy

help:
    @echo "Available commands:"
    @echo "  make install    - Install dependencies"
    @echo "  make run        - Run the application"
    @echo "  make test       - Run tests"
    @echo "  make clean      - Clean cache files"
    @echo "  make deploy     - Deploy to Heroku"

install:
    pip install -r requirements.txt

run:
    python run.py

test:
    pytest tests/ -v --cov=.

clean:
    find . -type d -name "__pycache__" -exec rm -r {} +
    find . -type f -name "*.pyc" -delete
    find . -type d -name "*.egg-info" -exec rm -r {} +

deploy:
    git push heroku main
