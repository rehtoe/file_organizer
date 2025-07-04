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
int Handler::error(ArgumentOverload argumentType){
    switch(argumentType){
        default:
        case 0:
            return int(ArgumentOverload::NONE);
        case 1:
            return ERROR_usage();
        case 68:
            return ERROR_sortDirectory();
        case 76:
            return ERROR_locationDirectory();
    }
}
void Handler::parser(){
    for(int i = 1; i < arguments.size(); i += 2){
            if(arguments.at(i) == "-d" || arguments.at(i) == "-D"){

            }else if(arguments.at(i) == "-l" || arguments.at(i) == "-L"){
                
            }
    }
}
int Handler::ERROR_usage(){ return int(ArgumentOverload::USAGE); }
int Handler::ERROR_sortDirectory(){ return int(ArgumentOverload::TARGET_DIRECTORY); }
int Handler::ERROR_locationDirectory(){ return int(ArgumentOverload::TARGET_LOCATION); }