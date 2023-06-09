from os import environ

bind = '0.0.0.0:' + environ.get('PORT', '8000')
worker_class = 'uvicorn.workers.UvicornWorker'
workers = 1
keepalive = 10
threads = 4
max_requests = 1000
pidfile = "/tmp/neuron-asgi.pid"
