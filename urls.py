from . import API
from .endpoints import download

API.path(
  "download/latest/<str:file_type>",
  download.latest,
  "download latest version of overlord"
)

API.path(
  "download/lts/<str:file_type>",
  download.lts,
  "download lts version of overlord"
)
