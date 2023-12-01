from .base import *  # noqa: F401,F403
import os

ALLOWED_HOSTS = [os.environ["ALLOWED_HOSTS"]]
DEBUG = False
SECRET_KEY = os.environ["SECRET_KEY"]
