# Snackcart 3.0 
####  This time it's not Snackcart 2.0

**Project Start Date:** Started 6/18/2020 

This is a the continuation of a program started 6 months ago done entirely in vanilla javascript.  This new version is done using Python for the backend, through the use of Django and SQLite.  

#### Technical Summary
  - Python 3.8
  - Django 3.0.8

The Pythonic portions of this project are: 
  - The entire backend
  - The new view inventory button and subsequent pages on the front-end.
  - Technically the front-end is fed from a Python function, but the actual functionality of the front-end is all JavaScript.  

CL REQUIREMENTS
-------------
##### Number of Commits: 10 Commits

##### Create a class, then create at least one object of that class and populate it with data

        products\models.py | class Products
        
  - This is the main product class and drives all other functionality in the products module.  It is called whenever a reference is made to the Product table.
  - This can be seen in action on the front-end using the View Inventory Details button.  This calls the view defined in products/views.py | product_detail_view
  - This can also be seen in use in the hidden non-admin Add Products (/products/templates/product/newproduct.html) and Edit form (/products/templates/product/newproduct.html)  
  - This is also used in numerous other places including /products/views.py | product_upload when the inventory is updated and when the database is read out as a QuerySet for processing prior to loading over to JSON.  
  Also see: products/models.py | thumbnail_preview       
 
 -------------
 
##### Create and call at least 3 functions, at least one of which must return a value that is used

    products/admin.py : ProductAdmin => save_model
    

This function extends the normal save function for all admin-side product views (add/edit/upload).  
 - The normal save function allows the addition/changes to be written to the database.  
 - The extension then creates a queryset from the database (selecting only the Active records and sorting them alphabetically by title)
 - It then opens the JSON file that the frontend uses to populate its inventory, rewrites the inventory file, and then closes that file.


    products/models.py | thumbnail_preview 
 
  - This function is called on self and assigns a thumbnail preview that is used in the amdin edit product view.  
  - It defines a “safe” snippet of html code that is returned by the function, effectively allowing for relational images of any product page.


    products/views.py | product_detail_view(request, id) 
    
    
  - This function provides both a Queryset and a record ID to the html rendered on the front-end product details page.  
  - The information passed back allow the page to dynamically re-render a portion of itself through an AJAX call when a user clicks one of the inventory buttons.     
  
-------------

##### Read data from an external file, such as text, JSON, CSV, etc and use that data in your application

    products/views.py : product_upload 

 -  This function is called on the page /product_upload/ and is used in the on-page form to allow the user to upload a .csv file of their products.  
 -  There is error handling for non-csv files, no file, and if the file is improperly formatted.  
 -  All errors and a success message are reported to the user dynamically in the Message Center portion of the page.

-------------
##### Write data to an external file, and use that file in your application (cross language communication JavaScript/Python via AJAX)

    products/admin.py : class ProductAdmin – save_model function

  - This super version of the save_model function is called when the product model is changed via a save operation.
  - After it has added the new record to the database, it reads/writes the objects from the Product table in the database to a JSON file to be handled by the JavaScript frontend.  
  - The function does some scrubbing/filtering/sorting prior to loading over to JSON.  It check to ensure the object is set as active and sorts the inventory alphabetically prior to writing.

-------------
-------------
#### What is new for version 3.0?

##### Scope and Requirements
Read the scoping and requirements in the SNACKCART 1.0 README: https://github.com/GabbardDesigns/snckcrt/blob/master/scoping.md

This version of Snackcart has the following enhancements:

##### Backend Changes
- Added an administrative backend to allow management of users (essentially allow more backend users) and management of inventory.

- Added the ability to modify the default list of items in the inventory:  
   - Add Items Manually
   - Edit Items
   - Upload Items via CSV

All changes are reflected instantly in the inventory through a combination of rewriting the JSON file read on the front-end and scheudled checks for changes in file vs database.

##### Front-end Changes
- Navigation changes dynamically based on whether user is logged in
- Added ability to view details about the items in inventory through the use of a view inventory button on the homepage (in the footer).

##### How to Make the Project Work
1. Setup a virtual environment (python -m venv /path/to/new/virtual/environment)
2. Activate the environment in command prompt or terminal ($ source <venv>/bin/activate or C:\> <venv>\Scripts\activate.bat)
3. Clone the GitHub project in your local directory with command git clone https://github.com/GabbardDesigns/snckcrt.git
4. Run the command in console "pip install -r requirements.txt".  This command will install the necessary packages required to run the project.
5. Go the the directory where Django project is present and manage.py file is present.
6. Open terminal and create a superuser, follow on-screen prompts  

        > python manage.py createsuperuser

7. In terminal (or command prompt) prepare the databases

        > python manage.py make migrations
        > python manage.py migrate

8. In terminal start the server

        > python manage.py runserver
        
9. Access the front-end web interface at http://127.0.0.1:8000/ 
10. Access the admin interface at http://127.0.0.1:8000/admin or by clciking the login link in the upper right corner.


##### Stock User Information

    superuser | username: super | password: superuserpassword

    school admin (staff) | username: school_admin  | password: QhZ6fb25TwkVyJV


##### Test Files (download and re-upload)
  - Sample good single record test file: snckrt\test_files\single_upload.csv 
  - Sample good multi-record test file: snckrt\test_files\multi_upload.csv
  - Sample bad record test file: snckrt\test_files\bad_upload.csv
  - Sample bad file format test file: snckrt\test_files\bad_upload.txt


#### Future Improvements
  - Move to or integrate React to allow for deployment on Android ecosystem. 