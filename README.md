# Snackcart 3.0 
#####  This time it's not Snackcart 2.0

Started 6/18/2020 

A new version of Snackcart. 

Built in Python 3.8 using Django.
Inventory will be editable.

FROM SNACKCART 1.0 README

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
