# main

[![Build Status](https://travis-ci.org/qulc/main.svg?branch=master)](https://travis-ci.org/qulc/main)
[![codecov](https://codecov.io/gh/qulc/main/branch/master/graph/badge.svg)](https://codecov.io/gh/qulc/main)

main is an open source **social network** built with [Python][0] using the [Django Web Framework][1].


## Install Guide
```bash
$ git clone https://github.com/qulc/main.git
$ cd main/

# Use Python 3.6 virtualenv or pyenv
$ python -m venv {VENV} && source venv/bin/activate
$ python -m pip install -r requirements.txt

# Add DATABASE_URL, REDIS_URL config to env
$ export REDIS_URL=redis://localhost:6379/0
$ export DATABASE_URL=postgres://postgres:@localhost:5432/main

# Create Tables
$ python manage.py makemigrations
$ python manage.py migrate

# Test
$ python manage.py test

# Run
$ python manage.py collectstatic
$ python manage.py runserver
```

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
[2]: https://main.qulc.me/
[3]: https://travis-ci.org/
[4]: https://www.heroku.com
