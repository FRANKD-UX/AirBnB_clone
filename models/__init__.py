# models/__init__.py

# Ensure imports are at the top of the file

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

# Dictionary to hold all model classes
all_classes = {
            'BaseModel': BaseModel,
            }

# Create an instance of FileStorage and reload
storage = FileStorage()
storage.reload()
