from pprint import pprint
from pymiere import Pymiere, utils
import os

pymiere = Pymiere()
data = pymiere.eval_script(filepath=os.path.join(__file__, "..", "jsxExtractStartVars.jsx"))
utils.write_json_file(os.path.join(__file__, "..", "class_datas", "start_vars.json"), data)
pprint(data, depth=2)
