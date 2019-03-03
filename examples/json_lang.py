# import this and you can import JSON files, too,
# provided they don't actually end in .json but in .py
# or do not have any ending.
import json
from a_bad_idea import add_implementation

def json_parser(code, module):
  module.value = json.loads(code)

add_implementation("json", json_parser)
