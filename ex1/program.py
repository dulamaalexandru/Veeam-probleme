from pickle import TRUE
import psutil
import os
nume_proces = input("insert process name \n")
interval = input("inset interval ")
# nume_proces="C:\Program Files\Google\Chrome\Application\chrome.exe"
os.startfile(nume_proces)
proc_curent = ""
for proc in psutil.process_iter():
    if proc.name() == nume_proces.split("\\")[-1]:    
        proc_curent=proc
file = open("result.txt", 'w')      
while TRUE :
    cpu_usage = proc_curent.cpu_percent(float(interval))/psutil.cpu_count()
    memory_info = proc_curent.memory_info()
    num_handles = proc_curent.num_handles()
    file.write("CPU USAGE: " + str(round(cpu_usage,2)) + " WORKING SET: " + str(memory_info.wset) + " PRIVATE BYTES: " + str(memory_info.private) + " NUM OF OPEN HANDLES: " + str(num_handles) + "\n" )