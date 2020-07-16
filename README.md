# Snackcart 3.0 
#####  This time it's not Snackcart 2.0

Started 6/18/2020 

A new version of Snackcart. 

Built in Python 3.8 using Django.
Inventory will be editable.

FROM SNACKCART 1.0 README

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

Purpose
     - Point of Sales (POS) system for a student run snack cart   

Users 
     - Children with developmental disabilities (limited reading and math skills)

Functional Requirements
     - Students must be able to click (touch) items to add them to the shopping order.  
     - A total must be presented to students and be used to help them understand how much is needed to be paid.  
     - There must be a way to reset the register once the transaction is completed. 

Nice to Have
     - Pay options/Pay Aid - Graphical interface to track payment received and show students how much they still need to receive.
     - Overpayment/Refund - The system should help students determine if change is needed and how much.  

Design Considerations
     - The intended use case for this solution is on a tablet or laptop in widescreen layout.  For this reason, portrait and phone configurations are a secondary consideration.

Distribution
     - The initial version will be a web-based application with a set inventory.  

Future Improvements

The full version of this application will be deployed on Android and iOS mobile devices using react-native and react-fs.  This version will feature an admin interface that will allow users with the admin code (a set code initially, changeable within the admin interface) to:
     - Add new inventory items
     - Change the name, price, etc of items
     - Manage the availability of inventory (by marking active or inactive)
