from .app import App
import sys
from pathlib import Path

def console():
    ops = options_parser(sys.argv[1:])
    
    QdocApp = App(ops["file_paths"]) 
    QdocApp.Start()

def options_parser(ops):
    ops_dict = {}
    flag=""
    for i in ops:
        if i == "-f":
            flag = "F"
            ops_dict["file_paths"] = []
            continue
        if flag == "F":
            ops_dict["file_paths"].append(i)
    return ops_dict

