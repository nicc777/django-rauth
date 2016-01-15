=====
rauth
=====

rauth is a simple authentication platform that can be used to simulate external 
authentication from any app.

A sample test is included in the file rauth_test.sh (depends on curl).

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'rauth',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^rauth/', include('rauth.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Run `python manage.py loaddata user.json` to load the sample data

5. Start the development server and visit http://127.0.0.1:8000/rauth/  

5. Visit http://127.0.0.1:8000/rauth/ to test, or run the rauth_test.sh script