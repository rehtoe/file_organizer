import os 
import shutil

# dictionary of file extensions to look for
fextensions = {
    ".pdf" : "Documents",       # documents
    ".doc" : "Documents", 
    ".docx" : "Documents", 
    ".odt" : "Documents", 
    ".txt" : "Documents", 
    ".png" : "Pictures",        # pictures
    ".jpg" : "Pictures", 
    ".jpeg" : "Pictures", 
    ".gif" : "Pictures", 
    ".mp3" : "Music",           # music
    ".wav" : "Music", 
    ".AAC" : "Music", 
    ".mp4" : "Videos",          # videos
    ".avi" : "Videos", 
    ".flv" : "Videos", 
    ".wmv" : "Videos", 
    ".mov" : "Videos", 
    ".a" : "Archives",          # archives
    ".rar" : "Archives", 
    ".zip" : "Archives", 
    ".7z" : "Archives", 
    ".targz" : "Archives", 
    ".csv" : "Data",            # data
    ".json" : "Data", 
    ".xml" : "Data", 
    ".xlsx" : "Data", 
    "" : "", 
}

# Folder to Organize Files into
directories = ["Archives", "Data", "Documents", "Music", "Other", "Pictures", "Videos"]

home_directory = os.path.join(os.path.expanduser('~'))
directory = os.path.join(home_directory, "file_organizer")
def go_home():
    print("went home")
    comm = "cd " + home_directory
    os.system(comm)
def go_scope():
    print("went scope")
    comm = "cd " + directory
    os.system(comm)

if(not os.path.exists(directory)):
    print("directory no exist, me work")
    go_home()
    os.makedirs(directory, exist_ok=True)

def directory_logic():
    go_scope()
    for foldername in directories:                         #     checks to ensure directories exists for program to execute
        ph_dir = os.path.join(directory, foldername)       #     working_directory (file_organizer for test)
        os.makedirs(ph_dir, exist_ok=True)                 #        Archives 
                                                           #        Data
                                                           #        Documents
                                                           #        Music
                                                           #        Other
                                                           #        Pictures
                                                           #        Videos

def file_cleanup():
    go_scope()
    for foldername in directories:
        ph_dir = os.path.join(directory, foldername)
        if(not os.path.exists(ph_dir)):
            continue
        if(not len(os.listdir(ph_dir))):
            comm = "rmdir " + ph_dir
            os.system(comm)

def organize_files():
    go_scope()
    print(directory)
    for filename in os.listdir(directory):
        print(filename)
        

def main():
    directory_logic() # ensures directory structure
    organize_files() # read the function name.....
    file_cleanup() # deletes folders with no files in them


main()