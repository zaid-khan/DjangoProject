This a very basic web application for a local library. I hope to make the database available after I'm done with the project, so watch the space.

Note the database information in the settings file:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdatabase',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
