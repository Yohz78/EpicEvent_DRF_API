# Développer une architecture back-end sécurisée en utilisant Django ORM

## Installation

## Project Installation

This locally-executable django application can be executed from http://localhost:8000/api using the following steps.

Installation and execution using venv and pip

Clone this repository using <code>git clone https://github.com/Yohz78/Projet_12</code>

Move to the LITReview root folder with <code>cd Projet_12</code>

Create a virtual environment for the project with <code> py -m venv env </code>on windows or <code> python3 -m venv env </code> on macos or linux.

Activate the virtual environment with <code> env\Scripts\activate</code> on windows or <code> source env/bin/activate</code> on macos or linux.

Install project dependencies with <code> pip install -r requirements.txt</code>

Move to the API file : <code>cd EpicEventsCRM </code>

## Postgresql Installation

[Install postgresql](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads). After installation, set up the database according to the information in settings.py using the Postgresql desktop app or the Postgresql command.

## Database migrations

After the project and postgresql installation, follow the following steps :

<code> python manage.py makemigrations </code>

<code> python manage.py migrate </code>

## Project use

Afterward, create a superuser :

<code> python manage.py createsuperuser </code>

Follow the instruction in order to create an admin.

Then, to start the server, use :

<code> python manage.py runserver </code>

When the server is running, the API can be accessed at http://localhost:8000/

## Usage

The API can be used both from your navigator, using a local URL such as http://127.0.0.1:8000, or from a software like Postman.

The admin interface is available at the /admin URL for superuser or staff users.
