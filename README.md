<h1>
    Test Compass
</h1>

<div>
<h2>
Django Setup
</h2>

1. **Install Python and Django** https://docs.djangoproject.com/en/5.0/topics/install/

2. **Create a Virtualenvironment**  
   `python -m venv env`

The virtualenvironment allows you to install as many
libraries and packages as you want in an isolated area, so it won't affect your computer

3. **Activate Virtualenv**  
   `source env/bin/activate`

4. Go to project-folder (/backend)
5. Install requirements  
   `pip install -r requirements.txt`

6. Migrate the database  
`python manage.py migrate`

7. Start the server  
`python manage.py runserver`

The server will now run on http://localhost:8000
</div>

<div>
<h2>
Create new migrations
</h2>
After changes on any "models.py" file, you have to re-make the migrations. Follow these steps.

1. **Create a migration file**  
   `python manage.py makemigrations <app_name> --name <your-name>`

The app name is the name of the app you changed the models on. So either `organizations` or `user_tests`. Your Name is the name of the migration. It should contain a short description on what changed.

2. **Migrate your database**    
`python manage.py migrate`

Usually this is enough. If you have any bigger migration locally, try deleting your sqlite database. 
</div>