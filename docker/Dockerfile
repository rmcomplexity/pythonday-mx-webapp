FROM python:3.7

RUN apt-get install dumb-init

COPY requirements.txt /tmp/.

RUN pip install --no-cache-dir -r /tmp/requirements.txt

RUN useradd -m portal

RUN mkdir -p /srv/www/vanilla && chown -R portal /srv/www/vanilla

USER portal

WORKDIR /srv/www/vanilla

CMD ["./manage.py", "runserver", "0.0.0.0:8080"]
