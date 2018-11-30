# Un Webapp en Contenedores.

## Secciones

1. Docker
    1. Introducción a Docker: que es y como funciona.
    2. Introducción a `docker-compose`.
    3. Ejemplo de como usar Docker y `docker-compose`: Jekyll.
2. Configuración de una applicación Django.
    1. Configuración local: desarrollo, logs, pruebas y debug.
        - Instala `virtualenv`: `pip install virtualenv`.
        - Corre Django `runserver`: `./manage.py runserver 0.0.0.0:8000`
        - Corre Pruebas: `./manage.py test -v2`
        - Corre `ipdb`: `python -m ipdb manage.py runserver 0.0.0.0:8000` o `python -m ipdb manage.py runserver 0.0.0.0:8000 --nothreading --noreload`
    2. Configuración en producción: Servidor HTTP (Nginx), Servidor WSGI (uwsgi/gunicorn), Aplicación (Django)
    3. Por que diferentes configuraciones?
    4. Por que estas configuraciones?
3. La imagen completa.
    1. Pros y contras de correr estos servicios con y sin contenedores.
    2. Moviendo una aplicación Django a contenedores (contenerizando).
    3. Configuración local: desarrollo, logs, tests, debug.
    4. Configuración en producción: Servidor HTTP, Servidor WSGI, Applicación (Django).
    5. Tips para ir a QA/producción.
4. Recomendaciones.
    1. Manejo de Docker local.
    2. Manejo de contenedores local y en servidores.
