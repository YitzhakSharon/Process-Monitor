import os
from time import gmtime, strftime
import time
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR
from datetime import datetime

class change_scanner:
    def __init__ (self,name_file1,time1,time2):
        self.filename=name_file1
        if time1<=time2:
            self.time1=time1+"\n"
            self.time2=time2+"\n"
        else:
            self.time1=time2+"\n"
            self.time2=time1+"\n"

    def change (self):
        if not self.filename.endswith(".txt"):
            self.filename+=".txt"
        if(os.path.exists(os.path.abspath(self.filename))):
            os.chmod(self.filename, S_IWUSR | S_IREAD)
        file=open(self.filename,"r+")
        dicttime1={}
        dicttime2={}
        lines=file.readlines()
        index=0

        for line in lines:
            temp=line.split(",")
            index+=1
            if self.time1 == temp[temp.__len__()-1]:
                break
            elif self.time1 == temp[temp.__len__()-1]:
                break

        while index< lines.__len__() and lines[index] != "\n":
            temp=lines[index].split(",")
            dicttime1[temp[1]]=temp[0]
            index+=1
            if(index == lines.__len__()):
                break

        index=0
        for line in lines:
            temp=line.split(",")
            index += 1
            if(self.time2 is temp[temp.__len__()-1]):
                break

        while index<lines.__len__() and lines[index]is not "\n" :
            temp=lines[index].split(",")
            dicttime2[temp[1]]=temp[0]
            index+=1
            if(index == lines.__len__()):
                break

        for temp1 in dicttime1:
            if not dicttime2.has_key(temp1):
                print str(dicttime1[temp1])+"  "+temp1

        for temp2 in dicttime2:
            if not dicttime1.has_key(temp2):
                print str(dicttime2[temp2])+"  "+temp2


a=change_scanner("processList","2018-05-03 18:29:28","2018-05-03 18:31:10")
a.change()
