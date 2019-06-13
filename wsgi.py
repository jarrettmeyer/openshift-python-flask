"""
Defines the WSGI (Web Server Gateway Interface) for the application.
"""
import os
from flask import Flask, request
from flask.logging import default_handler
from logging import DEBUG, ERROR, INFO, Logger, getLogger

app = Flask('flask-demo')
application = app


@app.route('/')
@app.route('/index')
def route_index():
    app.logger.debug('This is a debug message from %s.', request.endpoint)
    app.logger.info('This is an info message from %s.', request.endpoint)
    app.logger.error('This is an error message from %s.', request.endpoint)
    app.logger.warning('This is a warning message from %s.', request.endpoint)
    app.logger.critical('This is a critical message from %s.', request.endpoint)
    return ('Hello, World!', 200)


if __name__ == '__main__':
    logging_level = os.environ.get('LOGGING_LEVEL', None)

    # Configure logging.
    if logging_level == 'DEBUG':
        app.logger.setLevel(DEBUG)
    if logging_level == 'INFO':
        app.logger.setLevel(INFO)
    else:
        app.logger.setLevel(ERROR)

    # Start the application.
    app.run(host='0.0.0.0', port=8080, debug=True)
