import json

buffer:str = ""

def encode(filetext:str):
    try:
        conf = json.loads(filetext)
    except:
        conf = filetext
    print(conf)
    level = 0

    buffer:str=""
    if type(conf) == dict:
        for x in conf.keys():
            y = conf[x]
            if type(y) != dict:
                buffer = buffer + f"*{x}\n\t{y}"
    else:
        print("Config file isn't valid json syntax, please fix it")
    def search(object,recursion:int=0):
        global buffer
        if recursion > 0:
            print(f"Checking recursive dict at level {recursion} with value {object}")

        match object:
            case str():
                print("Type: header")
                if object.startswith("#l"):
                    pass #handle the literals dumb bass (fih)
                buffer = buffer+object

            case list():
                print("Type: list")
                if object[0] == "#l":
                    pass #handle the literals dumb bass (fih)

            case dict():
                print("Type: entry")
                for x in object.keys():
                    y = object[x]
                    search(y,recursion+1)

            case _:
                print(f"unknown element {object}")
    return(buffer)