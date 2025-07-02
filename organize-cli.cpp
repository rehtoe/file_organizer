/*  using c++ for the cli due 
    gcc accessibility to build the files into executables
    */

/*  Use case:
    CUSTOM LOCATION
    root_label -l "/a/b/"
        root_label  target_location
        organize    /home/USERNAME/
    
    CUSTOM DIRECTORY 
    root_label -d "/a/b/c/"
        root_label  target_directory
        organize    /home/USERNAME/Downloads/
    
    CUSTOM DIRECTORY AND LOCATION
    root_label -d "/a/b/c/" -t "/a/b/"
        root_label  target_directory            target_location
        organize    /home/USERNAME/Downloads/   /home/USERNAME/

    
    */

#define ROOT_LABEL "sort-dir"

enum class ArgumentOverload{
    NONE = 0,
    TARGET_DIRECTORY = 68, // 68, 100 = D, d
    TARGET_LOCATION = 76, // 76, 108 = L, l
    DEFAULT_LOCATION = 1,
};

int main(int argc, char* argv[]){

    return 0;
}