import json

class Program:
    def __init__(self, name,path):
        self.name = name
        self.path = path

def programEncoder(program):
    if isinstance(program,Program):
        return {"name":program.name,"path":program.path}

def programDecoder(jsonstr):
    program_dict = json.load(jsonstr)

    for program in program_dict:
        pass