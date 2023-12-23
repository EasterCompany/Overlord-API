from . import API
from .endpoints import download, documentation

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

API.path(
  "documentation/fetch",
  documentation.fetch,
  "fetch the content for a documentation page"
)

API.path(
  "documentation/survey",
  documentation.survey,
  "fetch a list of available documentation categories and files"
)
