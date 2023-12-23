from .. import API
from web.settings import BASE_DIR
from core.library import api, listdir


def fetch(req, *args, **kwargs):
  ''' returns the contents of a specific documentation file '''
  try:
    detail = api.get_json(req)['document'].split(':')
    with open(f"{BASE_DIR}/api/{API.NAME}/documents/{detail[1]}.md") as doc_file:
      return api.data({
        "title": detail[2],
        "document": doc_file.read()
      })
  except:
    return api.data({
      "title": None,
      "document": None
    })


def survey(req, *args, **kwargs):
  ''' returns a list of available documentation categories and files '''
  try:
    doc_files = {}
    doc_dir = f"{BASE_DIR}/api/{API.NAME}/documents"
    for entry in listdir(doc_dir):
      category = entry.replace('_', ' ').title()
      doc_files[category] = {
        "title": category,
        "source": entry,
        "docs": [
          {
            "title": ' '.join(x.split('.md')[0].split('_')[1:]).title(),
            "source": x.split('.md')[0]
          } for x in sorted(listdir(f"{doc_dir}/{entry}"))
        ]
      }
    return api.data(doc_files)
  except:
    return api.data({})
