import os
import sys
import re

# NILAI AWAL
argumen = ""
index = 0
locations = []

# MENDEFINISIKAN FUNGSI
# me-read file dan mengembalikan string perbaris
def open_file(location):      
    open_file = open(location , "r")
    open_file = open_file.readlines()
    return open_file

# mencari kata dari file
def match_string(cari_kata , line):
    search_string = re.search(cari_kata , line)
    if argumen == "-i":
        search_string = re.search(cari_kata , line , re.IGNORECASE)
    if argumen == "-w":
        line = " " + line + " "     # agar whole word pada ujung baris dapat terdeteksi
        search_string = re.search(f" \\b{cari_kata}\\b " , line)
    return search_string      

# mencari kata (dengan wildcard) dari file
def match_string_wildcard(cari_kata , line):
    wildcard = cari_kata.split("*")
    search_string = re.search(f"{wildcard[0]}.*{wildcard[1]}" , line) 
    if argumen == "-i":
        search_string = re.search(f"{wildcard[0]}.*{wildcard[1]}" , line , re.IGNORECASE)
    if argumen == "-w":
        line = " " + line + " "     # agar whole word pada ujung baris dapat terdeteksi
        search_string = re.search(f" \\b{wildcard[0]}.*{wildcard[1]}\\b " , line)
    return search_string

# print output
def print_line(location , index , line):
    print(f"{location: <40s} line {index: <3d} {line[:40]}")

# MENG-ASSIGN INPUT MENGGUNAKAN SYS KE VARIABEL
nama_python = sys.argv[0]
cari_kata = sys.argv[-2]
input_file = sys.argv[-1]

if len(sys.argv) == 4:      # jika argumen dimasukkan
    argumen = sys.argv[1]
    if argumen != "-w" and argumen != "-i":
        print("Argumen program tidak benar.")
        sys.exit()

if cari_kata.count("*") > 1:
    print("Argumen program tidak benar.")
    sys.exit()

# PENGECEKAN INPUT BERUPA FILE ATAU FOLDER
if os.path.isfile(input_file) == True:              # jika file langsung dapat diakses
    dir = input_file
    locations.append(dir)  

elif os.path.isdir(input_file) == True:             # jika file berada dalam folder
    for folder , subfolder , files in os.walk(input_file):
        for file in files:        
            dir = os.path.join(folder , file)
            locations.append(dir)       # menyimpan kumpulan direktori file dalam variabel locations
else:
    print(f"Path {input_file} tidak ditemukan")     # jika file tidak ditemukan
    sys.exit() 
    
# IMPLEMENTASI FUNGSI
for location in locations:          # iterasi file dari kumpulan file
    text = open_file(location)            
    for line in text:                
        line = line.strip("\n")
        line = line.strip()
        
        index += 1  # urutan baris teks

        if "*" in cari_kata:
            search_string = match_string_wildcard(cari_kata , line)
        else:
            search_string = match_string(cari_kata , line)

        if search_string:   # jika terdapat kata yang sama pada baris teks
            print_line(location , index , line)

    index = 0   # mereset urutan baris teks setiap file  

sys.exit()