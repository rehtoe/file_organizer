// interface source file
#include "interface.h"

Handler::Handler(){}
Handler::Handler(int argc, char* argv[]){ for(int i=0;i<argc;i++){ arguments[i]=argv[i]; } ROOT_LABEL = arguments[0]; }
void Handler::help(){
    std::cout << "Command Usage Docs\n"
            << "'" << ROOT_LABEL << "' is the leading command.\n"
            << "'-D/-d  :   target directory to sort.'\n"
            << "'-L/-l  :   location to move the files.'\n";
}
int Handler::error(ArgumentOverload argumentType){}
int Handler::ERROR_usage(){}
int Handler::ERROR_sortDirectory(){}
int Handler::ERROR_locationDirectory(){}