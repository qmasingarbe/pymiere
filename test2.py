import pymiere.core as pc
from pprint import pprint

pprint(pc.eval_script("JSON.stringify(f, internal_variables_replacer, 0, 1)"))