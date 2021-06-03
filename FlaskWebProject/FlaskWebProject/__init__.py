"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

# This line imports the contents of the FlaskWebProject and looks for something called views
# This is in the file views.py
# This ensures that the code in views.py runs when the app is run.
# Views.py contains the code to render pages
import FlaskWebProject.views
