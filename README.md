
# Django CRUD Parent/Child Example

This project consist of five stand alone applications that shows different
ways to implement CRUD operations in single table, and parent/child tables
using Django web framework.

This version uses Django 2.2 LTS version.

## Sample Applications 

The applications are:

- books_simple: Single table CRUD operations.
- books\_pc\_formset: Parent/Child CRUD operation using Django formsets, which means editing the children in the sample form as the parent.
- books\_pc\_formset2: similar to previous app but uses a foreign key in the children.
- books\_pc\_multiview: Parent/Child CRUD operation using multiple one view for the parent and another seperate view for the children.
- books\_pc\_multiview2: similar to previous app but uses a foreign key in the children.

## Installation and Running

Summary:

    git clone git@github.com:rayed/django-crud-parent-child.git
    cd django-crud-parent-child
    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
    cd apps
    ./manage.py migrate
    ./manage.py runserver

    ./manage.py createsuperuser
    
Description of the installation steps:

    # Clone the project
    git clone git@github.com:rayed/django-crud-parent-child.git

    cd django-crud-parent-child
    
    # Create Python 3 virtual environment 
    python3 -m venv venv
    # Activate the virtual environment
    . venv/bin/activate

    # Install required packages (Django 2.2 LTS)
    pip install -r requirements.txt

    cd apps
    # Create database tables for the project, project configured to use SQLite DB
    ./manage.py migrate

    # Run the development server
    ./manage.py runserver

