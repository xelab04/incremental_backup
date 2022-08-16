import csv
import os
import paths
import shutil
from termcolor import colored

def potato(path):
    file_array = []
    for item in os.listdir(path):
        if os.path.isdir(path+item):
            file_array += potato(path+item+"/")
        else:
            #print(path+item)
            try:
                ti_m = os.path.getmtime(path+item)
            except:
                ti_m = "None"
            file_array.append([path+item,ti_m])

    return file_array


def read_csv(csv_addr):
    result = {}
    with open(csv_addr) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                result[row[0]] = row[1]
            except:
                pass
            #file_addr = date

    return result

def write_csv(csv_addr,csv_contents):
    for item in csv_contents.items():
        print(item)
    with open(csv_addr,"w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_contents.items())
        print("written")

def compare(file_array,csv_contents):
    write_array = []
    for pair in file_array:
        file_addr,ti_m = pair

        if file_addr in csv_contents.keys():
            if str(csv_contents[file_addr]) != str(ti_m):
                #if the last date modified has changed
                write_array.append(file_addr)
                csv_contents[file_addr] = ti_m

        else:
            #not in csv_contents - ie new file
            write_array.append(file_addr)
            csv_contents[file_addr] = ti_m
    return write_array,csv_contents

def all_slash(string):
    index_array = []
    for i in range(len(string)):
        if string[i] == "/":
            index_array.append(i)
    return index_array

def copy_file(usb_addr,write_array):
    for file_path in write_array:
        src = file_path
        dst = usb_addr + file_path
        slash_index = get_last_slash(dst)
        dst = dst[:slash_index:]
        while dst[-1] == " ":
            dst = dst[:-1:]
        dst += "/"
        #dst = dst[:slash_index:] + "/"
        if "'" in src:
            print(colored((f"**{src}** has forbidden character ' in it. Skipping."), 'red'))
            continue
        if not os.path.exists(dst):
            os.makedirs(dst)
        shutil.copyfile(src, dst)
        #os.system(f"cp '{src}' '{dst}'")

def get_last_slash(string):
    index = None
    for i in range(len(string)):
        if string[i] == "/":
            index = i
    return index

source = paths.source
usb_addr = paths.usb_addr
csv_addr = paths.csv_addr

file_array = []
for i in range(len(source)):
    file_array += potato(source[i])

csv_contents = read_csv(csv_addr)

write_array,csv_contents = compare(file_array,csv_contents)

write_csv(csv_addr,csv_contents)

copy_file(usb_addr,write_array)
