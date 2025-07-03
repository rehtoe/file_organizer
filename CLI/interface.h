// interface header file
#include <iostream>
#include <string>

enum class ArgumentOverload{
    NONE = 0,
    TARGET_DIRECTORY = 68, // 68, 100 = D, d
    TARGET_LOCATION = 76, // 76, 108 = L, l
    DEFAULT_LOCATION = 1,
};

struct Handler{
    public:
    Handler();
    Handler(int argc, char* argv[]);
    void help();
    int error(ArgumentOverload argumentType);
    private:
    int ERROR_usage();
    int ERROR_sortDirectory();
    int ERROR_locationDirectory();
};