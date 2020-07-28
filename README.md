# Snackcart 3.0 
#####  This time it's not Snackcart 2.0

Started 6/18/2020 

This is a the continuation of a program started 6 months ago done entirely in vanilla javascript.  This new version is done using Python for the backend, through the use of Django and SQLite.  

Built in Python 3.8 using Django.
Inventory will be editable.

Read the scoping and requirements in the SNACKCART 1.0 README: https://github.com/GabbardDesigns/snckcrt/blob/master/scoping.md

his version of Snackcart has the following enhancements:

###### Backend Changes
- Added an administrative backend to allow management of users (essentially allow more backend users) and management of inventory.

- Added the ability to modify the default list of items in the inventory:  
   - Add Items Manually
   - Edit Items
   - Upload Items via CSV

All changes are reflected instantly in the inventory through a combination of rewriting the JSON file read on the front-end and scheudled checks for changes in file vs database.

######Front-end Changes
- Navigation changes dynamically based on whether user is logged in
- Added ability to view details about the items in inventory through the use of a view inventory button on the homepage (in the footer).

#####Technical Summary
  - Python 3.8
  - Django 3.0.8

#####How to Make the Project Work
1. Setup a virtual environment (python -m venv /path/to/new/virtual/environment)
2. Activate the environment in command prompt or terminal ($ source <venv>/bin/activate or C:\> <venv>\Scripts\activate.bat)
3. Clone the GitHub project in your local directory with command git clone https://github.com/GabbardDesigns/snckcrt.git
4. Run the command in console "pip install -r requirements.txt".  This command will install the necessary packages required to run the project.
5. Go the the directory where Django project is present and manage.py file is present.
6. Create a superuser: python manage.py createsuperuser
6. In the terminal run: python manage.py make migrations
7. In the terminal run: python manage.py migrate
8. In the terminal run: python manage.py runserver
9. Access the front-end web interface at http://127.0.0.1:8000/ 
10. Access the admin interface at http://127.0.0.1:8000/admin

Stock User Information

superuser
  | username: super  | password: superuserpassword

school admin user (staff)
  | username: school_admin  | password: QhZ6fb25TwkVyJV

Test Files (download and reupload)
- Sample good single record test file: test_files\single_upload.csv 
- Sample good multi-record test file: test_files\multi_upload.csv
- Sample bad record test file: test_files\bad_upload.csv
- Sample bad file format test file: test_files\bad_upload.txt


Testing Methodology
Add 


The Pythonic portions of this project are: 
  - The entire backend
  - The new view inventory button and subsequent pages on the front-end.
  - Technically the front-end is fed from a Python function, but the actual functionality of the front-end is all JavaScript.  

Future Improvements
  - Move to or integrate React to allow for deployment on Android ecosystem. 

