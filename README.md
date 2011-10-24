# Django Skeleton

## The included directories
* _project_ - the source code
* _static_ - the Django STATIC root directory
* _media_ - the Django MEDIA root directory
* _env_ - virtualenv or buildout environment files
* _help_ - files related to the project, tutorials, photoshop files, etc
* _setup_ - files necessary to setup the project inside various environments
* _logs_ - the logs

## Optionally directories
* _database_ - this is the parent location of your sqlite database, if case 

## Setup the project with virtualenv and pip
* $ cd /project_name
* $ git clone git@github.com:florentin/django-skeleton.git .
* $ virtualenv env --no-site-packages
* $ source ./env/bin/activate
* $ mkdir -p database
* $ pip install -r ./setup/requirements/production.txt
* $ pip install -r ./setup/requirements/development.txt

## Setup the database
* $ cd /project_name/
* $ source ./env/bin/activate
* $ cd ./project
* $ python manage.py syncdb --noinput
* $ python manage.py createsuperuser --email=admin@admin.com --username=admin
* $ Password: admin

## Run the development server
* $ cd /project_name/
* $ source ./env/bin/activate
* $ cd ./project
* $ python manage.py runserver --nostatic
