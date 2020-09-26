import os
from .structures import Token

root = 'src'
resources = 'resources'


def parse(template: str):
    file = open(os.path.join(os.getcwd(), root, resources,
                             template), "r", encoding="utf8")
    lines = []
    for line in file.readlines():
        lines.append(line.strip())
    file.close()
    return lines


def parse_into_tokens(line: str, start_index: int = 0):
    if "${" not in line or len(line) < 3:
        return []
    start = line.index("${")
    end = line.index("}")
    multiline = False
    if "*" in line:
        end = line.index("*")
        multiline = True
    question = line[start+2:end]
    collected_tokens = [
        Token(question, multiline, start+2 + start_index, end + start_index)]
    collected_tokens.extend(parse_into_tokens(line[end+1:], end + 1))
    return collected_tokens


def replace(token: Token,  word: str, line: str):
    return line[:token.start - 2] + word + line[token.end+1:]


def get_question_from(token: Token):
    question = token.question
    if token.multiline:
        question += "(type 'stop' when you finish): "
    else:
        question += ": "

    return question

def prepare(response: str):
    if 'stop' not in response:
        return response
    end = response.find('stop')
    return response[:end]
