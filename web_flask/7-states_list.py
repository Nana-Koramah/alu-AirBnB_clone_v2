#!/usr/bin/python3
"""
This module starts a Flask web application that serves a page listing states.
The states are listed in alphabetical order on the '/states_list' route.

The application interacts with a storage system to retrieve and display the states.
It also ensures the storage is properly closed after each request to maintain resource efficiency.
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
    
    This function retrieves all State objects from the storage, sorts them by name in
    alphabetical order, and passes the sorted list to an HTML template for rendering.
    
    Returns:
        str: Rendered HTML template displaying the list of states.
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """
    Teardown handler that closes the storage.
    
    This function is called automatically after each request to ensure that the
    database connection is properly closed, which helps in resource management.
    
    Args:
        exception (Exception): The exception that occurred during request handling, if any.
    """
    storage.close()

if __name__ == '__main__':
    # Run the Flask application on the specified host and port
    app.run(host='0.0.0.0', port='5000')
