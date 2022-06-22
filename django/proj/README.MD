Django Documentations Used on these projects

08) Models and Admin Panel

- python3 manage.py createsuperuser : 
    this allows you to create super user so you can log in from localhost:8000/admin

- python3 manage.py migrate :
    migrate executes those sql commands in the database file

What is Django Model?
    -Django model is a built in feature that django uses to create tables, their fields, and various constraints. Django Models is the sql of database one uses with django.

How to add models to your project application?
    - Go to admin.py and put following code
        from . models import "name of your models"
        admin.site.register("name of your model")

---------------------------------------------------------------------------------------------------

09) Database Relationships

- One to One : One table record can relate to one record in another table.
- One to many : One table record can relate to many records in another table.
- Many to many: This relationship occurs when multiple records in a table are associated with multiple records in another table. 

What is Django ForeignKey?
-ForeignKey is a django orm field to clumn mapping for creating and working with relationships between tables in relational database.

on_delete=models.CASCADE = This allows someone to delete aka CASCADE.

---------------------------------------------------------------------------------------------------

10) Database Queries
queryset = ModelName.objects.all() 
# queryset = variables that holds response
# ModelName = Model Name
# objects = Model objects attribute
# .all() = Method : other examples [.get(), .filter(), .exclude()]
