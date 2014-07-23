#!/usr/bin/python

import os,argparse,goslate,langid

def translate():

    T = goslate.Goslate()
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="file to be translated")
    parser.add_argument("target", help="Language to be translated to.")
    parser.add_argument("source",help="Source Language.")
    parser.add_argument("new", help="Name of new file.")

    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print("No such file")



    else:

        file = open(args.file,'r')
        tar = file.read()
        file.close()

        text = T.translate(tar,args.target,args.source)
        new = open(args.new,'wb')
        new.write(text.encode('utf-8'))





if __name__ == '__main__':
    translate()
