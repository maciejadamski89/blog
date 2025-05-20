"""Freeze the Flask application into static files."""

from flask_frozen import Freezer

from src.main import app

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
