# Quiz-App-Using-Django

Introduction

This project is a Quiz Game web application built using Python and Django. The game allows users to take quizzes on various topics, track their scores, and review their performance.
Features

    Score tracking and result display
    Admin interface for adding and managing quizzes

Prerequisites

    Python (3.6 or higher)
    Django (3.0 or higher)

Installation
Step 1: Clone the Repository

First, clone the repository to your local machine:

sh

    git clone https://github.com/shobhitkasturey/myProject.git
    cd myProject

Step 2: Create a Virtual Environment

Create a virtual environment to manage dependencies:

sh

    python -m venv env

Activate the virtual environment:

On Windows:

sh

    .\env\Scripts\activate

On macOS/Linux:

sh

    source env/bin/activate

Step 3: Install Dependencies

Install the required Python packages:

sh

    pip install django

Step 4: Set Up the Database

Run the following commands to set up the database:

sh

    python manage.py makemigrations
    python manage.py migrate

Step 5: Create a Superuser

Create a superuser to access the Django admin interface:
Give username and password for the superuser

sh

    python manage.py createsuperuser

Step 6: Run the Development Server

Start the development server:

sh

    python manage.py runserver


Project Structure

    myProject/: The main Django project directory.
        settings.py: Configuration file for the Django project.
        urls.py: URL routing for the project.
    myApp/: The Django app for the quiz game.
        models.py: Database models for quizzes and questions.
        views.py: Views for handling requests and rendering templates.
        urls.py: URL routing for the quiz app.
        templates/quiz/: HTML templates for the quiz pages.
        static/quiz/: Static files (CSS, JavaScript) for the quiz app.

Usage

Taking a Quiz

    Each quiz consists of single-choice questions.
    After completing the quiz, users can see their score and review correct and incorrect answers.

Admin Interface

    Admin users can log in to the Django admin interface at http://127.0.0.1:8000/admin.
    From the admin interface, admins can add new quizzes, questions, and manage user accounts.

Contributing

Contributions are welcome! Please follow these steps to contribute:

    Fork the repository.
    Create a new branch for your feature or bugfix.
    Commit your changes and push the branch to your forked repository.
    Create a pull request with a description of your changes.



For any questions or feedback, please contact shobhitkasturey@gmail.com


