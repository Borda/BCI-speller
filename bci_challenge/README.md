bci_challenge
=============

A short description of the project.

![Built with Cookiecutter Django https://github.com/pydanny/cookiecutter-django/](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)



Settings
--------

Moved to [settings](https://github.com/10clouds/project-template/master/docs/settings.md).


Basic Commands
--------------

#### Setting Up Your Users

* To create a **normal user account**, just go to Sign Up and fill out the form. 
Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your 
console to see a simulated email verification message. Copy the link into your 
browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command:

```
    $ docker-compose run --rm app ./manage.py createsuperuser
```

For convenience, you can keep your normal user logged in on Chrome and your 
superuser logged in on Firefox (or similar), so that you can see how the site 
behaves for both kinds of users.


#### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report::

```
    $ docker-compose run --rm app pytest --cov-report html --cov . --verbose
    $ open backend/htmlcov/index.html
```

#### Running tests with py.test

```
  $ docker-compose run --rm app pytest .
```

#### Celery

This app comes with Celery. By default all tasks is run not async.
If you need work local with async you must change `CELERY_ALWAYS_EAGER` on `False`
in `backend/settings/local.py` then all tasks will use `redis`
and docker configurations.
 
```
CELERY_ALWAYS_EAGER = False
```


#### Sentry

Sentry is an error logging aggregator service. You can send email to DevOps 
team and asking about you account and project bci_challenge.

You must set the DSN url in production.


Deployment
----------

The following details how to deploy this application.


#### Docker

See detailed [project-template Docker documentation](https://github.com/10clouds/project-template/blob/master/docs/developing-locally-docker.md).
