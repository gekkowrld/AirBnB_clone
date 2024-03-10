#!/usr/bin/python3
"""Initialize some modules for use
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
