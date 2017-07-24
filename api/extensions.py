"""Flask and other extensions instantiated here.

To avoid circular imports, extensions are instantiated here. They will be initialized
(calling init_app()) in application.py.
"""

from logging import getLogger
from flask_marshmallow import Marshmallow

LOG = getLogger(__name__)

# Marshmallow for serialization/deserialization
ma = Marshmallow()
