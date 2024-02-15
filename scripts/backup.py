from datetime import datetime
import os


def backup():
    return f'python3 /application/manage.py dumpdata > /application/backups/{datetime.today().date()}.json'

os.system(backup())
