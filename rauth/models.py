from django.db import models

# Create your models here.


class User(models.Model):
    '''
    This table will hold some users with their credentials.

    The require_valid_password is a flag that will force the password to be checked. If this is 'False', the check will
    ALWAYS return 'True'.

    The pass_if_pw_match setting can be set to 'False' to force the authentication to always fail, regardless of the
    password check result.

    If require_valid_password is True and pass_if_pw_match is True, the password must be set and must match for the
    check to pass

    The database should be dumped with:

        ./manage.py dumpdata > db.json

    You can load the data with:

        ./manage.py loaddata user.json
    '''
    username = models.CharField('Username', max_length=128, primary_key=True)
    require_valid_password = models.BooleanField('Require a Valid Password', default=False)
    password = models.CharField("Password", max_length=128, null=True)
    pass_if_pw_match = models.BooleanField("Pass authentication if Password Match", default=True)
    notes = models.CharField("Notes", max_length=1000000, null=True)



