import os
import sys

working = os.getcwd()
cpath = working+"config.json"

def read_config(filename:String):
    if os.is_file(f"{working}config.json"):
        config = open(cpath,'rw')
        print(config)
        with open(working_"config.org","W") as file:
            file.write(config)
        config.close()
    else:
        sys.exit()