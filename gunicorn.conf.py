# import multiprocessing

bind = "0.0.0.0:8000"
limit_request_fields = 80
limit_request_field_size = 4096
workers = 2 # int((multiprocessing.cpu_count() * 2) + 1)
worker_connections = 800
