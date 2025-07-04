// interface header file
#include <iostream>
#include <string>
#include <map>

// Argument overloads, enum = char(UPPERCASE)
enum class ArgumentOverload{
    NONE = 0,
    USAGE = 1,

    TARGET_DIRECTORY = 68, // 68, 100 = D, d
    TARGET_LOCATION = 76, // 76, 108 = L, l
    DEFAULT_LOCATION = 1,
};

// Handler object
struct Handler{
    public:
    std::map<int, std::string> arguments;
    std::string ROOT_LABEL;
    Handler();
    Handler(int argc, char* argv[]);
    void help();

    int error(ArgumentOverload argumentType);
    void parser();
    private:
    int ERROR_usage();
    int ERROR_sortDirectory();
    int ERROR_locationDirectory();
};