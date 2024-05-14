# Test task for Kokoc Group 


## Technologies Used

- Python 3.9
- Django 2.2.16
- PostgreSQL
- Docker

## Installation of the project:
Clone the repository and change into it on the command line:

	git clone https://github.com/mityay36/kokoc.git

Make your own .env file in main directory. All required variables are listed in .env.example

#### Start Docker Compose in daemon mode

    docker-compose -f docker-compose.yml up --build

#### Make migrations and collect static of your project
    docker-compose -f docker-compose.yml exec backend python manage.py makemigrations
    docker-compose -f docker-compose.yml exec backend python manage.py migrate
    docker-compose -f docker-compose.yml exec backend python manage.py collectstatic
    docker-compose -f docker-compose.yml exec backend cp -r /app/collected_static/. /backend_static/static/

#### Perform your own superuser
    docker-compose -f docker-compose.yml exec backend python manage.py createsuperuser

#### Manage the command
    docker-compose -f docker-compose.yml exec backend python manage.py load_currencies

### Congrats! Now you can access the application at [localhost](http://localhost:8000)

## Author
[Dmitry Pokrovsky](https://github.com/mityay36)