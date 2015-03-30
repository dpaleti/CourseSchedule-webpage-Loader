#!/usr/bin/env python

#hbg# cleans the doc.json
# generates arch.json with just arch courses in 20141

import csv
import re
import json
import xlrd
from collections import OrderedDict
import subprocess


#import simplejson as json

from pprint import pprint
from mmap import mmap,ACCESS_READ

subprocess.call("/Users/cl2720/desktop/springnew/new/workcode3/find.py", shell = True)
subprocess.call("/Users/cl2720/desktop/springnew/new/workcode3/images.py", shell = True)
subprocess.call("/Users/cl2720/desktop/springnew/new/workcode3/facsyl.py", shell = True)

#subprocess.Popen("find.py 1", shell=True)
 
# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('sample1.xls')
sh = wb.sheet_by_index(0)


# Create syllabi DICT
dict2 = {}
sf = open ("syllabi.txt", "r")
for l in sf:
    temp = (l.replace('\n','')).split(';')
    dir = temp[0]
    key = temp[1]
    fn1 = temp[2]
    fn2 = temp[3]

    if key in dict2:
        dict2[key].append({'dir':dir, 'wn': fn1, 'pdfn':fn2})
    else:
        dict2[key] = [{'dir':dir, 'wn': fn1, 'pdfn':fn2}]

sf.close()



# Create images DICT
dict3 = {}
sf = open ("images.txt", "r")
for l in sf:
    temp = (l.replace('\n','')).split(';')
    dir1 = temp[0]
    key1 = temp[1]
    fn3 = temp[2]
    fn4 = temp[3]

    if key1 in dict3:
        dict3[key1].append({'dir':dir1, 'wn': fn3, 'pdfn':fn4})
    else:
        dict3[key1] = [{'dir':dir1, 'wn': fn3, 'pdfn':fn4}]

print dict3
sf.close()


############################
# Create faculty syllabi DICT
dict4 = {}
sf = open ("facsyl.txt", "r")
for l in sf:
    temp = (l.replace('\n','')).split(';')
    dir2 = temp[0]
    key2 = temp[1] 
    fn5 = temp[0]
    fn6 = temp[3]

    if key2 in dict4:
        dict4[key2].append({'dir':dir2, 'wn': fn5, 'pdfn':fn6})
    else:
        dict4[key2] = [{'dir':dir2, 'wn': fn5, 'pdfn':fn6}]

#print dict4
sf.close()

############################






 
# List to hold dictionaries
courses_list = []
 
# Iterate through each row in worksheet and fetch values into dict
for rownum in range(1, sh.nrows):
    courses = OrderedDict()
    row_values = sh.row_values(rownum)
    courses['CampusCode'] = row_values[0]
    courses['ExamMeet'] = row_values[1]
    courses['PrefixLongname'] = row_values[2]
    courses['TypeCode'] = row_values[3]
    courses['CourseTitle'] = row_values[4]
    courses['MinUnits'] = row_values[5]
    courses['CallNumber'] = row_values[6]
    courses['BulletinFlags'] = row_values[7]
    courses['PrefixName'] = row_values[8]
    courses['Instructor1Name'] = row_values[9]
    courses['ClassNotes'] = row_values[10]
    courses['sess'] = row_values[11]
    courses['SchoolName'] = row_values[12]
    courses['req'] = row_values[13]
    courses['ChargeMsg2'] = row_values[14]
    courses['ChargeMsg1'] = row_values[15]
    courses['TypeName'] = row_values[16]
    courses['NumFixedUnits'] = row_values[17]
    courses['MaxUnits'] = row_values[18]
    courses['ExamDate'] = row_values[19]
    courses['SchoolCode'] = row_values[20]
    courses['Approval'] = row_values[21]
    courses['DivisionCode'] = row_values[22]
    courses['type'] = row_values[23]
    courses['CourseSubtitle'] = row_values[24]
    courses['Term'] = row_values[25]
    courses['CampusName'] = row_values[26]
    courses['DepartmentName'] = row_values[27]
    courses['DepartmentCode'] = row_values[28]
    courses['MaxSize'] = row_values[29]
    courses['ChargeAmt1'] = row_values[30]
    courses['ChargeAmt2'] = row_values[31]    
    courses['Meets2'] = row_values[32]
    courses['Meets3'] = row_values[33]
    courses['Meets1'] = row_values[34]
    courses['Meets6'] = row_values[35]
    courses['Meets4'] = row_values[36]
    courses['Meets5'] = row_values[37]
    courses['SubtermName'] = row_values[38]
    courses['NumEnrolled'] = row_values[39]
    courses['DivisionName'] = row_values[40]
    courses['Instructor3Name'] = row_values[41]
    courses['Instructor4Name'] = row_values[42]
    courses['Course'] = row_values[43]
    courses['SubtermCode'] = row_values[44]

    
    temp = courses['Course'][4:8] + courses['Course'][9:12]
    temp1 = temp[:4]

    if temp in dict2:
        courses['syllabi'] = dict2[temp]
    elif temp1 in dict2:
        courses['syllabi'] = dict2[temp1]
    else:
        print temp

    temp2 = courses['Course'][4:8] + courses['Course'][9:12]
    if temp2 in dict3:
        courses['images'] = dict3[temp2]
############################
    temp5 = int(row_values[6])
    courses['CallNumber'] = str(temp5)

    if courses['CallNumber'] in dict4:
        temp4 = courses['CallNumber']
        courses['facsyl'] = dict4[temp4]
        print ' call number found'  
############################

    courses['EnrollmentStatus'] = row_values[45]
    courses['Instructor2Name'] = row_values[46]
    courses_list.append(courses)

 
# Serialize the list of dicts to JSON
j = json.dumps(courses_list, indent = 1)
 
# Write to file
with open('main.json', 'w') as f:
    f.write(j)
    
