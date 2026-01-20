Visitor Log Management System (Django)

Project Overview:

This project is a Visitor Log Management System developed using Django and Django REST Framework.
It is designed as a backend REST API to manage visitor check-in and check-out details.

The system helps track visitors currently inside the premises and also allows viewing visitors by date.

Tech Stack:

Python
Django
Django REST Framework
SQLite (default Django database)

Features:

Visitor check-in
Visitor check-out
View current visitors
View visitors by date
Prevent duplicate check-in without check-out
Django Admin panel for managing visitor records

API Endpoints:

1. Check-In Visitor
Method: POST
URL: /api/check-in/

Request Body (JSON):
{
"name": "Ammu",
"phone": "9876543210",
"purpose": "Interview"
}

2. Check-Out Visitor
Method: POST
URL: /api/check-out/

Request Body (JSON):
{
"phone": "9876543210"
}

3. Current Visitors
Method: GET
URL: /api/current/

4. Visitors By Date
Method: GET
URL: /api/by-date/?date=YYYY-MM-DD

Example:
/api/by-date/?date=2026-01-20

How to Run the Project

1. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

2. Install dependencies
pip install django djangorestframework

3. Apply migrations
python manage.py makemigrations
python manage.py migrate

4. Create superuser (optional)
python manage.py createsuperuser

5. Run the development server
python manage.py runserver

Admin panel:
http://127.0.0.1:8000/admin/

Business Rules Implemented:

A visitor cannot check in again without checking out
Phone number is used to identify active visitors
Check-in time is automatically stored
Check-out time is recorded during check-out

Notes:

GET APIs can be tested using a browser
POST APIs should be tested using Postman
SQLite database is used for simplicity

Developed By
Hridhya Das
