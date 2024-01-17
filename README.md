### Initial Configuration

This project is the first part of my personal portfolio, the other is in a private repository, if you want to clone the code and create your own portfolio using mine as a reference, follow the next steps:

1.- Clone this repository:

                            git clone https://github.com/nicds-dev/portfolio.git 

2.- Create your own virtual environment :

                            virtualenv name_venv or python3 -m venv name_venv 

3.- Active virtual environment.

                            name_venv\Scripts\activate or source name_venv/bin/activate 

4.- Go to the route "django_portfl/" and install libraries.

                            (env) pip install -r requirements.txt 

5.- In the settings.py file create your own configuration for the connection to your database.

6.- In the project base run the commands:

                            (env) python3 manage.py makemigrations
                            (env) python3 manage.py migrate
                            (env) python3 manage.py runserver 
