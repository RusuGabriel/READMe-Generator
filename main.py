#! /usr/bin/python3
from src import *
from src.utils import *
import os


lines = parse('standard.md')
result_lines = []
file = open("RESULT_README.md", "w", encoding="UTF-8")
for line in lines:
    tokens = parse_into_tokens(line)
    for token in tokens:
        response = input(get_question_from(token))
        if token.multiline:
            while 'stop' not in response:
                response = response + '\n' + input()
        line = replace(token, prepare(response), line)
    result_lines.append(line + '\n')

file.writelines(result_lines)
