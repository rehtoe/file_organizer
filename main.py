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
    ".gz" : "Archives", 
    ".csv" : "Data",            # data
    ".json" : "Data", 
    ".xml" : "Data", 
    ".xlsx" : "Data", 
    69420666 : "Other", 
}

# Folder to Organize Files into
directories = ["Archives", "Data", "Documents", "Music", "Other", "Pictures", "Videos"]

home_directory = os.path.join(os.path.expanduser('~'))
directory = os.path.join(home_directory, "file_organizer")

# go to home directory
def go_home():
    comm = "cd " + home_directory
    os.system(comm)

# go to file organizer directory
def go_scope():
    comm = "cd " + directory
    os.system(comm)

def go_dir(dirrr):
    comm = "cd " + dirrr
    os.system(comm)

# if organizer does not exist, create 
if(not os.path.exists(directory)):
    go_home()
    os.makedirs(directory, exist_ok=True)
    
# checks if directories exists, if not make them
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

# deletes any empty folders
def file_cleanup():
    go_scope()
    for foldername in directories:
        ph_dir = os.path.join(directory, foldername)
        if(not os.path.exists(ph_dir)):
            continue
        if(not len(os.listdir(ph_dir))):
            comm = "rmdir " + ph_dir
            os.system(comm)

def organize_files(orgFolder):
    go_dir(orgFolder)
    for filename in os.listdir(orgFolder):
        if filename in directories:
            continue
        print(filename)
        root, extension = os.path.splitext(filename)
        if extension in fextensions:
            ph_dir = os.path.join(directory, fextensions[extension], filename)
            shutil.move(os.path.join(orgFolder, filename), ph_dir)
            print(f"Moved: {filename} to {fextensions[extension]}")
        elif not os.path.isdir(filename) and extension == "":
            ph_dir = os.path.join(orgFolder, filename)
            organize_files(ph_dir)
        else:
            ph_dir = os.path.join(directory, fextensions[69420666], filename) 
            shutil.move(os.path.join(orgFolder, filename), ph_dir)
            print(f"Moved: {filename} to {fextensions[69420666]}")

def main():
    directory_logic() # ensures directory structure
    organize_files(directory) # read the function name.....
    file_cleanup() # deletes folders with no files in them


main()