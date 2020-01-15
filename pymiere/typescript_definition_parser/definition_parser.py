import os
import re
from pprint import pprint

FUNCTION_REGEX = re.compile(r"declare function (?P<name>[a-zA-Z0-9]+)\((?P<args>.*)\): (?P<return>[a-zA-Z]+)")
METHOD_REGEX = re.compile(r"(?P<name>[a-zA-Z0-9]+)\((?P<args>.*)\): (?P<return>[a-zA-Z]+)")
VAR_REGEX = re.compile(r"declare var (?P<name>[a-zA-Z0-9]+): (?P<type>[a-zA-Z0-9]+)")
PROP_REGEX = re.compile(r"(?P<readonly>readonly )?(?P<name>[a-zA-Z0-9_\?]+):[ \t]{1,}(?P<type>[a-zA-Z0-9]+)")
TYPE_CORRESPONDENCE = {"string": "str", "boolean": "bool", "void": None, "number": "float", "any[]": "list"}


class Lines(object):
    """
    Cursor object on list of line
    """
    def __init__(self, lines):
        self.lines = lines
        self.line_count = len(lines)
        self.current_line_number = 0

    def current_line(self):
        return self.lines[self.current_line_number - 1].strip()

    def next_line(self):
        self.current_line_number += 1
        if self.current_line_number > self.line_count:
            raise EOFError()
        return self.current_line()


def parse_interface_block(data, name="interface"):
    line = data.current_line()
    result = dict()
    splitted_line = line.split(" ")
    result["name"] = splitted_line[splitted_line.index(name) + 1]
    result["props"] = list()
    if "}" not in line:
        while True:
            next_line = data.next_line().strip()
            if "}" in next_line:
                break
            if next_line.startswith("/**"):
                result["props"].append(("comment", parse_comment_block(data)))
            elif not next_line or any([next_line.startswith(c) for c in ["new", "(", "<T>", "[", "):"]]):
                pass
            elif next_line.count("(") > 1:
                pass
            elif "(" in next_line and ")" in next_line:
                result["props"].append(("method", parse_method_block(data)))
            else:
                result["props"].append(("property", parse_prop_block(data)))
            if "}" in next_line:
                break
    return result



def parse_var_block(data):
    m = VAR_REGEX.match(data.current_line())
    result = dict()
    result['name'] = m.group('name')
    result['type'] = TYPE_CORRESPONDENCE.get(m.group('type'), m.group('type'))
    return result


def parse_prop_block(data):
    # print("property for : ", data.current_line())
    line = data.current_line().strip()
    if line.startswith("static"):
        line = line.replace("static", "").strip()
    m = PROP_REGEX.match(line)
    result = dict()
    result['readonly'] = True if "readonly" in m.groupdict().keys() else False
    result['name'] = m.group('name')
    result['type'] = TYPE_CORRESPONDENCE.get(m.group('type'), m.group('type'))
    return result


def parse_method_block(data):
    # print("method grab for : ", data.current_line())
    m = METHOD_REGEX.match(data.current_line())
    result = dict()
    result['name'] = m.group('name')
    result['return'] = TYPE_CORRESPONDENCE.get(m.group('return'), m.group('return'))
    result['args'] = dict()
    args = m.group("args").split(",") if m.group("args") else list()
    for arg in args:
        result_arg = dict()
        arg_data = arg.split(":")
        if len(arg_data) != 2:
            raise ValueError()
        arg_name = arg_data[0].strip()
        arg_value = arg_data[1].strip()
        result_arg["optional"] = "?" in arg_name
        name = arg_name.replace("?", "").strip()
        result_arg["type"] = TYPE_CORRESPONDENCE.get(arg_value, arg_value)
        result['args'][name] = result_arg
    return result


def parse_function_block(data):
    m = FUNCTION_REGEX.match(data.current_line())
    result = dict()
    result['name'] = m.group('name')
    result['return'] = TYPE_CORRESPONDENCE.get(m.group('return'), m.group('return'))
    result['args'] = dict()
    args = m.group("args").split(",") if m.group("args") else list()
    for arg in args:
        result_arg = dict()
        arg_data = arg.split(":")
        if len(arg_data) != 2:
            raise ValueError()
        arg_name = arg_data[0].strip()
        arg_value = arg_data[1].strip()
        result_arg["optional"] = "?" in arg_name
        name = arg_name.replace("?", "").strip()
        result_arg["type"] = TYPE_CORRESPONDENCE.get(arg_value, arg_value)
        result['args'][name] = result_arg
    return result


def parse_comment_block(data):
    """
    parse comment in declaration
    :param data:
    :return:
    """
    result = data.current_line()
    while True:
        next_line = data.next_line()
        result += next_line
        if next_line.startswith("*/"):
            result = result.replace("/**", "").replace("*/", "").replace("*", "").strip()
            break
    if "@param" not in result:
        return result
    new_result = dict()
    result = result.split("@param")
    new_result["comment"] = result[0]
    new_result["args"] = dict()
    for arg_data in result[1:]:
        arg_data = arg_data.strip().split(" ")
        new_result["args"][arg_data[0]] = " ".join(arg_data[1:])
    return new_result


def parse_definition(lines):
    """
    global lexer + parser
    :param lines:
    :return:
    """
    data = Lines(lines)
    lexed_data = list()
    while True:
        try:
            # comment
            line = data.next_line()
            if line.startswith("/**"):
                lexed_data.append(("comment", parse_comment_block(data)))
            if line.startswith("declare function "):
                lexed_data.append(("function", parse_function_block(data)))
            if line.startswith("declare class "):
                lexed_data.append(("class", parse_interface_block(data, name="class")))
            if line.startswith("declare var "):
                lexed_data.append(("var", parse_var_block(data)))
            if line.startswith("declare interface ") or line.startswith("interface "):
                lexed_data.append(("class", parse_interface_block(data)))
        except EOFError:
            break
    pprint(lexed_data)
    return lexed_data


def read_definition_file(folder):
    """
    read declaration file from folder
    :param folder:
    :return:
    """
    files = os.listdir(folder)
    valid_files = [os.path.join(folder, f) for f in files if os.path.isfile(os.path.join(folder, f)) and f.endswith(".d.ts")]
    all_data = list()
    for f in valid_files:
        print("Parsing typescript definition file '{}'".format(f))
        with open(f, "r", encoding="utf8") as of:
            data = of.readlines()
        all_data.extend(parse_definition(data))

    result = {"class": dict(), "var": dict(), "func": dict()}
    # parse data
    previous = None
    for lex in all_data:
        if lex[0] != "comment" and previous is not None and previous[0] == "comment":
            if previous[1]:  # empty comment
                if lex[0] == "var":
                    result["var"][lex[1]["name"]] = previous[1]
                elif lex[0] == "function":
                    if isinstance(previous[1], dict):
                        result["func"][lex[1]["name"]] = previous[1]
                    else:
                        result["var"][lex[1]["name"]] = {"comment": previous[1], "args": list()}
                elif lex[0] == "class":
                    if lex[1]["name"] in result["class"]:
                        raise ValueError()
                    result["class"][lex[1]["name"]] = {"comment": previous[1], "props": dict()}
        if lex[0] == "class":
            if lex[1]["name"] not in result["class"]:
                result["class"][lex[1]["name"]] = {"comment": None, "props": dict()}
            previous_prop = None
            for prop in lex[1]['props']:
                if prop[0] != "comment" and previous_prop is not None and previous_prop[0] == "comment":
                    if not previous_prop[1]:  # empty comment
                        continue
                    if isinstance(previous_prop[1], dict):
                        result["class"][lex[1]["name"]]["props"][prop[1]["name"]] = previous_prop[1]
                    else:
                        result["class"][lex[1]["name"]]["props"][prop[1]["name"]] = {'comment': previous_prop[1]}
                previous_prop = prop
        previous = lex

    return result


if __name__ == "__main__":
    result = read_definition_file(os.path.join(__file__, "..", "definition_files"))
    pprint(result, depth=2)
    from pymiere.utils import write_json_file
    write_json_file(os.path.join(__file__, "..", "definition_data.json"), result)
