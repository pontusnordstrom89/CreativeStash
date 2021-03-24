# Django walkthrough


## Index ##

    - Part 1    Installing django and dependencies
    - Part 2    Create DB connection, create superuser and the admin page.
    - Part 3    Create an django app
    - Part 4    Create models to generate datbase tables and store our movie data
    - Part 5    Create views to view our movie collection






# For Windows users
In powershell write pip --version
if you get an error code you'll ned to add a path to python

https://stackoverflow.com/questions/36835341/pip-is-not-recognized

This error shows up on windows when one tries to use pip in the command prompt. To solve this error on windows, you must declare path variable by following these steps:

Step 1 - Right click on My Computer or This PC
Step 2 - Click on Properties
Step 3 - Click on Advanced System Settings

Patch to python folder:  C:\Users\     "UserName"    \AppData\Local\Programs\Python\Python39\Scripts

You will find a section called system variables.
Click on Path from the list of variable and values that shows up there.
After clicking on path click edit. You will find a New button in the pop up.
Click that and paste the location of the python35 or python36 folder (The location you specified while installing python) followed by “\Scripts” there.
For me its “C:\Users\a610580\AppData\Local\Programs\Python\Python35-32”
so I type “C:\Users\a610580\AppData\Local\Programs\Python\Python35-32\Scripts”
Click Ok to close all windows and restart your command prompt.
I repeat - restart your command prompt.



### Part 1 Installing django and dependencies

1. Install Django
    Django 3.0.13 or previous version to make it compatible with django mssql backend
    py -m pip install Django==3.0.13

2. Install django mssql backend. "MSSQL database connector"
    https://pypi.org/project/django-mssql-backend/

    py -m pip install django-mssql-backend

3. Create a directory where the project will live
    
    Create project folder
        mkdir django-project

    cd to the folder you created
        cd django-project

4. Generate the django project files in the project directory

    Run: 
        django-admin startproject mysite

    mysite == name of the project


5. In django-project folder you'll now have

    mysite/
        manage.py
        mysite/
            __init__.py
            settings.py
            urls.py
            asgi.py
            wsgi.py

6. Cd mysite
    You will do everything from this folder from now on!!

    /mysite holds the project files
    /manage.py takes commands from the command line and this is the file that you use to start/manage your django project and use its methods

7. Start django server
    py -3 manage.py runserver

    Visit your site at http://127.0.0.1:8000/ 

    # command line output should be
    Watching for file changes with StatReloader                                                                             
    Performing system checks...                                                                                                                                                                                                                     System check identified no issues (0 silenced).                                                                                                                                                                                                 
    You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.                                                                                          
    Run 'python manage.py migrate' to apply them.                                                                           
    March 16, 2021 - 09:45:03                                                                                               
    Django version 3.0.13, using settings 'mysite.settings'                                                                 
    Starting development server at http://127.0.0.1:8000/                                                                   
    Quit the server with CTRL-BREAK.












##### Part 2 #####

# Create DB conneciton, create superuser and admin page.


# In MSSQL manager create a new database called CreativeStash


Ctrl + c in command line to stop server


1. In settings.py

        mysite/
        manage.py
        mysite/
            __init__.py
            settings.py     <---------
            urls.py
            asgi.py
            wsgi.py




    #  In code editor open settings.py and find DATABASES, change to this

        DATABASES = {
            'default': {
                'ENGINE': 'sql_server.pyodbc',
                'HOST': 'localhost',
                'PORT': '',
                'NAME': 'CreativeStash',
                'USER': '',
                'PASSWORD': '',
                'OPTIONS': {
                    'driver': 'ODBC Driver 17 for SQL Server',
                    'unicode_results': True,
                },
            },
        }

2. Django has some standard tables like user, admin, group etc but we have to migrate them to our DB.

    In command line
    - py -3 manage.py makemigrations
    - py -3 manage.py migrate

    If you look att tables in your db there are some new ones like dbo.auth_user. It holds all users including the superuser we´re going to create now

3. In terminal write 
    -py -3 manage.py createsuperuser
    -follow the instructions

4. Run server
    - py -3 manage.py runserver

5. Launch browser and visit
    - http://127.0.0.1:8000/admin

    On the admin page you can see AUTHENTICATION AND AUTHORIZATION with Groups and Users as sub categories. Here you can administrate users, add or delete. create groups with permisions and place users in them.

















#### Part 3 ####

# Create a django app

# Projects vs. apps
    What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

We will create an movie collection app where you can add, store, display and delete movies


Ctrl + c to stop server

1. To create your app run this in command line
    - py -3 manage.py startapp movies

    movies will be the name of our app

2. That will create the directory movies in top mysite directory

    movies/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py

3. To display content from the app we have to create a view

    - In code editor open views.py

    - paste and save this code

        from django.http import HttpResponse

        def index(request):
            return HttpResponse("Hello, world. You're at the movie index.")



4. In movies create a file named urls.py

    - paste and save this code

        from django.urls import path

        from . import views

        urlpatterns = [
            path('', views.index, name='index'),
        ]

5. In order to view the content we create in our movies app we have to point the root url from our mysite project
    - Go to 
        mysite/urls.py

    - add our url pattern
    
        from django.contrib import admin

        from django.urls import include, path

        urlpatterns = [
            path('movies/', include('movies.urls')),
            path('admin/', admin.site.urls),
        ]
       
6. Register app with project in mysite/settings.py

    - Open mysite/settings.py and add movies

        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',

            'movies.apps.MoviesConfig',    
        ]


7. Run server and visit movies app
    - py -3 manage.py runserver
    - http://127.0.0.1:8000/movies









#### Part 4 ####

# Create models to generate databse tables and store our moive data

Models are python classes that structures the way we want to store data and translates it for us to SQL through a migration like the one we did before.

1. open movies/models.py and paste this code

    from django.db import models

    class Genre(models.Model):
        genre_name = models.CharField(primary_key=True, max_length=100)
        genre_description = models.TextField(max_length=1000)

    class Movie(models.Model):
        movie_id = models.AutoField(primary_key=True)
        movie_titel = models.CharField(max_length=100)
        movie_description = models.TextField(max_length=1000)
        release_date = models.DateField('Release date')
        genre = models.ForeignKey(Genres, on_delete=models.CASCADE)


2. Create sql tables for our models

    - py -3 manage.py makemigrations movies
    - py -3 manage.py migrate movies

    that will create two tables in DB CreativeStash,  Genres and Movies

    in movies/migrations it will also create 00001_initial.py
    it represents the migrations and columns of the created tables

3. When the models are created and migrated to DB we can register them in our admin area where we can manage and store new data to our tables.

    - open movies/admin.py in code editor and paste

        from django.contrib import admin

        from .models import Movies, Genres
        
        admin.site.register(Movies)
        admin.site.register(Genres)

4. Save and start the server

    - py -3 manage.py runserver
    - http://127.0.0.1:8000/admin


    # To make it easier to navigate items we can update our models to display names better in admin view

        from django.db import models

        class Genre(models.Model):
            genre_name = models.CharField(primary_key=True, max_length=100)
            genre_description = models.TextField(max_length=1000)

            def __str__(self):
                self.genre = self.genre_name + ' | ' + self.genre_description
                return self.genre

        class Movie(models.Model):
            movie_id = models.AutoField(primary_key=True)
            movie_titel = models.CharField(max_length=100)
            movie_description = models.TextField(max_length=1000)
            release_date = models.DateTimeField('Release date')
            genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


            def __str__(self):
                self.movie = str(self.movie_id) + ' | ' + self.movie_titel
                return self.movie


5. Add some movies to our database











#### Part 5 ####

Create views to view our movies

1. In movies/views.py update to this

    from django.http import HttpResponse
    from django.template import loader
    from django.shortcuts import get_object_or_404, render

    from .models import Movie, Genre

    def index(request):
        latest_movie_list = Movie.objects.order_by('release_date')[:5]
        template = loader.get_template('movies/index.html')
        context = {
            'latest_movie_list': latest_movie_list,
        }
        return HttpResponse(template.render(context, request))


    def detail(request, movie_id):
        return HttpResponse("You're looking at movie %s." % movie_id)


    def detail(request, movie_id):
        movie_details = get_object_or_404(Movie, pk=movie_id)
        return render(request, 'movies/detail.html', {'movie_details': movie_details})



2. In movies/urls.py add path to detail function

    urlpatterns = [
        # ex: /movies/
        path('', views.index, name='index'),
        # ex: /movies/2/
        path('<int:movie_id>/', views.detail, name='detail'),
    ]

3. In the movies/ create a new folder called <templates> and then a new folder in templates/ called <movies>
    - In movies/templates/movies/ create index.html and put this code in the html document

        {% if latest_movie_list %}
            <ul>
                {% for movie in latest_movie_list %}
                <li><a href="/movies/{{ movie.movie_id }}/">{{ movie.movie_text }}</a></li>
                {% endfor %}
            </ul>
            {% else %}
            <p>No movies are available.</p>
        {% endif %}


4. In movies/templates/movies/ create <detail.html> and add
    
    <h1>{{ movie_details.movie_titel }}</h1>
    <p>{{ movie_details.movie_description }}</p>


5. Some basic styling to movies page

    - In movies/ create a folder called <static>
    - in static/ create a folder called <movies>
    - in static/movies/ create style.css and write some simple styling like

        body {
            background-color: green;
        }

    - In index.html add to top of file

        {% load static %}
        <link rel="stylesheet" type="text/css" href="{% static 'movies/style.css' %}">

    Save and visit your site http://127.0.0.1:8000/movies

    Ctrl + Shift + R on windows to do a hard refresh of the site and show changes made to CSS


 
