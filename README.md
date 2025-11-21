Django Docker Template
===============

     django-admin startproject --template=https://github.com/ernestjumbe/django-template/zipball/master --extension=py,rst,gitignore,example,toml,Makefile,dev,local,dev,local --name Makefile,start,entryfile,Dockerfile project_name

.. note:: The text following this comment block will become the README.rst of the new project.

## Packages to add

- psycopg2-binary

## Dev packages to add

- django-extensions 3.2.3
- django-debug-toolbar 4.4.6
- werkzeug 3.1.3
- mypy 1.15.0

## Production packages

- gunicorn 23.0.0
- django-robots 6.1
- django-htmlmin 0.11.0