import json

def encode(filetext:String):
    try:
        conf = json.loads(filetext)
    except:
        conf = filetext
    print(conf)
    level = 0

    buffer:str=""

    for x in conf.keys():
        y = conf[x]
        if type(y) != dict:
            buffer = buffer + f"*{x}\n\t{y}"

    def search(object,recusion:int=0):
        if recusion > 0:
            print(f"Checking recursive dict at level {recursion} with value {object}")

        match object:
            case str:
                print("Type: header")
                if object.begins_with("#l"):
                    pass #handle the literals dumb bass (fih)

            case list:
                print("Type: list")
                if object[0] == "#l":
                    pass #handle the literals dumb bass (fih)

            case dict:
                print("Type: entry")
                for x in object.keys():
                    y = object[x]
                    search(y,recusion+1)

            case _:
                print(f"unknown element {x}")
                
        if is_recursive:
            pass
    return(buffer)