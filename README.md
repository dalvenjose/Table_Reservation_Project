Table Reservation and Food Ordering Website

This project is a comprehensive web-based application designed to simplify restaurant table reservations and food menu ordering. The application provides an intuitive interface for customers and powerful management tools for restaurant owners.


Features

Table Reservation

User Registration and Login:

Users can create accounts and log in securely.

Table Booking:

Customers can view available tables and make reservations for specific dates and times.

Reservation History:

Users can track their past and upcoming reservations.
Food Menu and Ordering

Browse Menu:

Users can view the restaurant's menu with detailed descriptions, prices, and images.

Order Food:

Customers can select items, add them to their cart, and place orders.

Order History:

Users can review their previous food orders.

Admin Dashboard

Manage Reservations:

Restaurant owners can approve, cancel, or update table reservations.

Manage Menu Items:

Add, edit, or delete menu items with ease.

Order Management:

View and process incoming food orders.

Additional Features

Responsive Design:

Ensures seamless functionality on desktops, tablets, and mobile devices.


Technologies Used

Frontend: HTML, CSS, JavaScript

Backend: Python, Django

Database: SQLite

Version Control: Git and GitHub



Installation

Clone the repository:


git clone https://github.com/dalvenjose/Table_Reservation_Project.git  

cd Table_Reservation_Website  

Set up a virtual environment:
python -m venv venv  

source venv/bin/activate  # On Windows, use `venv\Scripts\activate`  

Install dependencies:


pip install -r requirements.txt

Run database migrations:


python manage.py migrate  

Start the development server:


python manage.py runserver  
Access the website:

Open your browser and navigate to http://127.0.0.1:8000/.



Usage
For Customers:

Register or log in to your account.

Book a table for your desired date and time.

Browse the food menu, add items to your cart, and place an order.

View your reservation and order history.


For Admins:

Manage table reservations and food menu items through the admin dashboard.

Process and track customer food orders.


Acknowledgments

Django Documentation

SQLite

Contributors and open-source libraries
