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
    program_arr = []

    for program in program_dict:
        program_arr.append(Program(program["name"], program["path"]))
    
    return program_arr