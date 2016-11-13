"""
db operations
"""

#https://pymodm.readthedocs.io/en/latest/getting-started.html

from pymodm import MongoModel, connect, fields

# Connect to MongoDB and call the connection "my-app".
connect("mongodb://localhost:27017/myDatabase", alias="my-app")

class User(MongoModel):
    email = fields.EmailField(primary_key=True)
    first_name = fields.CharField()
    last_name = fields.CharField()