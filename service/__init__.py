"""
Service Package
"""
from flask import Flask

app = Flask(__name__)

# These imports must be after the Flask app
from service import routes  
# pylint: disable=wrong-import-position,cyclic-import
from service.common import log_handlers  
# pylint: disable=wrong-import-position

# Initialize logging
log_handlers.init_logging(app, "gunicorn.error")

# Logging service start message
app.logger.info(70 * "*")
app.logger.info("  S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")
