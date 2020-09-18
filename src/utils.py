import os

root = 'src'
resources = 'resources'


def parse(template: str):
    file = open(os.path.join(os.getcwd(), root, resources, template), "r")
    lines = file.readlines()
    result = []
    for line in lines:
        result.append(line.strip())
    return result
    
