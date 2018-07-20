from .base import *

TESTING = True  # controls whether our static site, custom devtools, and admin site are available

# automatically redirect to HTTPS, and other SSL stuff
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
