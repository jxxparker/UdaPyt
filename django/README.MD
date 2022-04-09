Django Documentations Used on these projects

08) Models and Admin Panel

- python3 manage.py createsuperuser : 
    this allows you to create super user so you can log in from localhost:8000/admin

10) Database Queries

-queryset = ModelName.objects.all()

# ModelName = ModelName
# objects. = model objects attrivute
# .all() = method 
    - other examples include .get(), .filter(), .exclude()

11) Model Forms
 -- {{form.as_p}} : prints everything in form neated way.
 -- form.is_valid(): The form's data will be validated the first time either you call is_valid() or access errors
 -- form.save() : save method is called on the Django ModelForm instance in order to save the data to the database (SQLite3)


