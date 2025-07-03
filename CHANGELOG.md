# **CHANGELOG.md**  

## v0.3
- **Added**:
  - Boilerplate GUI model to organize-gui.py, further functionality needed.

## v0.2
- **Added**:  
  - Recursive folder cleanup (`file_cleanup()`).  
  - Support for nested directory scanning.
- **Changed**
  - Generalized a Function to change the Current Directory to passed path argument
  - organize_files() -> organize_files(directoryPath)
- **Fixed**:    
  - Edge cases for deleting empty folders.
  - Edge case for interacting with Folders/Files with spaces in their names.  

## v0.1
- **Added**:  
  - Path handling for cross-platform compatibility (Unix/Windows).
  - File Sorting, updated organize_files() 
- **Changed**
  - 'Other' category for sorting unsupported file types
- **Fixed**: 
  - Program Concatenating incorrect File Paths.

## Initial Commit
- **Boiler Plate**
  - List of Program Directory Labels
  - Dictionary for File Extension -> Label Lookup
  - Functions to change Current Directory to Home Directory or Program Directory
  - Functions: directory_logic(), organize_files(), file_cleanup() 
  - 6 file categories