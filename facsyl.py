#!/usr/bin/env python                                                                                               

import os, os.path
import glob

# local directory of all the syllabi
filepath = '/Users/cl2720/desktop/springnew/new/workcode3/webapp/faculty'


master = os.path.abspath(filepath)

#print master

fin = {}

f = open("facsyl.txt","w")


for mrn in os.listdir(master):  # folder of folders
    if os.path.isdir(os.path.join(master,mrn)):  # if folder is directory
        
        if (len(os.listdir(os.path.join(master,mrn)))) > 0: # number of pdfs > 0
            for pdf in os.listdir(os.path.join(master,mrn)):
                print os.path.join(master,mrn)
                print pdf
                temp = pdf.split("_")
                print temp
                sess = ""
                if len(temp[1]) < 4:
                    sess = temp[1]
                print (temp[0] + sess + ";" + mrn + sess + ";" + pdf)
                f.write(mrn + ";" + temp[0] + ";" + sess + ";" + pdf + "\n")
               
f.close()

