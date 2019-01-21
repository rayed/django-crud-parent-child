
# Django CRUD Parent/Child Example

This project consist of five stand alone applications that shows different
ways to implement CRUD operations in single table, and parent/child tables.

## Sample Applications 

The applications are:

- books_simple: Single table CRUD operations.
- books\_pc\_formset: Parent/Child CRUD operation using Django formsets, which means editing the children in the sample form as the parent.
- books\_pc\_formset2: similar to previous app but uses a foreign key in the children.
- books\_pc\_multiview: Parent/Child CRUD operation using multiple one view for the parent and another seperate view for the children.
- books\_pc\_multiview2: similar to previous app but uses a foreign key in the children.

# Running the Applications

Install the needed Python package (only Django 1.9):

    pip install -r requirements.txt

Create the database:

    ./manage.py makemigrations
    ./manage.py migrate

Then run the server:

    ./manage.py runserver

