========================================================================
             LITTLE LEMON RESTAURANT WEB APPLICATION
         Meta Back-End Developer Professional Certificate
                      Capstone Project
========================================================================

PROJECT OVERVIEW
----------------
This is the complete back-end web application for the Little Lemon restaurant,
developed using Django and Django REST Framework (DRF) as required for the 
Meta Back-End Developer Capstone project.

The application includes:
1. Static homepage with restaurant branding and styling.
2. Menu API with generic ListCreateAPIView and RetrieveUpdateDestroyAPIView.
3. Booking API with ModelViewSet and Token Authentication permissions.
4. User management and registration using Djoser.
5. DRF Token Generation endpoint.
6. Comprehensive unit tests for Models and Views.
7. Local MySQL database connection.


PROJECT PREREQUISITES & INSTALLATION
------------------------------------
1. Create and activate a virtual environment:
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. MySQL Database Setup:
   Ensure your MySQL server is running on 127.0.0.1:3306 with:
   - Database name: littlelemon
   - Username: root
   - Password: (blank / empty by default)

   To create the database in MySQL:
   CREATE DATABASE littlelemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

4. Run Database Migrations:
   python manage.py makemigrations
   python manage.py migrate

5. Create a Superuser (Admin):
   python manage.py createsuperuser

6. Run Unit Tests:
   python manage.py test

7. Start the Development Server:
   python manage.py runserver


========================================================================
                 API ENDPOINTS REFERENCE FOR INSOMNIA
========================================================================

1. STATIC HTML HOMEPAGE
-----------------------
- GET  http://127.0.0.1:8000/restaurant/
  Renders the Little Lemon static landing page with logo, styling, and navigation.


2. MENU API ENDPOINTS
---------------------
- GET  http://127.0.0.1:8000/restaurant/menu/
  Lists all menu items.
  Response: 200 OK with list of menu objects.

- POST http://127.0.0.1:8000/restaurant/menu/
  Creates a new menu item.
  Header: Content-Type: application/json
  Body:
  {
      "title": "Greek Salad",
      "price": "12.50",
      "inventory": 25
  }

- GET  http://127.0.0.1:8000/restaurant/menu/1
  Retrieves single menu item with ID 1.

- PUT  http://127.0.0.1:8000/restaurant/menu/1
  Updates menu item with ID 1.
  Header: Content-Type: application/json
  Body:
  {
      "title": "Greek Salad Special",
      "price": "14.00",
      "inventory": 30
  }

- DELETE http://127.0.0.1:8000/restaurant/menu/1
  Deletes menu item with ID 1.


3. TABLE BOOKINGS API (Protected by IsAuthenticated)
---------------------------------------------------
All requests below require the following header:
Authorization: Token <your_auth_token_here>

- GET  http://127.0.0.1:8000/restaurant/booking/tables/
  Lists all table reservations.

- POST http://127.0.0.1:8000/restaurant/booking/tables/
  Creates a new table booking reservation.
  Header: 
    Content-Type: application/json
    Authorization: Token <your_auth_token_here>
  Body:
  {
      "name": "John Doe",
      "no_of_guests": 4,
      "booking_date": "2026-11-01T19:00:00Z"
  }

- GET  http://127.0.0.1:8000/restaurant/booking/tables/1/
  Retrieves booking detail for ID 1.

- PUT  http://127.0.0.1:8000/restaurant/booking/tables/1/
  Updates booking detail for ID 1.
  Body:
  {
      "name": "John Doe",
      "no_of_guests": 5,
      "booking_date": "2026-11-01T19:30:00Z"
  }

- DELETE http://127.0.0.1:8000/restaurant/booking/tables/1/
  Deletes table booking with ID 1.


4. USER REGISTRATION & AUTHENTICATION (DJOSER)
---------------------------------------------
- POST http://127.0.0.1:8000/auth/users/
  Registers a new user account.
  Header: Content-Type: application/json
  Body:
  {
      "username": "reviewer",
      "password": "Password123#",
      "email": "reviewer@example.com"
  }

- POST http://127.0.0.1:8000/auth/token/login/
  Logs in a user and generates an authentication token.
  Header: Content-Type: application/json
  Body:
  {
      "username": "reviewer",
      "password": "Password123#"
  }
  Response:
  {
      "auth_token": "a1b2c3d4e5f6..."
  }

- GET  http://127.0.0.1:8000/auth/users/me/
  Returns information about the currently logged-in user.
  Header: Authorization: Token <your_auth_token_here>

- POST http://127.0.0.1:8000/auth/token/logout/
  Logs out the user and invalidates the token.
  Header: Authorization: Token <your_auth_token_here>


5. DRF TOKEN GENERATION ENDPOINT
--------------------------------
- POST http://127.0.0.1:8000/api-token-auth/
  (Also accessible at: http://127.0.0.1:8000/restaurant/api-token-auth/)
  Generates an auth token using DRF's obtain_auth_token.
  Header: Content-Type: application/json
  Body:
  {
      "username": "reviewer",
      "password": "Password123#"
  }
  Response:
  {
      "token": "a1b2c3d4e5f6..."
  }

========================================================================
