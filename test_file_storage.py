#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

# Create an instance of FileStorage
storage = FileStorage()

# Check if the objects are empty initially
all_objs = storage.all()
print("-- Initial objects --")
print(all_objs)  # Should be empty {}

# Create a new BaseModel instance
print("-- Creating a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()

# Check if the object has been saved
all_objs = storage.all()
print("-- Objects after saving a new one --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

# Check if the object is stored in the JSON file
print("-- Checking the contents of the file.json --")
with open('file.json', 'r') as file:
    print(file.read())

# Reload the objects from the file and verify
print("-- Reloading objects from file --")
storage.reload()
all_objs = storage.all()
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)
