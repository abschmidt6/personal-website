"""
Andrew Schmidt development configuration.

Andrew Schmidt <abschmidt6@gmail.com>
"""

import os

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Database file is var/insta485.sqlite3
DATABASE_FILENAME = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'andrewschmidt.sqlite3'
)