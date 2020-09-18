import os

root = 'src'
resources = 'resources'


def parse(template: str):
    file = open(os.path.join(os.getcwd(), root, resources,template), "r", encoding="utf8")
    lines = []
    for line in file.readlines():
        lines.append(line.strip())
    return lines
