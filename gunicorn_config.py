import os

graceful_timeout = 666
timeout = 333
keep_alive = 6
workers = os.getenv('GUNICORN_WORKER_NUM', 4)
bind = "0.0.0.0:8000"
module = "tmo:application"
