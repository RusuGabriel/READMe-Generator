#! /usr/bin/python3
from src.utils import *

lines = parse('standard.md')
result = []
file = open("RESULT_README.md", "w", encoding="UTF-8")
for line in lines:
    if "${" in line:
        firstPart = line.split("${")[0]
        question = line.split("${")[1].split("}")[0]
        secondPart = line.split("}")[1]
        response = input(question)
        line = firstPart + response + secondPart[1]
    result.append(line +"\n")
file.writelines(result)
