# __init__.py (inside app/ folder)
from flask import Flask

app = Flask(__name__)

from app import app  # Importing your app to avoid circular imports
