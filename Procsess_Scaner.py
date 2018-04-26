import psutil
import time


class Procsess_Scanner:
    def __init__(self,t):
        self.t=t

    def write_prosses_change (self):
        old_dict={}
        file = open("processList.txt","a+")
        for proc in psutil.process_iter():
            s=str(proc.pid)+", "+proc.name()
            file.write(s)
            file.write("\n")
            old_dict[proc.name()]=proc.pid
        file.write("\n")
        file.close()
        new_dict = {}


        while(1):
            change=open("Status_Log.txt","a+")
            file = open("processList.txt", "a+")
            for procs in psutil.process_iter():
                s = str(procs.pid) + ", " + procs.name()
                file.write(s)
                file.write("\n")
                new_dict[procs.name()]=procs.pid


            for temp1 in new_dict:
                if not old_dict.has_key(temp1):
                    print "   1111"
                    change.write(str(new_dict[temp])+" , "+temp)
                    change.write("\n")


            for temp2 in old_dict:
                if not new_dict.has_key(temp2):
                    print "     222"
                    change.write(str(old_dict[temp2]) +", "+temp2)
                    change.write("\n")
            change.close()
            file.close()
            old_dict.clear()
            for temp in new_dict:
                old_dict[temp]=new_dict[temp]
            new_dict.clear()
            time.sleep(self.t)
