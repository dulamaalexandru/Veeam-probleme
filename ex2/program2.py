import sys
import os 
import shutil
from datetime import datetime
import time
def get_time():
    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    return current_time

folder_source = sys.argv[1]
folder_replica = sys.argv[2]
time_interval = sys.argv[3]
log_path = sys.argv[4]

log_file = open(log_path + "\\log.txt", "a")
while True:
    try:
        for file_name in os.listdir(folder_source):
            for destination_file_name in os.listdir(folder_replica):
                if file_name == destination_file_name:
                    if os.path.getsize(folder_source + "\\" + file_name) == os.path.getsize(folder_replica + "\\" + destination_file_name) :
                        sursa = open(folder_source + "\\" + file_name, "r")
                        destinatie = open(folder_replica + "\\" + destination_file_name, "r")
                        text_sursa = sursa.read()
                        text_destinatie = destinatie.read()
                        if text_sursa != text_destinatie:
                            shutil.copyfile(folder_source + "\\" + file_name, folder_replica + "\\" + destination_file_name)
                            print("[" + get_time() + "] " + "Copied file " + file_name + " from source to destination" + "\n")
                            log_file.write("[" + get_time() + "] " + "Copied file " + file_name + " from source to destination" + "\n")
                    else:
                        shutil.copyfile(folder_source + "\\" + file_name, folder_replica + "\\" + destination_file_name)
                        print("[" + get_time() + "] " + "Copied file " + file_name + " from source to destination" + "\n")
                        log_file.write("[" + get_time() + "] " + "Copied file " + file_name + " from source to destination" + "\n")

            if not (file_name in os.listdir(folder_replica)):
                shutil.copyfile(folder_source + "\\" + file_name, folder_replica + "\\" + file_name)
                print("[" + get_time() + "] " + "Copied file " + file_name + " from source to destination" + "\n")
                log_file.write("[" + get_time() + "] " + "Copied file " + file_name + " from source to destination" + "\n")

        for destination_file_name in os.listdir(folder_replica):   
            if not(destination_file_name in os.listdir(folder_source)):
                os.remove(folder_replica + "\\" + destination_file_name)
                print(("[" + get_time() + "] " + "Deleted file " + destination_file_name + " from destination" + "\n"))
                log_file.write("[" + get_time() + "] " + "Deleted file " + destination_file_name + " from destination" + "\n")
    except: 
        continue
    time.sleep(int(time_interval))