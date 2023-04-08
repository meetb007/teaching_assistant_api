import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

secrets = os.environ
if os.path.exists(os.path.join(BASE_DIR, 'secrets.json')):
    with open(os.path.join(BASE_DIR, 'secrets.json')) as secrets_file:
        secrets = json.load(secrets_file)


def get_secret(setting):
    try:
        return secrets[setting]
    except KeyError:
        raise Exception("Set the {} setting".format(setting))


DATABASE_URL = get_secret('DATABASE_URL')
JWT_SECRET_KEY = get_secret('JWT_SECRET_KEY')
