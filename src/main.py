"""Main entry point for the Flask application."""

import os

from flask import Flask, render_template
from flask_assets import Environment
from flask_compress import Compress
from flask_frozen import Freezer

# Set the secret key for the Flask application
app = Flask(
    os.getenv("APP_NAME", "Dataglitch Website"),
    template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates"),
    static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), "static"),
)
app.config["FREEZER_DESTINATION"] = os.getenv(
    "FREEZER_DESTINATION", os.path.join(os.path.dirname(os.path.dirname(__file__)), "static_files")
)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["COMPRESS_ALGORITHM"] = "gzip"
app.config["FREEZER_RELATIVE_URLS"] = True

# Setup assets environment
assets = Environment(app)
# assets.url = app.static_url_path
# assets.cache = webassets_dir
# assets.debug = True  # This helps with debugging asset issues

# Initialize Flask-Compress
Compress(app)

# Register the Freezer with the Flask application
freezer = Freezer(app)


# Pages routes
@app.route("/")
def index() -> str:
    """Home page route."""
    return render_template("index.html")


def run_server() -> None:
    """Entry point for uv run server command."""
    port = 3000
    host = "localhost"
    app.run(debug=False, port=port, host=host)


if __name__ == "__main__":
    run_server()
