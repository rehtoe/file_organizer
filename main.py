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

os.system("cd")
directory = os.path.join(os.path.expanduser('~'), "file_organizer")     # Working Directory directory to organize
                                                                        # using file_organizer as a test directory

if(not os.path.exists(directory)):
    comm = "mkdir file_organizer"
    os.system("cd")
    os.system(comm)

def directory_logic():
    os.system("cd file_organizer")
    for foldername in directories:                         #     checks to ensure directories exists for program to execute
        ph_dir = os.path.join(directory, foldername)       #     working_directory (file_organizer for test)
        if(not os.path.exists(directory)):                 #        Archives 
            comm = "mkdir " + foldername                   #        Data
            os.system(comm)                                #        Documents
                                                           #        Music
                                                           #        Other
                                                           #        Pictures
                                                           #        Videos
    os.system("cd ../")

def file_cleanup():
    for foldername in directories:  
        ph_dir = os.path.join(directory, foldername)
        if(not len(os.listdir(ph_dir))):
            comm = "rm " + ph_dir
            os.system(comm)

def organize_files():
    for filename in os.listdir(directory):
        print(filename)
        

def main():
    directory_logic() # ensures directory structure
    organize_files() # read the function name.....
    file_cleanup() # deletes folders with no files in them


main()