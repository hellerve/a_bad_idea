import xml.etree.ElementTree
from a_bad_idea import add_implementation

def xml_parser(code, module):
  module.value = xml.etree.ElementTree.fromstring(code)

add_implementation("xml", xml_parser)
