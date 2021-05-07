# CreativeStash
- A project by Group 14 in course DA336A-TS043.
- Spring 2021. 
- Bachelor of Science in Computer and Information Science, Malmö University.

## Getting started

    1. Clone files https://github.com/pontusnordstrom89/CreativeStash.git
        
        In powershell, terminal or similar
            - cd to CreativeStash/

    2. To create a virtual environment. In CreativeStash/ folder run 
        
        - MAC           python3 -m venv venv

        - Windows       py -3 -m venv venv

    

    3. Activate virtual environment

        - MAC           venv/bin/activate

        - WINDOWS       venv\Scripts\activate


    4. To install CreativeStash's required python modules run
        pip install -r requirements.txt


    5. In mysite/mysite/
        - create an empty file called local_settings.py

    6. cd to CreativeStash/mysite/

       Run 
            - MAC       python3 manage.py runserver

            - WINDOWS   py -3 manage.py runserver




    EXTRA  !!!!! DATABASE IS NOT COMPATIBLE WITH LATEST VERSION !!!!!
    * To use sqlite3 database 

        * Go to CreativeStash/mysite/mysite/settings.py
            Find and comment out 
            - from .local_settings import *

            - Find DATABASES and uncomment, remove ''' before and after

            DATABASES = {
                'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                }
            }


        In console with path /CreativeStash/mysite/ 
        Run 
            - MAC       python3 manage.py runserver

            - WINDOWS   py -3 manage.py runserver

        Log in as admin
            username = admin
            password = admin

        There are some other users in the db all have the same password
            password = strongpass

        Now you can create users, create ideas and use the admin pages at http://127.0.0.1:8000/admin/

        Django documentation https://docs.djangoproject.com/en/3.2/


        To browse database download https://sqlitebrowser.org/






## Project Code
- Python
- HTML, CSS, JavaScript
- SQL

## Project frameworks
- Django
- Bootstrap

## Dependencies
- Python see requirements.txt
