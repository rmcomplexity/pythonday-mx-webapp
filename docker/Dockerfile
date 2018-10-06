FROM python:3.7


COPY requirements.txt /tmp/.

RUN pip install --no-cache-dir -r /tmp/requirements.txt

RUN useradd -m portal

RUN mkdir -p /srv/www/vanilla && chown -R portal /srv/www/vanilla

USER portal

WORKDIR /srv/www/vanilla
