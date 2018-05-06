import psutil
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import Handler
import os
from time import gmtime, strftime
import time
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR


class Procsess_Scanner:
    def __init__(self,t):
        self.t=t


    def writeProssesChange (self):
        new_dict={}
        old_dict={}
        if(os.path.exists(os.path.abspath("processList.txt"))):
            os.chmod('processList.txt', S_IWUSR | S_IREAD)
        file = open("processList.txt","a+")
        filename_proc = os.path.abspath("processList.txt")
        os.chmod('processList.txt', S_IREAD | S_IRGRP | S_IROTH)  # readonly
        current_time_proc =datetime.fromtimestamp(os.stat(filename_proc).st_mtime)
        for proc in psutil.process_iter():
            s=str(proc.pid)+", "+proc.name()+" ,"+strftime("%Y-%m-%d %H:%M:%S", gmtime())
            if str(current_time_proc) == str(datetime.fromtimestamp(os.stat(filename_proc).st_mtime)) :
                os.chmod('processList.txt', S_IWUSR | S_IREAD)
                file.write(s)
                file.write("\n")
                old_dict[proc.name()]=proc.pid
                current_time_proc = datetime.fromtimestamp(os.stat(filename_proc).st_mtime)
                os.chmod('processList.txt', S_IREAD | S_IRGRP | S_IROTH)  # readonly
            else:
                print  "some write to the processList file with out premotion"
        file.write("\n")
        if(os.path.exists(os.path.abspath("Status_Log.txt"))):
            os.chmod('Status_Log.txt', S_IWUSR | S_IREAD)
        change = open("Status_Log.txt","a+")
        filename_change=os.path.abspath("Status_Log.txt")
        os.chmod('Status_Log.txt', S_IREAD | S_IRGRP | S_IROTH)  # readonly
        current_time_change=datetime.fromtimestamp(os.stat(filename_change).st_mtime)
        current_time_proc = datetime.fromtimestamp(os.stat(filename_proc).st_mtime)
        change.close()
        while(1):
            # insert the current process to new_dict
            for procs in psutil.process_iter():
                if (str(current_time_proc) == str(datetime.fromtimestamp(os.stat(filename_proc).st_mtime))):
                    os.chmod('processList.txt', S_IWUSR | S_IREAD)
                    s = str(procs.pid) + " , " + procs.name() +" ,"+strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    file.write(s)
                    file.write("\n")
                    new_dict[procs.name()]=procs.pid
                    os.chmod('processList.txt', S_IREAD | S_IRGRP | S_IROTH)
                    current_time_proc = datetime.fromtimestamp(os.stat(filename_proc).st_mtime)
                else:
                    print "some write to the processList file with out premotion"
                #check change in the new process
                if not old_dict.has_key(procs.name()):
                  if(str(current_time_change)==str(datetime.fromtimestamp(os.stat(filename_change).st_mtime))):
                        os.chmod('Status_Log.txt', S_IWUSR | S_IREAD)
                        change = open("Status_Log.txt", "a+")
                        s=str(procs.pid)+" , "+procs.name() +" ,"+strftime("%Y-%m-%d %H:%M:%S", gmtime())
                        change.flush()
                        change.write(s)
                        change.write("\n")
                        os.chmod('Status_Log.txt', S_IREAD | S_IRGRP | S_IROTH)  # readonly
                        change.close()
                        current_time_change = datetime.fromtimestamp(os.stat(filename_change).st_mtime)
                  else:
                       print "some write to the Status_Log file with out premotion"
            os.chmod('processList.txt', S_IWUSR | S_IREAD)
            file.write("\n")
            file.flush()
            os.chmod('processList.txt', S_IREAD | S_IRGRP | S_IROTH)

            for temp2 in old_dict:
                if not new_dict.has_key(temp2):
                    if(str(current_time_change)==str( datetime.fromtimestamp(os.stat(filename_change).st_mtime))):
                        os.chmod('Status_Log.txt', S_IWUSR | S_IREAD)
                        change = open("Status_Log.txt", "a+")
                        s=str(old_dict[temp2]) +" , "+temp2+" ,"+strftime("%Y-%m-%d %H:%M:%S", gmtime())
                        change.write(s)
                        change.flush()
                        change.write("\n")
                        current_time_change = datetime.fromtimestamp(os.stat(filename_change).st_mtime)
                        os.chmod('Status_Log.txt', S_IREAD | S_IRGRP | S_IROTH)  # readonly
                    else:
                        print "some write to the Status_Log file with out premotion"

            old_dict.clear()
            #insert the new process to the current process
            for temp in new_dict:
                old_dict[temp]=new_dict[temp]
            new_dict.clear()
            time.sleep(self.t)

        change.close()
        file.close()





t=input("enter time at secend for scannig: ")
p = Procsess_Scanner(t)
observer = Handler.Observer()
observer.schedule(Handler.MyHandler(), '.')
observer.start()
p.writeProssesChange()




