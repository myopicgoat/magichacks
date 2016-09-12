#!/usr/bin/env python
from sys  import argv
from os.path import splitext
from re import match

#############
# TODO
# find and set execution count to nul
# find and remove everything within outputs [ ... ]
# below is what we want.
   # "execution_count": null,
   # "metadata": {
   #  "collapsed": false
   # },
   # "outputs": [],



##########################################

if len(argv)<2:
    error("Not enough arguments given, you should provide the path to a .ipynb file and that of an output file.")
inFile  = argv[1]
# default name
outFile = splitext(inFile)[0]+"_template.ipynb"
# given name
if len(argv)>2:
    outFile = argv[2] # will overwrite if exists, be careful

##########################################

tag_magic = '"%%'
tag_open  = '"#<cca>'
tag_close = '"#</cca>'

flag_write = True

buffsize    = 0
maxbuffsize = 100
buff        = []

with open(inFile,"r") as fin:
    with open(outFile,"w") as fout:
        for line in fin.readlines():
            ls    = line.strip()
            if ls[0:len(tag_magic)]==tag_magic:
                continue
            elif ls[0:len(tag_open)]==tag_open:
                flag_write = False
            if flag_write:
                fout.write(line)
            elif ls[0:len(tag_close)]==tag_close:
                # match the line to check if there's a return or not
                # if there isn't (last line of the cell), add an empty line
                # otherwise it corrupts the IPYNB
                if(not match(r".*\\n",ls)):
                    fout.write("\"\"")
                flag_write = True
