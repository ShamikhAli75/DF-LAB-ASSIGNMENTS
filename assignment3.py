#!/usr/bin/python -tt
import argparse
import os
import yara
parser = argparse.ArgumentParser()
parser.add_argument('directory',help='path of directory')
parser.add_argument('rule',help='path of rule file')
args = parser.parse_args()
dir = args.directory
rule = yara.compile(filepath=args.rule)
for root, dirs, files in os.walk(dir):
    for filename in files:
        f = os.path.join(root, filename)
        if os.path.isfile(f):
                a = open(f,"r").read()
                if rule.match(f):
                     print(f)
                     print("matched")
                else:
                     print(f)
                     print("Not matched")
                	
        	
