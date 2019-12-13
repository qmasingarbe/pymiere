from pprint import pprint
from pymiere import Pymiere, utils

filepath_jsxObjectToPythonObject = r"D:\code\prpro\jsxObjectToPythonObject.jsx"


pymiere = Pymiere()
data = pymiere.eval_script(filepath=filepath_jsxObjectToPythonObject)
print("Result :")
pprint(data, depth=3)

utils.write_json_file(r"D:\code\prpro\classData_videoitem_qe.json", data)

# todo try using https://github.com/Adobe-CEP/Samples/tree/master/PProPanel/jsx PremierePro.d.ts