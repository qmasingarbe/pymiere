import os
from pprint import pprint
from pymiere import utils
from pymiere.core import eval_script

data = eval_script(filepath=os.path.join(__file__, "..", "jsxExtractStartVars.jsx"))
utils.write_json_file(os.path.join(__file__, "..", "class_datas", "start_vars.json"), data)
pprint(data, depth=2)
