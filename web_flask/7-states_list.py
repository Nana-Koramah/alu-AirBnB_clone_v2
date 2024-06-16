#!/usr/bin/python3
"""
This module starts a Flask web application that serves a page listing states.
"""

from flask import Flask, render_template
from models import *
from models import storage

# Create an instance of the Flask class
app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Route handler for /states_list.
    Displays an HTML page with the states listed in alphabetical order.
    Fetches all State objects from storage, sorts them by name, and passes them to the template.
    
    Returns:
        str: Rendered HTML template with the list of states.
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """
    Teardown handler that closes the storage.
    This function is called after each request to ensure the database connection is closed.
    
    Args:
        exception (Exception): The exception that occurred (if any).
    """
    storage.close()

if __name__ == '__main__':
    # Run the Flask application on the specified host and port
    app.run(host='0.0.0.0', port='5000')

