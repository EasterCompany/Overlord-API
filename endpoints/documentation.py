from web.settings import BASE_DIR
from core.library import api


def fetch(req, *args, **kwargs):
  try:
    detail = api.get_json(req)['document'].split(':')
    with open(f"{BASE_DIR}/api/overlord/documents/{detail[1]}.md") as doc_file:
      return api.data({
        "title": detail[2],
        "document": doc_file.read()
      })
  except:
    return api.data({
      "title": None,
      "document": None
    })
