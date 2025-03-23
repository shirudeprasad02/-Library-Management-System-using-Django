


📚 Library Management System

A Django-based RESTful API for managing books, with authentication for admin users and public access for students.

🚀 Features
Admin Signup & Login (JWT Authentication)

Admin Actions: Create, Read, Update, Delete books

Student View: View all available books

MySQL Database (Configured using XAMPP Server)

Django REST Framework (DRF) for API handling

Token-Based Authentication (JWT)

⚙️ Tech Stack
Backend: Django, Django REST Framework (DRF)

Database: MySQL (Using XAMPP Server)

Authentication: JWT (JSON Web Token)

📂 Project Setup & Installation
1️⃣ Clone the Repository

git clone https://github.com/your-username/library-management.git

cd library-management

2️⃣ Create & Activate a Virtual Environment

python -m venv venv

venv\Scripts\activate  # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

🔗 MySQL Connectivity Using XAMPP

4️⃣ Set Up MySQL Database in XAMPP

Start XAMPP and ensure:

Apache and MySQL services are running.

Open phpMyAdmin (http://localhost/phpmyadmin).

Create a New Database:

Click on "New" (left sidebar).

Enter library_db as the database name.

Select Collation: utf8_general_ci.

Click Create.

5️⃣ Configure Django to Use MySQL (XAMPP)

Open library/settings.py and update database settings:

DATABASES = {

    'default': {
    
        'ENGINE': 'django.db.backends.mysql',
        
        'NAME': 'library_db1',
        
        'USER': 'root',  # Default XAMPP MySQL user
        
        'PASSWORD': '',  # Default XAMPP MySQL password (empty)
        
        'HOST': 'localhost',
        
        'PORT': '3306',
        
    }

    

✅ Now, Django is connected to MySQL via XAMPP! 🎉

6️⃣ Run Migrations

python manage.py makemigrations books

python manage.py migrate

7️⃣ Create a Superuser

python manage.py createsuperuser

Follow the prompts to set up an admin login.

8️⃣ Start the Server

python manage.py runserver

Your API will be available at http://127.0.0.1:8000/

📌 API Endpoints

🧑‍💻 Admin Authentication

Method	Endpoint	Description

POST	/api/admin/signup/	Register a new admin

POST	/api/admin/login/	Login admin (returns JWT token)

📚 Book Management (Admin Only)

Method	Endpoint	Description

POST	/api/books/	Add a new book

GET	/api/books/	Get all books

PUT	/api/books/{id}/	Update book details

DELETE	/api/books/{id}/	Delete a book

👨‍🎓 Student View

Method	Endpoint	Description

GET	/api/student/books/	View all books (Read-only)

🔑 Authentication

Admin users need to include a JWT token in the Authorization header:


Authorization: Bearer <your_access_token>

To get a token, first login via /api/admin/login/.

🎯 Example Requests
📌 Admin Login

URL: POST http://127.0.0.1:8000/api/admin/login/

Body:


{

  "email": "admin@example.com",
  
  "password": "password123"
  
}

Response:

{

  "refresh": "your_refresh_token",
  
  "access": "your_access_token"
  
}

🤝 Contributing

Feel free to fork this repository and submit pull requests!

⚡ License

This project is open-source and available under the MIT License.

✅ Now, Commit the README.md to GitHub

git add README.md
git commit -m "Added README documentation with MySQL (XAMPP) connectivity"
git push origin main

✅ Your project is now fully documented for GitHub, including MySQL connectivity with XAMPP! 🚀
Let me know if you need any modifications. 😊
