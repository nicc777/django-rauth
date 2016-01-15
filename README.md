# django-rauth

Simple remote authentication service created as a Django app. 

## Setup

1. Add "polls" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = [
        ...
        'rauth',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^rauth/', include('rauth.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Run `python manage.py loaddata db.json` to load the sample data

5. Start the development server and visit http://127.0.0.1:8000/rauth/  

6. Visit http://127.0.0.1:8000/rauth/ to test, or run the rauth_test.sh script  

