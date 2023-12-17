from time import sleep
from core.library import api


def latest(req, *args, **kwargs):
  sleep(2)
  return api.success()


def lts(req, *args, **kwargs):
  sleep(2)
  return api.success()
