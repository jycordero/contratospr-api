#!/bin/bash

set -e

postgres_ready(){
python manage.py shell << END
import sys
import psycopg2
from django.db import connections
try:
    connections['default'].cursor()
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

case "$1" in
  "start")
    until postgres_ready; do
      >&2 echo "==> Waiting for Postgres..."
      sleep 1
    done

    echo "==> Running migrations..."
    python manage.py collectstatic --noinput
    python manage.py migrate

    echo "==> Running dev server..."
    python manage.py runserver 0.0.0.0:8000
    ;;

  "start-worker")
    tasks_packages=$(find ./contratospr -type d -name tasks | sed s':/:.:g' | sed s'/^..//' | xargs)
    tasks_modules=$(find ./contratospr -type f -name tasks.py | sed s':/:.:g' | sed s'/^..//' | sed s'/.py$//g' | xargs)
    all_modules="$tasks_packages $tasks_modules"

    echo "Discovered tasks modules:"
    for module in $all_modules; do
      echo "  * ${module}"
    done
    echo

    dramatiq --watch ./contratospr --processes 2 $all_modules
    ;;

  *)
    exec "$@"
    ;;
esac
