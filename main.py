#! /usr/bin/python3
from src import *
from src.utils import *


lines = parse('standard.md')
result_lines = []
file = open("RESULT_README.md", "w", encoding="UTF-8")
for line in lines:
    tokens = parse_into_tokens(line)
    for token in tokens:
        response = input(token.question+": ")
        line = replace(token, response, line)
    result_lines.append(line +"\r")

file.writelines(result_lines)
