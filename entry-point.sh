#!/usr/bin/dumb-init /bin/sh

./manage.py runserver 0.0.0.0:8000 &  # launch a process in the background
webpack --watch  # launch another process in the foreground
