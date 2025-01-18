import os

workers = os.getenv('GUNICORN_WORKER_NUM', 4)
bind = "0.0.0.0:8000"
module = "tmo:application"
