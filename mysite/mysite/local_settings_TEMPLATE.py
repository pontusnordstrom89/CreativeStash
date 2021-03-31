
#Rename this file to local_settings.py, uncomment and adjust to your database settings.

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


#MSSQL on Windows
'''
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'mydb',
        'USER': 'user@myserver',
        'PASSWORD': 'password',
        'HOST': 'myserver.database.windows.net',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    },
}
'''

#MSSQL on MacOS
'''
DATABASES = {
    'default': {
        'NAME': 'CreativeStash',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': '127.0.0.1',
        'USER': 'sa',
        'PASSWORD': 'Creativestash2021',
        'PORT': '1433',
        'OPTIONS': {'driver':'ODBC Driver 17 for SQL Server'}
    }
}
'''
