#!/bin/sh

exec gunicorn -b :5000 --workers 3 --access-logfile - --error-logfile - autoapp:app --preload
