# django-rauth

Simple remote authentication service created as a Django app. 

## Setup

* Add "polls" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = [
        ...
        'rauth',
    ]

* Include the polls URLconf in your project urls.py like this:

    url(r'^rauth/', include('rauth.urls')),

* Run `python manage.py migrate` to create the polls models.

* Run `python manage.py loaddata db.json` to load the sample data

* Start the development server and visit http://127.0.0.1:8000/rauth/  

* Visit http://127.0.0.1:8000/rauth/ to test, or run the rauth_test.sh script  

## Example

After the application has started, you can POST data to the app with two mandatory fields: `username` and `password`.

Based on how the user is configured in the database, a JSON object will be returned with the authentication result and reason.

I have used this approach to test and play with Django - especially customizing the authentication to use external sources. 

## Final Note

This is for educational use mainly. DO NOT use this as an authentication mechanism - it has not been designed with true security in mind at all!

Future enhancements will be mainly for my own purposes. 

