import json
import os
import sys
import fstools

def load():
    with open("filesystem.json","r") as fs:
        return json.load(fs)

def get_path_from_way(way):
	atual=""
	for pasta in way:
		atual+=f"/{pasta}"
	return atual

def save_fs(fs):
    with open("filesystem.json","r") as arq:
        json.dump(fs,arq,indent=4)

fs=load()
os.system("clear")
exec(fs["sbin"]["login.py"])


