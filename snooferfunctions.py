import pandas as pd
import re
import docx
import os

badpassworddb = []
baddbtxtfiles =[]
filepaths = []
p = []
text = []
textclean =[]

class functions():

    #makes the badpassword list
    def builddb ():
      #path to all the password files you want to use
        path = (r"C:\Leakedpwds")
        for root, dirs, files in os.walk(path):
           path = root.split(os.sep)
           for file in files:
               metafilter = ".meta"
               if ".txt" in file and metafilter not in file:
                   baddbtxtfiles.append(os.path.join(root, file))
                   
               else:
                   pass

    #takes the contents of the library of badpassword files and turns it into a array
    def db ():
        for files in baddbtxtfiles:
            with open(files, encoding='utf-8', errors = 'ignore') as file_in:
                for line in file_in:
                    reg = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
                    if len(line) >= 8 and ("http://" not in line) and ("https://" not in line) and (".com" not in line):
                        if (bool(re.search('[a-zA-Z]',line)) == True) and (bool(re.search('[0-9]',line)) == True) and (reg.search(line) != None):
                            badpassworddb.append(line.strip("\n"))

                    else:
                        pass


    def locate (path):
        for root, dirs, files in os.walk(path):
            for file in files:
                metafilter = ".meta"
                if ".txt" in file or ".docx" in file and metafilter not in file:
                    f = str(os.path.join(root, file))
                    functions.filetype(f)
                    
                else:
                    pass



    # builds word doc array
    def docxs(path):
        doc = docx.Document(path)
        for words in doc.paragraphs:
            text.append(words.text)


    def txtclean(file):
        with open(file, 'r') as t:
            tread = t.readlines()
            for line in tread:
                textclean.append(line.strip('\n'))



    #  functions based on file types
    def filetype(data):
        if ".txt" in data:
            functions.txtclean(data)
            i = 0
            limit = (len(textclean) * len(badpassworddb))
            while i <= limit:
                for pwd in badpassworddb:
                    for line in textclean:
                        var = re.escape(str(pwd))
                        if re.findall(var, line, flags=re.IGNORECASE):
                            print("found " + str(pwd) + " in")
                            print(data)
                            p.append("\n" + str(pwd) + " --------------" + "\n" + data)
                            i += 1
                        else:
                            i += 1
                            
            if i >= limit:
                textclean.clear()

        if ".docx" in data:
            functions.docxs(data)
            i = 0
            limit = (len(text)*len(badpassworddb))
            while i <= limit:
                for pwd in badpassworddb:
                    #print(pwd)
                    for line in text:
                        var = re.escape(str(pwd))
                        if re.findall(var, line, flags=re.IGNORECASE):
                            print("found " + str(pwd) + " in")
                            print(data)
                            p.append("\n" + str(pwd) + " --------------" + "\n" + data)
                            i += 1
                        else:
                            i += 1

            if i >= limit:
                text.clear()
                        

        if ".xlsx" in data:
            pass
            #work in progress
        else:
            pass

    def exporting ():
        with open("output.csv", "w") as file:
            file.writelines(p)
            file.close()
