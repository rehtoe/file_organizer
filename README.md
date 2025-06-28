# Python File Organizer  

Automatically sorts files into predefined folders (`Documents`, `Pictures`, `Music`, etc.) in `~/file_organizer` (Unix) or `C:\Users\username\file_organizer` (Windows).  

### **How It Works**  
- Creates `file_organizer` in your home directory with 7 subfolders:  
  ```plaintext
  Archives, Data, Documents, Music, Other, Pictures, Videos 
  ``` 
- Moves files based on their extensions (e.g., .pdf → Documents, .mp4 → Videos).
- Recursively cleans up empty folders.

### **Usage**
- Move all Files and folders into `.../file_organizer` 
- Run python script:
  ```bash
  python organize.py
  ```

### **Requirements**
- Python 3.x
- Libraies: os, shutil

### **Notes**
- Hardcoded paths (modify script to change).
- Skips hidden files/directories.
- File Extension Support:
  - Archives: .a, .rar, .zip, .7z, .gz
  - Data: .csv, .json, .xml, .xlsx
  - Documents: .pdf, .doc, .docx, .odt, .txt
  - Music: .mp3, .wav, .AAC, 
  - Other: EVERYTHING ELSE
  - Pictures: .png, .jpg, .jpeg, .gif
  - Videos: .mp4, .avi, .flv, .wmv, .mov

### **Thank You**
- To [Cole831](https://github.com/cole831) for the massive help with Use Logic, Test Cases, and Development. Would not have been able to concurrently test Windows without him. 