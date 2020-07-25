#-*- coding:utf-8 -*-

from pdfminer.high_level import extract_text #Import pdfminer module to extract text from PDF
import re #Import re module to use regex

#Set Filename
filename = "resume.pdf"

#Read regex ruleset from ruleset.txt
f = open("./ruleset.txt", "r", encoding='UTF8')
ruleList = []
while True:
    line = f.readline().replace("\n","") #Read ruleset.txt and find find rules by line
    if not line:
        break
    if line[0] != "#": #If rule starts with #, define it as a remark
        ruleList.append(line)
f.close()

text = extract_text(filename) #Extract text from pdf file
text = text.replace("\n","") #Remove \n to search case when text splited with two lines

f = open("result.txt", "w", encoding='UTF8') #Save result as result.txt
#Search text based on ruleset regex
#Print and Save result
for rule in ruleList:
    p = re.compile(rule)
    result = p.findall(text)

    if result != []:
        f.write("Based on ruleset: {}\n".format(rule))
        print("Based on ruleset: {}". format(rule))
        for i in result:
            if(type(i) == tuple):
                i = i[0]
            f.write(i+"\n")
            print(i)
        f.write("\n")
        print("\n")
f.close()