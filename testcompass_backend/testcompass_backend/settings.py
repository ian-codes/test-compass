try:
    from .settings_prod import *

except ImportError:
    from .settings_dev import *