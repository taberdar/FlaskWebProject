"""
This script runs the FlaskWebProject application using a development server.
"""

from os import environ

# This line imports app from the FlaskWebProject folder
# app is defined in the file __init__.py 

from FlaskWebProject import app

if __name__ == '__main__':  # This will be true if this file is being run directly
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)  # This line runs the app code.
