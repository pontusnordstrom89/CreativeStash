#### CreativeStash
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


    5. cd to CreativeStash/mysite/

        - Run 
            - MAC       python3 manage.py runserver

            - WINDOWS   py -3 manage.py runserver




    EXTRA
    -To use sqlite3 database 

        - Go to CreativeStash/mysite/mysite/settings.py
            Find DATABASES uncomment and replace with

            DATABASES = {
                'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                }
            }

        - In shell/terminal cd to CreativeStash/mysite

            1. Run
                - MAC       python3 manage.py makemigrations

                - WINDOWS   py -3 manage.py makemigrations


            2. 
                - MAC       python3 manage.py makemigrations theStash

                - WINDOWS   py -3 manage.py makemigrations theStash


            3. 
                - MAC       python3 manage.py migrate

                - WINDOWS   py -3 manage.py migrate

            4. 
                - MAC       python3 manage.py createsuperuser

                - WINDOWS   py -3 manage.py createsuperuser

            Follow instructions

            Now you can create users, create ideas and use the admin pages at http://127.0.0.1:8000/admin/






# Project Code
- Python
- HTML, CSS, JavaScript
- SQL

# Project frameworks
- Django
- Bootstrap


# Dependencies
- Python see requirements.txt
