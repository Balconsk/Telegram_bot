To correct the work of the bot
you need to use the function to create a database.

What you need to do is:

1) Open the python interpreter

2) Import the database class 
> from models.model_sqlite3.py import DataBase

3) Create a database instance and call the create_database function

> db = DataBase()
> db.create_database()