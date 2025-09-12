import os
import sys
import filehandler

working = os.getcwd()
cpath = working+"config.json"

if not os.is_file(f"{working}Carl.jpg"):
    sys.exit()

def read_config(filename:String):
    if os.is_file(f"{working}config.json"):
        config = open(cpath,'r')
        print(config)
        config = filehandler.encode(config)
        with open(working+"config.org","W") as file:
            file.write(config)
        config.close()
    else:
        sys.exit()
