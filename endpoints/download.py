from time import sleep
from core.library import api


def latest(req, file_type:str, *args, **kwargs):
  return api.data({ "url": "", "name": "" })


def lts(req, *args, **kwargs):
  return api.data({ "url": "", "name": "" })
