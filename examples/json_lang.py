# import this and you can import JSON files, too,
# provided they don't actually end in .json but in .py
# or do not have any ending.
import json
from a_bad_idea import add_implementation

add_implementation("json", json.loads)
