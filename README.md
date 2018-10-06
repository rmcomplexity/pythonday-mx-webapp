# pyladies-django-docker
Source to follow PyLadies class about Django and Docker on 05/Oct/2018

## Outline

1. Docker
    1. Introduction to Docker: What is it and overview of how it works.
        - **Build image:** `docker build -t class/nginx`.
        - **Run container:** `docker run --rm --name my_site -p 8080:80 class/nginx`.
        - **Mount a volume:** `docker run --rm --name my_site -p 8080:80 -v $(pwd)/imgs:/srv/www/site/imgs class/nginx`
    2. Introduction to docker-compose: What is it and how it works.
        - **Run docker-compose:** `docker-compose up`
    3. Examples on how to use Docker and docker-compose: Running different services.
2. Django application setup
    1. Local setup: development, logging, testing, debugging
    2. Production setup: HTTP Server (Nginx), WSGI server (uwsgi/gunicorn), Application server (Django)
    3. Why different setups?
    4. Why these specific setups?
3. Putting it all together
    1. Pros and cons of the HTTP server, WSGI server, Application server running locally and in containers.
    2. Moving a Django application into containers (containerization).
    3. Local setup: development, logging, testing, debugging
    4. Production setup: HTTP Server (Nginx), WSGI server (uwsgi/gunicorn), Application server (Django)
    5. Tips on deploying to staging/production.
4. Recommendations
    1. Local docker management.
    2. Container management locally and in remote servers.
    3. Future Work.
