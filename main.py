import os
import sys
import filehandler

working = os.getcwd()
cpath = working+"config.json"

if not os.path.exists(f"{working}Carl.jpg"):
    sys.exit()

def read_config():
    if os.path.exists(f"{working}config.json"):
        config = open(cpath,'r')
        print(config)
        config = filehandler.encode(config.read())
        with open(working+"config.org","W") as file:
            file.write(config)
    else:
        sys.exit()
