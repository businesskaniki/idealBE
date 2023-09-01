# Django Project Setup Guide

This guide explains how to set up a Django project within a Python virtual environment. Using a virtual environment ensures that project dependencies are isolated and can be easily managed.

## Prerequisites

Before starting, ensure that you have the following prerequisites installed on your system:

- Python 3.x
- `virtualenv` (you can install it using `pip install virtualenv`)

## Project Setup

1. *Clone the Repository*

   Clone the project repository to your local machine:

   ```
   git clone https://github.com/businesskaniki/idealBE.git
   cd idealBE

   Create a Virtual Environment

Create a Python virtual environment for the project. Replace env with your preferred virtual environment name:



python3 -m venv env

Activate the Virtual Environment

Activate the virtual environment:

On Linux/macOS:



source env/bin/activate

On Windows:



.\env\Scripts\activate

You should see the virtual environment's name in your terminal prompt, indicating that it's active.

Install Project Dependencies

Install the required Python packages within the virtual environment using pip. Make sure you are inside your project directory and that your virtual environment is activated:



pip install -r requirements.txt

Create the Database

Run the following commands to create the database tables:



python manage.py makemigrations
python manage.py migrate

Create a Superuser

Create an admin superuser to manage the Django admin panel and access your project:



python manage.py createsuperuser

Follow the prompts to set up the superuser credentials.

Run the Development Server

Start the development server:



python manage.py runserver

Your Django project should now be accessible at http://127.0.0.1:8000/.

Access the Admin Panel

You can access the Django admin panel at http://127.0.0.1:8000/admin/ and log in using the superuser credentials created in step 6.